from git import Repo, Git, exc
import time
import shutil
import os

git_username = 'NovaProtocol'
git_repository = 'GitHub-auto-pull'
branch = 'main'

try:
    repo = Repo()
except exc.InvalidGitRepositoryError:
    Git().clone(f"git://github.com/{git_username}/{git_repository}.git")
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
