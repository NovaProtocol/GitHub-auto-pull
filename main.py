from git import Repo, Git, exc
import time
import shutil
import os


def auto_git():
    try:
        repo = Repo()
    except exc.InvalidGitRepositoryError:
        if git_password:
            credentials = f'{git_username}:{git_password}@'
        else:
            credentials = ''
        Repo.clone_from(url=f"https://{credentials}github.com/{git_username}/{git_repository}.git", to_path=f'{os.getcwd()}/{git_repository}', branch=branch)
        file_names = os.listdir(f'{os.getcwd()}/{git_repository}')
        for file_name in file_names:
            if file_name == __file__.split('\\')[-1]:
                pass
            else:
                shutil.move(os.path.join(f'{os.getcwd()}/{git_repository}', file_name), os.getcwd())
        repo = Repo()
    print('Intialization Complete')
    while True:
        repo.remotes.origin.fetch()
        if sum(1 for _ in repo.iter_commits('main..origin/main')):
            repo.remotes.origin.pull()
            print('Pulled from repo')
        time.sleep(1)

git_username = 'NovaProtocol'
git_password = "" # optional. Leave blank if repo is public else add token
git_repository = 'GitHub-auto-pull'
branch = 'main'

auto_git()


