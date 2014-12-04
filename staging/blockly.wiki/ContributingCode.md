# Introduction

Blockly welcomes your contributions.  Want to translate Blockly into a new language?  Want to fix a bug that's annoying you?  Want to write an application that uses Blockly?

The only rule is that all code committed by anyone must be reviewed and approved by one other contributor.

## First-time contributor

Just use Subversion to pull down a copy of Blockly's source from the repository:
```
svn checkout http://blockly.googlecode.com/svn/trunk/ blockly
```
Windows users may wish to use [Tortise SVN](http://tortoisesvn.tigris.org/).

Make your changes, then send us the resulting patch:
```
svn diff
```
Post the patch in a bug, or on the newsgroup, or email it to one of us.

If it is good, and you want to do more, we will add you as a contributor.

## As a contributor

Once you are a Blockly contributor we encourage you to [install depot\_tools](http://dev.chromium.org/developers/how-tos/install-depot-tools) that streamline the process of getting reviews done.  Then you can set up your working directory:

```
mkdir blockly
cd blockly
gclient config --name trunk https://blockly.googlecode.com/svn/trunk
gclient sync
```

First time before running 'gclient sync', you may need run the command:
```
svn ls https://blockly.googlecode.com/svn/trunk
```

and type 'p' to accept Server certificate (p)ermanently to access the https resource.

[Install Closure library](Closure).

### Update the code

```
cd blockly
gclient sync
```

### Submitting a code review

  * Do some work.
  * cd trunk
  * ` gcl change `
  * [Run tests](UnitTesting).
  * ` gcl upload xxxx `
  * Go to the url on codereview.appspot.com returned by ` gcl upload `.
  * Click on "Publish+Mail Comments", fill in the reviewer field, and send.
  * Get "LGTM" (Looks Good To Me) from reviewer.
  * ` gclient sync `
  * [Run tests](UnitTesting).
  * ` gcl commit xxxx `

### Branching

To include branches in your client, create it with:

```
gclient config --name blockly https://blockly.googlecode.com/svn
```

To merge in changes from the main branch, run the following from the subdirectory for the branch (e.g., ` branches/i18n `):

```
svn merge https://blockly.googlecode.com/svn/trunk
```
