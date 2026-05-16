# Git Recovery and Push Protection Fix

Date: 2026-05-16

Repository root:

```text
D:\programming
```

Final remote:

```text
https://github.com/sumitkumar-lab/Data-Structure-Algorithm.git
```

## Final Result

The repository is now on a single local branch:

```text
main
```

The branch is clean and tracks GitHub:

```text
main -> origin/main
```

Final pushed repair commit before this documentation file was added:

```text
8b1a6d4 Remove hard-coded OpenWeather API key
```

## Problems Found

There were four main Git problems:

1. The repository was in detached HEAD state.
2. There were multiple diverged branches: `main`, `save-current-work`, `grok_1`, and `origin/main`.
3. The first push failed because GitHub detected a hard-coded OpenWeather API key in history.
4. The remote repository had moved to a new GitHub URL.

## Step 1: Inspect The Repository

We first checked the current Git state.

```bash
git status --short --branch
```

Why:

To quickly see the active branch and whether there were modified, deleted, or untracked files.

Result showed:

```text
## HEAD (no branch)
```

That meant the repo was in detached HEAD state.

We checked the repository root:

```bash
git rev-parse --show-toplevel
```

Why:

To confirm that `D:\programming` was the Git repository root.

We listed the root directory:

```powershell
Get-ChildItem -Force
```

Why:

To confirm the workspace contained `.git` and to understand the project layout.

We checked full status:

```bash
git status
```

Why:

To see all modified, deleted, and untracked files in human-readable form.

We checked local branches:

```bash
git branch -vv
```

Why:

To see which branches existed and where HEAD was.

Initial branches included:

```text
grok_1
main
HEAD detached at 06e9002
```

We checked remotes:

```bash
git remote -v
```

Why:

To see which GitHub repository `origin` pointed to.

We checked recent history:

```bash
git log --oneline --decorate -n 8
```

Why:

To identify the detached commit.

We checked which branches contained the detached commit:

```bash
git branch -a --contains HEAD
```

Why:

To see whether the detached commit was already protected by a branch.

It was not protected by a normal branch yet.

We checked all branches and the graph:

```bash
git branch -a -vv
git log --all --oneline --decorate --graph -n 20
```

Why:

To see how `main`, `grok_1`, `origin/main`, and detached HEAD related to each other.

## Step 2: Protect Detached HEAD

A safety branch was created from the detached HEAD:

```bash
git switch -c save-current-work
```

Why:

Detached HEAD commits can become hard to recover after switching branches. Creating `save-current-work` protected the current commit and gave the work a real branch name.

Then the current changes were committed as a WIP commit:

```bash
git add -A
git commit -m "WIP: save current learning changes"
```

Why:

The working tree had many changes. A WIP commit safely preserved them before merging or rebasing.

## Step 3: Inspect Changes Before Merging

We reviewed the working tree and branch graph again:

```bash
git status --short --branch
git branch -vv
git log --graph --decorate --oneline --all --date-order
```

Why:

To confirm `save-current-work` was active and clean before touching `main`.

We checked a summary of changed files:

```bash
git diff --stat
git diff --name-status
```

Why:

To see the size and type of changes: modified files, deleted files, and untracked files.

We inspected the `master_LM/oops` folder:

```powershell
Get-ChildItem -Force master_LM\oops
```

```bash
rg --files master_LM/oops
```

Why:

To understand whether deleted files had been replaced by a folder structure.

We inspected specific diffs:

```bash
git diff -- "FAANG_for _AI/Models/classification.py"
git diff -- master_LM/context.py master_LM/foundation.py master_LM/pipeline.py
```

Why:

To understand what was inside the current learning changes.

We checked a deleted file from HEAD:

```bash
git show HEAD:master_LM/oops/oops_concept.py
```

Why:

To see whether deleting `master_LM/oops/oops_concept.py` removed meaningful content.

We listed tracked files under `master_LM/oops`:

```bash
git ls-files master_LM/oops
```

Why:

To separate tracked files from new untracked files.

## Step 4: Update main From GitHub

We fetched the latest remote state:

```bash
git fetch origin
```

Why:

To avoid merging local branches into stale `main`.

We switched to `main`:

```bash
git switch main
```

Why:

The goal was to consolidate everything into `main`.

We fast-forwarded local `main` to `origin/main`:

```bash
git merge --ff-only origin/main
```

Why:

`origin/main` had one commit that local `main` did not have. `--ff-only` kept this update simple and avoided creating an unnecessary merge commit.

## Step 5: Merge save-current-work Into main

We started the merge:

```bash
git merge --no-ff save-current-work -m "Merge save-current-work into main"
```

Why:

To bring the saved detached work into `main` while keeping a visible merge point.

This produced a conflict:

```text
CONFLICT (modify/delete): data.dvc deleted in save-current-work and modified in HEAD.
```

We inspected the conflict:

```bash
git status --short --branch
git ls-files -u
git show :1:data.dvc
git show :2:data.dvc
```

Why:

To compare the merge base and `main` versions of `data.dvc`.

Resolution:

We kept the `main` version of DVC files.

```bash
git restore --source=HEAD --staged --worktree .dvc/.gitignore .dvc/config .dvcignore data.dvc
```

Why:

`main` had active DVC metadata and a non-empty `data.dvc` pointer. Keeping it avoided breaking DVC tracking.

We inspected `.gitignore`:

```powershell
Get-Content .gitignore
```

```bash
git diff --cached -- .gitignore
```

Why:

The merge was replacing `/data` with only `venv/`, which would have dropped DVC-related ignore behavior.

We edited `.gitignore` to keep data, virtual environment, and Python cache files ignored:

```gitignore
/data
venv/
__pycache__/
*.pyc
```

Why:

To keep DVC-managed `data/` out of normal Git commits and avoid committing generated Python cache files.

We removed a generated `.pyc` from the index:

```bash
git rm --cached python_concepts/__pycache__/pydantic.cpython-312.pyc
```

Why:

`.pyc` files are generated artifacts and should not be committed.

We staged `.gitignore`:

```bash
git add .gitignore
```

Then we completed the merge:

```bash
git commit --no-edit
```

Why:

The merge message had already been provided when starting the merge.

Created commit:

```text
58aa840 Merge save-current-work into main
```

After the later history rewrite, this commit ID changed to:

```text
1858dd0 Merge save-current-work into main
```

## Step 6: Merge grok_1 Into main

We started the merge:

```bash
git merge --no-ff grok_1 -m "Merge grok_1 into main"
```

Why:

To bring the remaining local branch into `main`.

This produced a conflict:

```text
CONFLICT (modify/delete): Tree/binaryTree.py deleted in HEAD and modified in grok_1.
```

We inspected the conflict:

```bash
git status --short --branch
git ls-files -u
git show :1:Tree/binaryTree.py
git show :3:Tree/binaryTree.py
```

Why:

To compare the merge base and `grok_1` versions of the file.

Resolution:

We kept `grok_1`'s `Tree/binaryTree.py`, because the base file was empty and `grok_1` had real code.

```bash
git add Tree/binaryTree.py
```

`grok_1` also tried to add a file under `data/`:

```text
data/read.txt
```

We removed it from Git tracking:

```bash
git rm --cached data/read.txt
```

Why:

The `data/` folder is DVC-managed/ignored, so regular Git should not track `data/read.txt`.

We checked the merge state:

```bash
git status --short --branch
git diff --cached --name-status
```

Then completed the merge:

```bash
git commit --no-edit
```

Created commit:

```text
ecc7cc3 Merge grok_1 into main
```

After the later history rewrite, this commit ID changed to:

```text
0d8cc70 Merge grok_1 into main
```

## Step 7: Delete Merged Local Branches

We verified both branches were merged:

```bash
git status --short --branch
git branch --merged main
git log --graph --decorate --oneline --all --date-order -n 30
```

Why:

To make sure deleting local branch names would not lose work.

Then we deleted the merged branches:

```bash
git branch -d save-current-work grok_1
```

Why:

Both branches were already merged into `main`, so the extra branch names were no longer needed.

We verified only `main` remained locally:

```bash
git status --short --branch
git branch -a -vv
git log --graph --decorate --oneline --all --date-order -n 30
```

## Step 8: Push Attempt Failed

We tried to push:

```bash
git push -u origin main
```

Why:

To publish the consolidated local `main` to GitHub and set upstream tracking.

The push failed for two reasons:

1. The repository moved to a new GitHub URL.
2. GitHub push protection detected a hard-coded OpenWeather API key in commit history.

The blocked file was:

```text
API/weather_api.py
```

The blocked line was the OpenWeather key assignment. The actual secret is intentionally not written in this document.

## Step 9: Remove The Secret From The Current File

We inspected the file:

```powershell
Get-Content API\weather_api.py
```

Why:

To confirm the hard-coded API key was still present.

We checked file history:

```bash
git log --oneline --decorate --all -- API/weather_api.py
```

Why:

To identify which commit introduced the file containing the key.

We edited `API/weather_api.py` to use an environment variable instead of a hard-coded key:

```python
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
```

We also added a guard:

```python
if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable is required")
```

Why:

Secrets should come from environment variables, not source code.

We committed that current-file fix:

```bash
git add API/weather_api.py
git commit -m "Remove hard-coded OpenWeather API key"
```

Why:

This removed the key from the latest file contents, but GitHub still blocked the push because the key also existed in old commits.

## Step 10: Remove The Secret From Git History

We checked whether `git-filter-repo` was installed:

```bash
git filter-repo --help
```

Why:

`git-filter-repo` is the preferred tool for rewriting history safely.

Result:

```text
git: 'filter-repo' is not a git command.
```

So we used Git's built-in `filter-branch`.

First attempted command:

```bash
git filter-branch --force --tree-filter 'if [ -f "API/weather_api.py" ]; then sed -i -E "s/^OPENWEATHER_API_KEY[[:space:]]*=.*/OPENWEATHER_API_KEY = os.getenv(\"OPENWEATHER_API_KEY\")/" "API/weather_api.py"; fi' -- main
```

Why:

To rewrite every commit on `main` and replace the hard-coded key assignment.

Result:

This failed on Windows because the shell quoting was fragile:

```text
fatal: bad revision '='
```

We then created a temporary PowerShell helper script:

```powershell
$path = Join-Path (Get-Location) "API/weather_api.py"

if (Test-Path -LiteralPath $path) {
    $content = Get-Content -LiteralPath $path -Raw
    $updated = [regex]::Replace(
        $content,
        '(?m)^OPENWEATHER_API_KEY\s*=.*$',
        'OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")'
    )

    if ($updated -ne $content) {
        Set-Content -LiteralPath $path -Value $updated -NoNewline
    }
}
```

Temporary file:

```text
rewrite_weather_key.ps1
```

Then we successfully rewrote history:

```bash
git filter-branch --force --tree-filter "powershell -NoProfile -ExecutionPolicy Bypass -File D:/programming/rewrite_weather_key.ps1" -- main
```

Why:

This replaced the hard-coded key assignment in every commit that contained `API/weather_api.py`.

Afterward, the temporary script was deleted.

## Step 11: Remove Old Secret-Bearing Backup References

`git filter-branch` leaves old commits under `refs/original`.

We checked for them:

```bash
git for-each-ref refs/original --format="%(refname)"
```

Found:

```text
refs/original/refs/heads/main
```

We deleted the backup ref:

```bash
git update-ref -d refs/original/refs/heads/main
```

Why:

Otherwise the old secret-bearing commits would still be referenced locally.

We expired reflogs:

```bash
git reflog expire --expire=now --all
```

Why:

Reflogs can keep old commits reachable locally.

We pruned unreachable objects:

```bash
git gc --prune=now
```

Why:

To remove old unreachable objects that may still contain the secret.

## Step 12: Verify The Secret Was Removed From main History

We checked that no backup refs remained:

```bash
git for-each-ref refs/original --format="%(refname)"
```

We searched history for hard-coded OpenWeather assignments:

```bash
git log -G 'OPENWEATHER_API_KEY[[:space:]]*=[[:space:]]*"[[:alnum:]]' --oneline main -- API/weather_api.py
```

Why:

To verify that `main` no longer contained commits assigning the API key as a literal string.

Result:

No matching commits were returned.

We checked the cleaned graph:

```bash
git log --graph --decorate --oneline --all --date-order -n 30
```

Why:

To confirm the rewritten branch structure still looked correct.

## Step 13: Update The Moved Remote URL

GitHub reported the repository had moved.

Old remote:

```text
https://github.com/sumitrwk90/Data-Structure-Algorithm.git
```

New remote:

```text
https://github.com/sumitkumar-lab/Data-Structure-Algorithm.git
```

We updated `origin`:

```bash
git remote set-url origin https://github.com/sumitkumar-lab/Data-Structure-Algorithm.git
```

Why:

To push to the current repository location.

We fetched once more:

```bash
git fetch origin
```

Why:

To refresh `origin/main` before using `--force-with-lease`.

We verified the remote and state:

```bash
git remote -v
git status --short --branch
git rev-parse origin/main
```

Why:

To confirm we were pushing to the correct repository and had a fresh view of `origin/main`.

## Step 14: Push Cleaned History

Because history was rewritten, a normal push would not be a fast-forward push.

We pushed with `--force-with-lease`:

```bash
git push --force-with-lease -u origin main
```

Why:

`--force-with-lease` is safer than plain `--force`. It only overwrites the remote if the remote is still at the commit we last fetched.

Result:

```text
branch 'main' set up to track 'origin/main'.
main -> main (forced update)
```

## Step 15: Final Verification

We checked final status:

```bash
git status --short --branch
```

Result:

```text
## main...origin/main
```

We checked branch tracking:

```bash
git branch -vv
```

Result:

```text
* main 8b1a6d4 [origin/main] Remove hard-coded OpenWeather API key
```

## Important Security Note

The OpenWeather API key was exposed in Git history before GitHub blocked the push.

Even though the repository history was cleaned and pushed successfully, the key should be revoked or rotated in the OpenWeather account.

## Best Practices Used

1. Created a branch before leaving detached HEAD.
2. Made a WIP commit before merging.
3. Merged branches into `main` only after confirming the working tree was clean.
4. Resolved DVC conflicts by keeping DVC metadata intact.
5. Kept generated `.pyc` files out of Git.
6. Kept `data/` out of regular Git tracking because it is DVC-managed.
7. Removed the API key from both current files and old commits.
8. Used `--force-with-lease` instead of plain `--force`.
9. Updated the moved GitHub remote URL before pushing.
10. Verified final status and branch tracking after the push.

## Step 16: Add This Documentation File

This documentation file was created in the repository root:

```text
GIT_RECOVERY_AND_PUSH_FIX.md
```

Commands to add it to Git:

```bash
git add GIT_RECOVERY_AND_PUSH_FIX.md
git commit -m "Document Git recovery and push fix"
git push
```

Why:

To keep the full troubleshooting and repair record inside the project history.
