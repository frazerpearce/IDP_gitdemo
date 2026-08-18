# Git/GitHub circle pull-request exercise

This small repository is a worked exercise in the Git/GitHub workflow:

```text
clone -> branch -> edit and test -> commit -> push -> pull request -> review -> merge
```

The starting repository contains 20 independent Python scripts. Each script draws
a red unit circle on a white square frame whose x and y limits are both `[-2, 2]`.
Each student changes only the script matching their assigned number. Because the
files are separate, the class can work in parallel.

## What you will need

- A GitHub account and access to the class repository.
- Git installed on your computer.
- Python 3.9 or newer.
- Your assigned student number, from `01` to `20`.
- A partner who will review your pull request.

Commands below use `python3`. On Windows, use `python` instead if that is the
command provided by your installation.

## Instructor: publish this exercise to GitHub

Create a new, empty GitHub repository. Do not ask GitHub to add a README,
`.gitignore`, or licence, because those files are already present here. Then, from
this directory, run:

```bash
git init
git add .
git commit -m "Add circle pull-request exercise"
git branch -M main
git remote add origin https://github.com/ORGANISATION/REPOSITORY.git
git push -u origin main
```

Replace `ORGANISATION/REPOSITORY` with the real repository path. Give students
write access, or ask them to fork the repository if your class uses forks.

For a reliably enforced review, use GitHub's repository settings to protect the
`main` branch and require at least one approving pull-request review before a
merge. If branch protection is not available, instruct students not to merge
until their partner has submitted an approval.

## Student A: make the change

In these instructions, replace `NN` with your two-digit student number. For
example, student 7 uses `07`, the file `scripts/student_07.py`, and a branch such
as `student-07-blue-circle`.

### 1. Clone the repository

Do this once, using the URL supplied by the instructor:

```bash
git clone https://github.com/ORGANISATION/REPOSITORY.git
cd REPOSITORY
```

Check that the clone is ready:

```bash
git status
```

You should be on `main`, with a clean working tree.

### 2. Create your own branch

First obtain the latest accepted changes, then create a branch:

```bash
git switch main
git pull
git switch -c student-NN-blue-circle
```

Do not make this exercise's change directly on `main`.

### 3. Create a Python environment and install the dependency

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The `.venv` directory and generated PNG images are ignored by Git.

### 4. Run your starting script

Student `NN` runs:

```bash
python3 scripts/student_NN.py
```

The script writes `student_NN_circle.png` in the current directory. Open it and
confirm that it shows a **red unit circle** on a **white square frame**, with both
axes running from `-2` to `2`.

### 5. Make the assigned change

Open only `scripts/student_NN.py` in an editor. Find:

```python
CIRCLE_COLOR = "red"
```

Change it to:

```python
CIRCLE_COLOR = "blue"
```

Do not edit another student's numbered script.

### 6. Test and inspect the change

Run your script again:

```bash
python3 scripts/student_NN.py
```

Open the newly generated PNG and check:

- the circle is blue;
- the circle is centred at `(0, 0)` and has radius 1;
- the background is white;
- the frame is square;
- both axes span `[-2, 2]`.

Now ask Git what changed:

```bash
git status
git diff -- scripts/student_NN.py
```

The diff should contain one meaningful change: `"red"` becomes `"blue"`. The
PNG should not appear in `git status`, because generated output is not source
code and is ignored.

### 7. Commit the change

Stage only your assigned script:

```bash
git add scripts/student_NN.py
git status
git commit -m "Change student NN circle to blue"
```

Before pushing, check the short history:

```bash
git log --oneline -3
```

### 8. Push the branch

```bash
git push -u origin student-NN-blue-circle
```

If your class uses forks, `origin` should be your fork. GitHub may print a link
that opens a pull request.

### 9. Open a pull request

On GitHub, open the repository and select **Compare & pull request** (or
**Pull requests** -> **New pull request**). Set:

- base branch: `main`;
- compare branch: `student-NN-blue-circle`;
- title: `Change student NN circle to blue`.

Use this description:

```text
What changed

Changed the circle colour in scripts/student_NN.py from red to blue.

Why

This completes the numbered Git/GitHub collaboration exercise.

Tests / evidence

Ran: python3 scripts/student_NN.py
Observed a blue unit circle centred at (0, 0), on a white square frame
with x and y limits of [-2, 2].
```

Open the pull request and send its URL to your assigned reviewer. Do not merge it
yourself before it has been reviewed and approved.

## Student B: review and approve the pull request

The reviewer should be a different student. Open the pull request URL and:

1. Read the description and its **Tests / evidence** section.
2. Open **Files changed**.
3. Confirm that only the assigned file, `scripts/student_NN.py`, changed.
4. Confirm that the only intended source change is `"red"` to `"blue"`.
5. Check that the rest of the script still creates a radius-1 circle, keeps equal
   aspect ratio, uses a white background, and sets both limits to `(-2, 2)`.

Optionally, test the contributor's branch locally:

```bash
git fetch origin
git switch student-NN-blue-circle
python3 scripts/student_NN.py
```

Return to the pull request on GitHub. Select **Review changes**, choose
**Approve**, write a short note such as the following, and submit the review:

```text
Checked the diff and test evidence. The assigned circle is blue and the
unit-circle geometry and [-2, 2] white square frame are unchanged.
```

If the wrong file changed or the plot requirements are not preserved, choose
**Request changes** instead and explain exactly what needs correcting. The author
should fix the same branch, commit, and run `git push`; the existing pull request
will update automatically.

## Merge after approval

After a different student has approved the pull request, the person authorised
by the instructor selects **Merge pull request** and confirms the merge. Delete
the remote feature branch if GitHub offers to do so.

The author then updates their local copy:

```bash
git switch main
git pull
```

The completed repository now records who made the change, what changed, who
reviewed it, and when it was accepted.

## Avoiding collisions during the class

- Change only the script with your assigned number.
- Use a uniquely numbered branch name.
- Do not commit generated PNG files or `.venv`.
- Pull the latest `main` before creating a branch.
- Do not reuse somebody else's branch.
- If GitHub says the branch is behind `main`, that is usually harmless here
  because each student edits a different file; follow the instructor's merge
  policy.

## Exercise checklist

Author:

- [ ] I used my assigned numbered script.
- [ ] I worked on a numbered branch, not directly on `main`.
- [ ] I changed `red` to `blue`.
- [ ] I ran the script and inspected its PNG.
- [ ] I committed and pushed the source script only.
- [ ] My pull request includes tests/evidence.
- [ ] I asked another student to review it.

Reviewer:

- [ ] I checked the pull request's **Files changed** view.
- [ ] I checked the plot requirements were preserved.
- [ ] I submitted an approval (or clearly requested necessary changes).
- [ ] The pull request was merged only after approval.

