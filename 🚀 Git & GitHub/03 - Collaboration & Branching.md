

# 03. Collaboration & Branching


## 1. Repository Cloning & Permissions

Cloning downloads a full copy of a remote GitHub repository to your local machine[cite: 62].

Bash

```bash
# Clone a repository from GitHub
git clone [https://github.com/username/repository-name.git](https://github.com/username/repository-name.git)
````


### GitHub Access Levels

- **Read:** Allows users to view and clone the repository.
    
- **Write:** Allows users to commit, create branches, and push changes.
    
- **Admin:** Full repository management access.
    


### Forking

If you do not have write access, **forking** creates a personal copy of the repository under your own GitHub account to experiment freely without affecting the original codebase.


## 2. Branch Management (`git branch` & `git switch`)

Branches allow parallel development without modifying the main line of code (`main`).

Bash

```bash
# Create a new branch
git branch <branch-name>

# Switch to an existing branch
git switch <branch-name>

# Create and switch to a new branch in a single command
git checkout -b <branch-name>
```


## 3. Teamwork & Synchronizing Changes (`git pull`)

When working with others, update your local branch to incorporate changes pushed by team members to the remote repository.

Bash

```bash
# Fetch and merge changes from the remote branch into your current local branch
git pull
```