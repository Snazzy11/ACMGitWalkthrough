# ACM Git Walkthrough

A small Python noticeboard for practicing Git. Fork it, change it, break it,
and practice fixing it. No packages or database setup required.

The events and members are fictional workshop data.

## Get started

You need Git, Python 3.8 or newer, and a GitHub account.

1. Click **Fork** on this repository's GitHub page.
2. Open your fork, click **Code**, and copy its clone URL.
3. Replace `YOUR-USERNAME` below with the owner of your fork:

```bash
git clone https://github.com/YOUR-USERNAME/ACMGitWalkthrough.git
cd ACMGitWalkthrough
python app.py
```

Use `python3` if that is your system's Python command.

Configure your commit identity if you haven't already:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

These settings identify your commits. Authentication to GitHub is separate;
use your Git credential manager or `gh auth login` if GitHub CLI is installed.

## The code

- `app.py`: prints the greeting, event list, available seats, and members.
- `club_data.py`: contains the event and member data you can edit.

## Exercise 1: Your first contribution

Create a branch:

```bash
git switch -c add-my-name
```

Add your name to `MEMBERS` in `club_data.py`, then run the app and review your work:

```bash
python app.py
git status
git diff
git add club_data.py
git diff --staged
git commit -m "Add my name to the member list"
git push -u origin add-my-name
```

Open a pull request on GitHub. Set the **base repository to your fork** and
the **base branch to `main`**. Check this explicitly: GitHub may offer the
instructor's repository as the destination.

A normal commit records staged changes. If you edit a file after staging it,
run `git add` again to include those newer edits.

## Exercise 2: Pick a small feature

Merge your first pull request, then start a fresh branch:

```bash
git switch main
git pull --ff-only
git switch -c improve-noticeboard
```

Choose one task:

- Add a new event.
- Display `FULL` when an event has no seats remaining.
- Display the total number of club members.
- List members alphabetically without changing the stored list.
- Add a description to each event and display it.

Run `python app.py`, inspect the diff, commit your change, push your branch,
and open a pull request. Have a partner review it.

## Exercise 3: Create a merge conflict

This exercise uses two branches in your existing clone. Start with a clean
working directory (`git status`), then:

```bash
git switch main
git pull --ff-only
git switch -c greeting-friendly
```

In `app.py`, replace the `WELCOME_MESSAGE` assignment with:

```python
WELCOME_MESSAGE = "Welcome, ACM friends!"
```

Save and commit:

```bash
git add app.py
git commit -m "Make the greeting friendly"
git switch main
git switch -c greeting-formal
```

You are back at the same starting point. Change that same assignment to:

```python
WELCOME_MESSAGE = "Welcome to the ACM chapter meeting."
```

Save, commit, and merge:

```bash
git add app.py
git commit -m "Make the greeting formal"
git merge greeting-friendly
```

Git should report a conflict in `app.py`. Open it and find the greeting
versions separated by `<<<<<<< HEAD`, `=======`, and `>>>>>>> greeting-friendly`.

The first version comes from your current branch (`greeting-formal`); the
second comes from `greeting-friendly`. Replace the entire block, including
the markers, with a greeting that combines both intentions:

```python
WELCOME_MESSAGE = "Welcome to the ACM chapter meeting, friends!"
```

Finish the merge:

```bash
python app.py
git add app.py
git diff --staged
git commit -m "Combine the friendly and formal greetings"
git log --oneline --graph --decorate --all
```

The result is on `greeting-formal`; `main` has not moved. You can push this
branch and open a pull request into your fork's `main`.

To cancel an unresolved merge instead, run `git merge --abort`.

**Does changing the same file always cause a conflict?** No. Git can usually
combine edits to different parts of a file. Try another pair of branches
where one changes the greeting and the other changes the `Club members`
heading. Use `git merge --no-edit OTHER-BRANCH` to combine them.

If you repeat an exercise, use fresh branch names.

## Exercise 4: Undo a mistake

After completing or aborting any merge, check that `git status` is clean:

```bash
git switch -c practice-revert
```

Change the greeting to an intentionally incorrect message and save it:

```bash
git add app.py
git commit -m "Introduce a wrong greeting for recovery practice"
git revert --no-edit HEAD
python app.py
git log --oneline -3
```

The previous greeting should return. Both the mistaken commit and the new
commit undoing it remain in history.

To practice unstaging, make another temporary edit and run:

```bash
git add app.py
git restore --staged app.py
git diff
```

Your edit is still in the file, but it is no longer staged. To discard that
temporary unstaged edit, use `git restore app.py`. That command discards
unstaged changes in this file, so inspect them first.

## Working in pairs

Use one fork per pair. Its owner invites their partner as a collaborator,
and both students clone that fork. Work on separate branches and review each
other's pull requests. For a shared conflict exercise, both change the
greeting from the same starting commit, merge one pull request first, then
have the other student run `git fetch origin` and `git merge origin/main`
on their feature branch before resolving the conflict.
