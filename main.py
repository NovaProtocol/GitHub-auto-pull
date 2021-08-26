from git import Repo
import time

repo = Repo()

branch = 'main'
repo.remotes.origin.fetch()
x = sum(1 for _ in repo.iter_commits('main..origin/main'))
repo.remotes.origin.pull()
print('done')
time.sleep(5)