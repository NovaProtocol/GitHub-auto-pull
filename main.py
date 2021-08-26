from git import Repo
repo = Repo()
branch = 'main'
repo.remotes.origin.fetch()
commits_diff = repo.git.rev_list('--left-right', '--count', f'{branch}...{branch}@{{u}}')
print(commits_diff)

print(sum(1 for _ in repo.iter_commits('main..origin/main')))
