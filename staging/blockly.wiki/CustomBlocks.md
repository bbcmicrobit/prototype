This document is aimed at developers who wish to create new blocks within Blockly.  It is assumed that one has a local copy of Blockly which one can edit, one is generally familiar with Blockly's usage, and one has a basic understanding of JavaScript or some similar language.

# Introduction

Blockly comes with a large number of pre-defined blocks.  Everything from mathematical functions to looping structures.  However, in order to interface with an external application, one must create custom blocks to form an API.  For example, when creating a drawing program, one might need to create a "_draw circle of radius R_" block.

In most cases the easiest approach is to just find a really similar block which already exists, copy it, and modify it as needed.  The following documentation is for those who need more help.  If all else fails, post in the [support newsgroup](https://groups.google.com/group/blockly).

## Define Block

The first step is to create a block; specifying its shape, labels, and connection points.  This is done in the ` language/ ` directory.

→ More info on [Defining Blocks](DefiningBlocks)...

Advanced blocks may dynamically change their shape in response to the user or other factors.

→ More info on [Creating Mutators](CreatingMutators)...

## Code Generation

The second step is to create the generator code to export the new block to a programming language (such as JavaScript, Python, or Dart).  This is done in the ` generators/ ` directory.

→ More info on [Generating Code](GeneratingCode)...

To generate code that is both clean and correct, one must be mindful of the order of operations list for the given language.

→ More info on [Operator Precedence](OperatorPrecedence)...

Creating more complicated blocks requires the use of temporary variables and/or utility functions.  This is particularly true when an input is used twice and needs to be cached.

→ More info on [Caching Arguments](CachingArguments)...