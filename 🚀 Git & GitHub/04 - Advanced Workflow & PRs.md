
# 04. Advanced Workflow & PRs


## 1. Merging Branches & Handling Conflicts

Merging combines changes from one branch into another (e.g., bringing `main` updates into a feature branch or vice versa)[cite: 70, 71].

Bash

```bash
# Bring updates from main into your current working branch
git checkout main
git pull
git checkout <your-feature-branch>
git merge main
````


### Merge Conflicts

Occur when changes are made to the same part of a file across different branches, or when one branch deletes a file modified by another. Code editors provide options to resolve them:

- **Accept Incoming Changes:** Overwrites local changes with the branch being merged.
    
- **Accept Current Changes:** Keeps local branch changes and ignores merged changes.
    
- **Accept Both Changes:** Retains both versions of the modified code.
    

After resolving conflicts, stage and commit the merged code:

Bash

```bash
git add .
git commit -m "fix: resolve merge conflicts"
git push origin <your-feature-branch>
```


## 2. Pull Requests (PRs) & Code Review

A **Pull Request (PR)** proposes merging code from one branch/repository into another, allowing team review, discussion, and automated checks before integrating code.

### PR Checklist

1. **Pull Latest Changes:** Update local code (`git pull origin main`).
    
2. **Test:** Verify feature execution and build integrity.
    
3. **Review:** Clean up temporary code, logs, and unnecessary files.
    
4. **Resolve Conflicts:** Ensure no open merge conflicts remain.
    


## 3. Open Source Contribution Workflow

Standard process for contributing to external or team repositories:

1. **Fork** the original repository to your GitHub account.
    
2. **Clone** your fork locally: `git clone <fork-url>`.
    
3. **Create a branch** for changes: `git switch -c feature-name`.
    
4. **Commit & Push** updates to your fork.
    
5. **Open a Pull Request** against the original project's `main` branch.