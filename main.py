from git import Repo

repo = Repo()

print(len(list(repo.iter_commits())))