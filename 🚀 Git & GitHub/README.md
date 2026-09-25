
# 🚀 Git & GitHub: Version Control & Collaboration (MOC) 

<p align="center"> <img src="https://img.shields.io/badge/TOOL-GIT-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge"> <img src="https://img.shields.io/badge/PLATFORM-GITHUB-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"> <img src="https://img.shields.io/badge/VAULT-OBSIDIAN-7A3EE8?style=for-the-badge&logo=obsidian&logoColor=white" alt="Obsidian Badge"> <img src="https://img.shields.io/badge/ENVIRONMENT-MACOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS Badge"> </p> 

> [!NOTE] 
> This module serves as the central **Map of Content (MOC)** for Git version control mechanisms, terminal workflows, branch management, and GitHub collaboration strategies. 
> 
> 
> --- 
> 


## 📚 Core Modules 

1. **[01 - Introduction & Setup](./01%20-%20Introduction%20%26%20Setup.md)** — History of Git/GitHub, environment verification, `git init`, `git remote`, and default branch configuration. 
2. **[02 - Core Workflow](./02%20-%20Core%20Workflow.md)** — Staging area (`git add`), commit snapshots (`git commit`), status checking (`git status`), and pushing to remote (`git push`).
3. **[03 - Collaboration & Branching](./03%20-%20Collaboration%20%26%20Branching.md)** — Repository cloning, access permissions, forking, branch management (`git branch`, `git switch`), and synchronizing changes (`git pull`).
4. **[04 - Advanced Workflow & PRs](./04%20-%20Advanced%20Workflow%20%26%20PRs.md)** — Merging branches (`git merge`), resolving merge conflicts, Pull Request (PR) lifecycle, code review checklists, and open-source contribution workflow.


## 🗺️ Architecture & Workflow Overview 
> 

```mermaid
flowchart LR
    subgraph Local Environment
        WD[Working Directory] -->|git add| SA[Staging Area]
        SA -->|git commit| LR[Local Repository]
    end
    subgraph Remote Platform
        LR -->|git push| RR[Remote Repository - GitHub]
        RR -->|git fetch / pull| WD
    end
```