# introduction to git

The purpose of `git` (and VCS generally) is to track changes so that
one can more easily manange their own projects and collaborate with
others. Version control means we can keep track of who does what in a
project, and revert files to previous forms (this is super useful in
software development, where minor changes in code can break an entire
app!).

## Step 1: Make sure you have Git installed on you machine.

To use git, you need to first install the software. [Read here to
install
Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Step 2: Set up your account on Github (you likely already did this)

You need to set up an account on github, following the steps in the
previous lesson.

## Step 3: Configure user info via Command Line

Then, you need to configure your user information locally. Copy and
paste the following into your terminal or command line application 

```console
git config --global user.name "YOUR_USERNAME"
git config --global user.email "im_satoshi@musk.com"
```