# GitHub Forks

Forking allows developers to make changes to a project before incorporating into the production environment. The repository that you fork from is called the upstream repository.

Read more in the GitHub documentation:

[About forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)

[Configuring a remote repository for a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork)

[Sycning a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork?platform=mac)

## Syncing a fork

In order to keep your local copy of the repository synced with the upstream source, you have to create a remote that points to that upstream repository.
```
$ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
$ git remote -v
> origin git@github.com:YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin git@github.com:YOUR_USERNAME/YOUR_FORK.git (push)
> upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
> upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

Once you have a remote configured for the upstream repository, you can fetch and merge from the default branch.
```
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
```