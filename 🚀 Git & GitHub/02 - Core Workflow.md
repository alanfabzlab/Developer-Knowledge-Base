
# 02. Core Workflow & Local Push


## 1. Working Directory, Staging & Local Repository

Git categorizes workspace changes into three primary areas:

- **Working Directory:** The project folder on your computer. Changes here are tracked locally by Git.
- **Staging Area:** A temporary prep area where you select specific changes before saving them.
- **Local Repository:** The `.git` directory containing committed snapshots of your project.

---


## 2. Staging Changes (`git add`)

The `git add` command moves changes from the working directory to the staging area.

Bash

```bash
# Add a single file to staging
git add file_name.ext

# Add all changed files in the working directory
git add .

# Add all files matching a specific extension
git add *.ext
````

## 3. Saving Snapshots (`git commit`)

A commit captures a snapshot of the staged files with an explanatory message.

Bash

```bash
# Create a commit with a message
git commit -m "feat(scope): descriptive message"
```

_Good practice:_ Keep commit messages short, clear, and descriptive (e.g., using Conventional Commits).


## 4. Status Tracking & Pushing (`git status` & `git push`)

### Inspecting Workspace Status

Bash

```bash
# Check staged, unstaged, and untracked files
git status
```


### Pushing to Remote Repository

Bash

```bash
# First time pushing a new branch (sets upstream)
git push -u origin main

# Subsequent pushes
git push
```


## 5. Repository Documentation (`README.md`)

A `README.md` file serves as the core documentation for a repository, explaining what the project does, how to set it up, and how to maintain it.