# Git Commands
To-do:  
   _Should probably learn about secrets and include that_
## Index:  
1. [Introdction](#Introduction)
2. [Git Setup and Token Setup](#Git-Setup-and-Token-Setup)
   1. [Token Creation](#Token-Creation)
   2. [Token Applicaton](#Token-Application)
3. [Common Commands](#Common-Commands)
   1. [Check Connection](#Check-Connection)
   2. [Clone](#Clone)
   3. [Push](#Push)
   4. [Pull](#Pull)
   5. [Checkout](#Checkout)

## Introduction
***Git is NOT GitHub!***  
Git is a package which manages tracking changes in source code during software development.  
It is a disitrubuted Version Control System (VCS) Meaning you can have a complete copy of the project history on a local machine. It also runs syncing between local and remote repositories.

Local repos might be a local file directory, remote repositories might be hosted on services like GitHub, GitLab or Bitbucket. 

## Repositories
Git creates snapshots of work periodically, the place where these snapshots are kept are the repository.The repository is generally created within the folder where the project files are kept. 

### Git init
**Initialising a git repo:**  
*A general workflow will look like:*
```bash
cd /home/repos          # navigate to wherever you keep projects 
mkdir project_folder    # make a new folder for a specific project
cd project_folder       # navigate INTO the new folder
git init                # make it a git repo - this needs to be at the
                        # top level within the project folder
```
this will create the `.git` folder; this hidden folder represents the Git repository. It stores all metadata relating to the project, including all commits, project history, configuration files etc. It also stores any specific Git configuration and settings that might be enabled for the particular project.  

**Deleting a git repo:**  
Deleting the `.git` folder will make the folder no longer a repository, and all history of the repository will be removed, however the working files will not be harmed.

**reinitialising a git repo:**  
Running `git init` again will re-initialize the repo, but will not harm anything.
The primary reason reinitialising  a repo is to pick up newly added templates (or to move the repository to another place if `--separate-git-dir` is given).  

*'Picking up newly-added templates' means that any templates which have not already been copied from the template directory will now be copied into the existing git directory.*

*'Moving the repository to another place' means that, if `--separate-git-dir` points to somewhere else, the existing `.git` directory will be moved there and replaced by a link.*

### Git configuration
Git should be configured to know who the user is so that changes can be properly attributed. This is typically only run once.  
Basic information should include username and e-mail:
```bash
git config --global user.name "Seraphania"
git config --global user.email "strings333@hotmail.com"
```
To Check the current global configurations use:
```bash
git config --global --list
```

### Git add and commit
The `git add` command adds a file (or folder) to the list of things Git is tracking. it takes the argument for the file (or folder name).

The `git commit` command creates a **commit object** for whatever changes were made to whatever has been added. it takes the `-m` flag and requires a commit message.  
*A general workflow will look like:*
```bash
$ vi checklist.md                   # create a file (and make changes if required)
$ git add checklist.md              # add the file to git's tracking
$ mkdir subfolder                   # create a subfolder if required
$ git add subfolder/                # add the folder to the tracking
$ git commit -m "my first commit"   # commit all the changes so far (take a 
                                    # snapshot of the project.)
[master (root-commit) 25713b7] my first commit
 1 file changed, 6 insertions(+)
 create mode 100644 checklist.md
```
Git stores:
The commit object does not exactly store changes directly. Instead, Git stores changes in a different location in the Git repository and simply records (in the commit) where the changes have been stored. Along with recording where it stored the changes, the commit records a bunch of other details:  
* A pointer to the location inside the .git folder where Git has stored the changes, called a tree. This is a set of alphanumeric characters.
* The “author” info—that is, the username and email address (set up in [git config](#git-configuration))
* The time the commit was made, represented in seconds elapsed since January 1, 1970. this is the time when the commit was made, along with the time zone the machine is located in.
* The commit message supplied when `git commit -m` was invoked.

Only the added files are committed, meaning that commits can be broken up into tasks.  

    Consider a scenario where you are working on a new feature or fixing a bug. As you navigate the project you notice a typo in a documentation file and, being the good teammate that you are, you fix it. However, this fix is completely unrelated to your original task. So how do you separate the documentation fix from your original task?

    You finish the task you were working on, and you only add the files that were affected by that change to the index. And then you commit, giving it an appropriate message. Remember, Git only commits the files that were added to the index.

    Next you git add the file in which you fixed the typo and make another commit, this time providing a message that describes your fix.

If something is staged and you don't wish it to be `git reset <file>` can be used. Thsi will unstage the file. The file is optional `git reset` will unstage everything if no file is specified.

### Branching
The default branch is master (or main), but it is not special, the name can be changed.
to create a new branch the command `git branch new-branch-name` is used (the branch name can be anything). `git branch` with no arguments will list all branches, with '*' beside the current working branch.

A new branch must be switched to after creation. `git switch new-branch-name`.

`git branch -M main` renames the current branch (to main)
___
# Commands
`git init` makes the current directory into a git repository by creating the .git folder  
`git config --global user.name "Seraphania"` set global user name  
`git config --global user.email "strings333@hotmail.com"` set global e-mail address  
`git config --global --list` check git global config settings  
`git add <folder or file>` add element to the git index, staging it for a commit  
`git commit -m "commit message"` take a snapshot of all changes that have been added  
`git reset <file>` un-adds a file (file specification optional)  
`git branch new-branch-name` creats a new branch (called new-branch-name)  
`git switch new-branch-name` switches the working branch to the named branch  
`git branch` lists all current branches (with * next to the current working branch)
`git branch -M main` renames the current branch (to main)
`git switch -c my-first-branch` switches and creates the branch in one go  
