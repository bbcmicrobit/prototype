# Introduction

Did you just get this error message?

![](closure_alert.png)

If so, then you are probably attempting to run the uncompiled version of Blockly and you are missing the dependency on [Closure Library](https://developers.google.com/closure/library/).

## Getting Closure

Getting Closure is quick and easy.  Use either Git or Subversion to checkout a copy from [Closure's repository](https://github.com/google/closure-library):

```
svn checkout https://github.com/google/closure-library/trunk closure-library-read-only
```

Once you have the Closure files, place them next to Blocky's root directory and ensure that the directory is named ` closure-library-read-only `.  This is the directory structure you want:

![](closure_directory.png)

That's it.  Blockly should now work in uncompiled mode.
