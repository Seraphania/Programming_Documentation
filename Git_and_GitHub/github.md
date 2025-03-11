Common activities include: 
- Pull Request (PR): 
  - In Git-based collaboration workflows, a pull request is a way to propose changes to a repository. It allows others to review, discuss, and suggest modifications before merging the changes into the main codebase.
- Clone:
  - To clone a repository means to create a copy of it on your local machine. This is usually the first step when you start working on a project.
- Push and Pull:
  - Pushing means uploading your local changes to a remote repository, and pulling means downloading changes from a remote repository to your local machine.
- Merge:
  - Merging combines changes from different branches into one. For example, you might merge a feature branch into the main branch after completing a new feature.
- Conflict:
  - Conflicts occur when Git cannot automatically merge changes from different branches. Resolving conflicts requires manual intervention.
- Remote:
  - A remote is a version of your project stored on another machine. You can have multiple remotes, such as origin (default name for the remote where you cloned the repository) or other contributors' repositories.

Here's a basic workflow:
+ Clone a repository: `git clone <repository_url>`
+ Create a branch: `git branch <branch_name>` and switch to it: `git checkout <branch_name>` or in one step: `git checkout -b <branch_name>`
+ Make changes and commit them: `git add <file(s)>` and git `commit -m "Your commit message"`
+ Push changes to a remote repository: `git push origin <branch_name>`
+ Create a pull request on the hosting service (GitHub, GitLab, etc.) Review, discuss, and merge the pull request


## Git Setup and Token Setup
### Token Creation
1. Log into Github.com in a browser.
2. Click on profile (top right).
3. Go to "< > Developer settings" - bottom of the left hand menu.
4. Under "Personal access tokens" select "Fine-grained tokens"
5. Select the permissions required and generate the token. - It will look horrid!
6. Copy the token for later use.
   
### Token Applicaton
Configure git to use store  as the credential helper.  
`git config --global credential.helper store`  
Add the token to the credeentials:
`echo "https://<username>:<your_token>@github.com" > ~/.git-credentials`  
replace "<username>" with the username (Seraphnaia), and "<your token>" with the token generated. This can also be done by editing `~/.git-credentials` in a text editor.

## Common Commands
### Check Connection
To display the URLs of the remote repositories that your local repository is linked to for both fetching and pushing:  
`git remote -v`

### Clone
Move to the directory where you want the repo to sit - in my case '/git'.  
`git clone https://github.com/Seraphania/Arch`  
This will copy the "Arch" repository to '/git/Arch'.  

### Push
1. After making local changes, navigate to the forlder where the repo is held ('~/git/Arch') and add the files (rounds them up for pushing):  
`git add .`  
2. Commit the changes with a note about the changes made:  
`git commit -m "Commit message here"`  
3. Push the changes - upload them to the repository:  
`git push origin main`  
Main can be replaced with a branch name if it's different.
Push Notes:
- Specific files files can be pushed if required; it doesn't matter too much for small projects, but it can mean more spcific commit messages which might be nice; use:  
`git add /path/to/file.md`
paths should be relative to the pwd.  
- Github can render some formats based on their extensions including syntax highlighting;
  - .md for markdown,
  - .py for python code,
  - .sh for bash scripts etc.  

### Pull
Pull requests are used for creating branches, which is proposing changes rather than replacing the main repo. Mostly used for collaboration.
1. Create a new branch:  
`git checkout -b feature-branch`  
2. Make the chages and commit (as above).  
3. Push the branch to the fork:  
`git push origin feature-branch`  
This means it can be used to replace the files of a single directory, for example to update this file locally with the last on submitted on github:  
`git pull origin main`  
* I Probably need to learn a bit more about branches!

### Checkout
git checkout is used to switch your working directory to the specified branch. It updates the files in your working directory to match the branch's latest commit.  
`git checkout branch-name`
Restoring Files:  
This command restores the specified file in your working directory to its state in the latest commit of the current branch. Useful for discarding changes in a file.  
`git checkout -- path/to/file`
Checking Out Specific Commits or Tags:  
This command checks out a specific commit by its hash. The working directory will reflect the state of the repository at that commit. Note that this will put you in a "detached HEAD" state.  
`git checkout commit-hash`
Creating and Switching to a New Branch:  
This command creates a new branch and switches to it immediately.  
`git checkout -b new-branch-name`

For newer Git versions (2.23+), it's recommended to use git switch for switching branches and git restore for discarding changes, as they provide a more intuitive and focused interface:

    Switch branches: git switch branch-name
    Discard changes: git restore path/to/file

___
#From GPT
# GitHub Usage Guide
## Index
- [GitHub Usage Guide](#github-usage-guide)
  - [Index](#index)
  - [Introduction](#introduction)
  - [Setting up Git](#setting-up-git)
    - [Configuring Git](#configuring-git)
  - [Git Operations](#git-operations)
    - [Cloning Repositories](#cloning-repositories)
    - [Committing Changes](#committing-changes)
    - [Pushing Changes](#pushing-changes)
    - [Pulling Changes](#pulling-changes)
    - [Branching](#branching)
    - [Merging](#merging)
    - [VS Code Git Integration](#vs-code-git-integration)
    - [View Commit History](#view-commit-history)
    - [Collaboration with Pull Requests](#collaboration-with-pull-requests)
    - [Creating Pull Requests from VS Code](#creating-pull-requests-from-vs-code)

## Introduction
GitHub is a platform for version control and collaboration, allowing developers to work on projects together. This guide will explain the basics of using Git with GitHub, from setting up repositories to using Git operations in both the command line and Visual Studio Code.

## Setting up Git
Before using Git, make sure Git is installed on the system. Install it by following the instructions on the [official Git website](https://git-scm.com/).

### Configuring Git
Set up the global username and email for commits:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
## Git Operations
### Cloning Repositories

To clone a repository from GitHub:

    Copy the repository URL from the GitHub page.
    Open a terminal and run:

git clone https://github.com/username/repository.git

In VS Code:

    Open the Source Control panel (Ctrl+Shift+G), click Clone Repository, and paste the URL to clone.

### Committing Changes

To commit your changes:

    Stage the changes:

git add .

    Commit with a message:

git commit -m "Your commit message"

In VS Code:

    Make changes to your files.
    Go to the Source Control panel, enter a commit message, and click the checkmark icon to commit.

### Pushing Changes

To push your commits to GitHub:

git push origin main

In VS Code:

    Once committed, click the ... in the Source Control panel and select Push.

### Pulling Changes

To fetch the latest changes from GitHub and merge them with your local repo:

git pull origin main

In VS Code:

    Click the ... in the Source Control panel and select Pull to get the latest changes.

### Branching

Branches allow you to work on different features independently. To create and switch to a new branch:

git checkout -b new-branch

In VS Code:

    Open the Source Control panel, click the branch name, and select Create New Branch.

### Merging

To merge changes from one branch into another:

    Switch to the branch you want to merge into:

git checkout main

    Merge the changes from the other branch:

git merge new-branch

In VS Code:

    Switch branches from the Source Control panel and use Merge options from the command palette.

### VS Code Git Integration

VS Code offers seamless Git integration. Here's how to use it:

    Open your project in VS Code.
    The Source Control panel (Ctrl+Shift+G) will automatically show the current Git status.
    You can:
        Stage changes (+ icon),
        Commit changes (enter a message and hit the checkmark),
        Push and pull changes (using the ... menu),
        Create and switch branches (via the branch menu at the bottom).

### View Commit History

To view your commit history, open the Source Control panel and click on the ... menu, then select View Git Log or use the Git History extension.


### Collaboration with Pull Requests

Pull requests are used to propose changes to a repository. You can create a pull request after pushing your branch:

    Push your branch to GitHub.
    Go to GitHub, navigate to your repository, and click New Pull Request.
    Select your branch and compare it with the base branch (usually main).
    Add a description and submit your pull request.

Once your changes are reviewed, they can be merged into the base branch by the project maintainer.


### Creating Pull Requests from VS Code

In VS Code, use the GitHub Pull Requests and Issues extension to:

    View open pull requests,
    Create new pull requests,
    Review and merge pull requests directly from the editor.

Notes on Git Terminology:

    Commit: A snapshot of changes made to your files.
    Push: Uploading your local commits to GitHub.
    Pull: Fetching the latest changes from GitHub to your local repository.
    Branch: A separate line of development.
    Merge: Combining changes from two branches.

Additional Resources

For more detailed Git and GitHub documentation, check out the Git Documentation and GitHub Docs.
