

# 03. Collaboration & Branching

**Spanish version:** [03 - Colaboración y Ramas.md](03%20-%20Colaboraci%C3%B3n%20y%20Ramas.md)

**Course:** Git & GitHub
**Topic:** Cloning, Permissions, Forking & Branch Management
**Tags:** `#git` `#branching` `#collaboration`



## 1. Repository Cloning & Permissions

Cloning downloads a full copy of a remote GitHub repository to your local machine[cite: 62].

Bash

```bash
# Clone a repository from GitHub
git clone [https://github.com/your-handle/quest-engine.git](https://github.com/your-handle/quest-engine.git)
```


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
git branch feature/boss-ai

# Switch to an existing branch
git switch feature/loot-table

# Create and switch to a new branch in a single command
git checkout -b feature/quest-dialogue
```


## 3. Teamwork & Synchronizing Changes (`git pull`)

When working with others, update your local branch to incorporate changes pushed by team members to the remote repository.

Bash

```bash
# Fetch and merge changes from the remote branch into your current local branch
git pull
```
