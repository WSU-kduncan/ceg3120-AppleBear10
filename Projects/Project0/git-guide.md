# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it. `status` has a sample of what a well done filled in entry looks like.

Entries that are currently crossed out we will get to later in the course that you could go back and write some details on later.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Points to an existing repo and makes a clone or copy of that repo at a new directory at another location
    - Can easily copy entire contents and history of work/projects with a simple command in your terminal
  - `git clone`
- add
  - The add command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit
    - adds all modified and new (untracked) files in the current directory and all subdirectories to the staging area
  - `git add`
- rm
  - To remove tracked files from the Git index. rm gives the option to:
    - remove files from the staging index
    - remove files from the working directory
  - `git rm`
- commit
  - "commit"/saves all staged changes to file(s). It will also have a brief description from the user where you write messages about what changed.
    - commit is a good convention to use. It helps you communicate and collaborate with your team
    - serves as an archive of changes
    - commit messages plays an important role in software development for it records or documents the changes in natural languages during the progress of the project
  - `git commit`
- push
  - Used to upload local repository content to a remote repository
    - Syncs "commits" with remote (GitHub)
    - Ideally should be pushing content after commiting
  - `git push`
- fetch
  - Downloads commits and files from a remote repository into your local repo
    - does not actually make changes into your working files. More like a view on what has happened in that remote repository
  - `git fetch`
- merge
  - Used to join the histories of two or more developments. Benefits:
    - perserves chronology of commits 
    - creates explicit merge commits
  - `git merge`
- pull
  - Fetches (content from remote) and merge it into your local repo copy. Benefits:
    - simplifies collaboration
    - offers more thorough code review and testing possibilities
    - provides visibility into feature work and project progress
  - `git pull`
- branch
  - Lets you create, list, rename, and delete branches
    - essentially an independent line of development
    - good for working on new features or bug fixes because it isolates your work from that of other team members
  - `git branch`
- checkout
  - Lets you navigate between the branches created by git branch
    - helps manage bugs by making it harder for unstable code to merge into the master code repository
  - `git checkout`

- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
  - Contains all information that is necessary for the project and all information relating commits, remote repository address, etc
    - easy to store the data, which is helpful in tracking any file
  - `.git folder`
- .gitignore file
  - Tells Git which files to ignore when committing your project to the GitHub repository. When to use:
    - excludes libraries files that need to be built per system
    - keep excess off GitHub
    - keep secrets off GitHub
  - `.gitignore file`
- ~~.git/hooks~~

## GitHub

- Pull requests
  - Lets you tell others about changes you've pushed to a branch in a repository on GitHub
- SSH authentication to repositories
  - A key that allows you to directly access a repository
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project0
