# *If* we're going to create syntax for anonymous blocks, I think the
# primary use case ought to be cleanup operations to replace try/finally
# blocks for locking and similar things. I'd love to have syntactical
# support so I can write

blahblah(myLock):
     code
     code
     code
