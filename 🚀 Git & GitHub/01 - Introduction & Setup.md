
# 01. Introduction & Setup


## 1. Overview & History

Git is a distributed version control system created by Linus Torvalds in 2005 to manage source code history for the Linux kernel. GitHub, founded in 2008, is a cloud-based platform that hosts Git repositories and provides collaboration tools.


### Key Terminology
- **Git:** The local CLI tool that tracks changes in files over time.
- **GitHub:** The web platform hosting remote repositories for sharing and collaboration.
- **Local Repository:** A `.git` folder stored on your local disk containing history drafts.
- **Remote Repository:** The cloud-hosted copy of the project on GitHub.

---


## 2. Environment Verification

Before working with Git, verify installation on your system terminal.

```bash
# Check installed Git version
git --version
````


_Expected output example:_ `git version 2.39.3` (or higher).


## 3. Local Initialization & Remote Linkage

Connecting a local project folder to a newly created empty GitHub repository involves four fundamental steps.


### Step 1: Initialize Local Repository

Navigate to your project directory and initialize tracking:

Bash

```bash
# Verify current directory path
pwd

# Initialize empty Git repository
git init
```

Running `git init` creates a hidden `.git` directory to store local commits and configuration.


### Step 2: Link to Remote GitHub Repository

Attach the GitHub URL as the `origin` remote:

Bash

```bash
# Add connection to remote repository
git remote add origin [https://github.com/username/repository-name.git](https://github.com/username/repository-name.git)
```


### Step 3: Set Default Branch Name

Rename the default branch to `main`:

Bash

```bash
# Rename active branch to main
git branch -M main
```


### Step 4: Verify Connection

Check that the branch setup was successful:

Bash

```bash
# List local branches
git branch
```


_Expected output:_ `* main`
