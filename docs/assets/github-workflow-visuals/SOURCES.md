# GitHub Pull Request Workflow Visuals

Openly-licensed diagrams and screenshots of the pull request / merge request workflow, for
slides about contributing fixes to course materials. Every file here is free to reuse with
attribution — nothing is scraped from a proprietary docs site.

## From GitHub Docs (`github/docs`, CC BY 4.0)

The `github/docs` repository is licensed **CC BY 4.0** for content, including these images.
Attribution: *GitHub Docs, licensed CC BY 4.0.* Source repo: <https://github.com/github/docs>

| File | What it shows | Upstream path |
| --- | --- | --- |
| `gh-docs-pr-conversation-example.png` | A merged "Fix typo" pull request — title, Merged badge, Conversation/Commits/Checks/Files changed tabs, reviewer approval, PR body | `assets/images/help/pull_requests/pr-conversation-example.png` |
| `gh-docs-pr-files-changed-example.png` | The "Files changed" diff view of a pull request | `assets/images/help/pull_requests/pr-files-changed-example.png` |
| `gh-docs-standard-merge-commit-diagram.png` | Branch/commit diagram of a standard merge commit | `assets/images/help/pull_requests/standard-merge-commit-diagram.png` |
| `gh-docs-commit-squashing-diagram.png` | Branch/commit diagram of squash-and-merge | `assets/images/help/pull_requests/commit-squashing-diagram.png` |
| `gh-docs-compare-across-forks-link.png` | The "compare across forks" link when opening a PR from a fork | `assets/images/help/pull_requests/compare-across-forks-link.png` |
| `gh-docs-repository-fork-button.png` | The repository header with the Fork button | `assets/images/contributing/repository-fork-button.png` |

## From Wikimedia Commons

| File | What it shows | Credit / license |
| --- | --- | --- |
| `git-workflow-hashar.svg` | Developer → local repo → review → central repo loop (drawn for the MediaWiki/Gerrit workflow, but the shape is generic) | Hashar, [GitWorkflow.svg](https://commons.wikimedia.org/wiki/File:GitWorkflow.svg), CC BY-SA 3.0 |
| `git-operations.svg` | The core git operations between workspace, index, local repo, and remote repo | Duesentrieb, [Git operations.svg](https://commons.wikimedia.org/wiki/File:Git_operations.svg), CC BY 3.0 |
| `git-branches-two-forks-rebase.svg` | Two forks of a branch, before and after rebase | Bunyk, [Git branches two forks rebase.svg](https://commons.wikimedia.org/wiki/File:Git_branches_two_forks_rebase.svg), CC BY-SA 4.0 |
| `oneflow-example.png` | The OneFlow branching model (feature branch off main and back) | Qeef, [OneFlow Example.png](https://commons.wikimedia.org/wiki/File:OneFlow_Example.png), CC BY-SA 4.0 |
| `gitlab-merge-request.png` | GitLab's merge request UI — the same workflow under a different name | GitLab, Inc., [GitLab Merge Request.png](https://commons.wikimedia.org/wiki/File:GitLab_Merge_Request.png), MIT |
| `octicons-git-pull-request.svg` | The pull request icon itself | GitHub, [Octicons-git-pull-request.svg](https://commons.wikimedia.org/wiki/File:Octicons-git-pull-request.svg), MIT |

## In use

- `week1.qmd`, "help improve the class!" — `gh-docs-pr-conversation-example.png`. Chosen
  because it is a *merged typo fix*: the smallest possible contribution, accepted. It follows
  the "Things are Rarely Perfect on the First Attempt" slide, so the visual argument is that
  the fix path is short and low-stakes, not that students need to learn all of git.
