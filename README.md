# ACM Git Walkthrough

One Python file for practicing Git. Change the greeting or add your name.

## Start

Fork this repo on GitHub, then clone **your fork**. Replace `YOUR-USERNAME`:

```bash
git clone https://github.com/YOUR-USERNAME/ACMGitWalkthrough.git
cd ACMGitWalkthrough
python app.py
```

Use `python3` if needed.

## Make a commit

Add your name to `members` in `app.py`, save it, then:

```bash
git diff
git add app.py
git commit -m "Add my name"
git push
```

## Make a merge conflict

Start with your changes committed. Run each step after making the indicated edit.

1. Run `git switch main`, then `git switch -c greeting-a`.
2. Change the first line to `message = "Hi, ACM!"` and save.
   Run `git add app.py`, then `git commit -m "Use Hi"`.
3. Run `git switch main`, then `git switch -c greeting-b`.
4. Change the first line to `message = "Welcome, ACM!"` and save.
   Run `git add app.py`, then `git commit -m "Use Welcome"`.
5. Run `git merge greeting-a`. Both branches changed the same line differently,
   so Git asks you to resolve a conflict.
6. Open `app.py`. Keep one greeting and remove the conflict markers
   (`<<<<<<<`, `=======`, and `>>>>>>>`) and the unwanted greeting.
7. Run `python app.py`, then `git add app.py` and
   `git commit -m "Resolve greeting conflict"`.

The merged result is on `greeting-b`. To cancel an unresolved merge instead,
run `git merge --abort`. Use new branch names if you repeat the exercise.
