
# Introduction

We use the term _variable_ the same as it is used in mathematics and in other programming languages: a named value that can be changed (varies).  Variables can be created in several different ways.
  * Every [count with](Loops#count_with) and [for each](Loops#for_each) block uses a variable and defines its values.  These values can only be used within the block.  A traditional computer science term for these are [loop variables](https://en.wikipedia.org/wiki/Loop_variable).
  * User-defined functions (also known as "procedures") can define inputs, which creates variables that can be used only within the function.  These are traditionally called "[parameters](https://en.wikipedia.org/wiki/Parameter)" or "arguments".
  * Users may create variables at any time through the "set" block.  These are traditionally called "[global variables](https://en.wikipedia.org/wiki/Global_variables)".
Blockly does not support [local variables](https://en.wikipedia.org/wiki/Local_variable).


## Default names

While users can choose any name for a variable, core Blockly provides a default name, "item", as shown in the below picture.  Some applications provide other default values, such as "value", also shown below.

## Dropdown menu

Clicking on a variable's dropdown symbol (triangle) gives the following menu:

![](help/variables-dropdown.png)

The menu provides the following options.
  * the names of all variables defined in the program.
  * "Rename variable...", which changes the name of this variable wherever it appears in the program.  Selecting this opens a small window that prompts the user for the new name with the text: "Rename all %1 variables to:", where %1 is replaced by the old name (here "item").
  * "New variable...", which enables the user to enter a new name for the variable, without replacing or changing variables with the old name (here "item").  Selecting this opens a small window that prompts the user for the new name with the text "New variable name:".

# Blocks

## Set

The **set** block assigns a value to a variable, creating the variable if it doesn't already exist.  For example, this sets the value of the variable named "age" to 12.

![](help/variables-set-variable.png)

## Get

The **get** block provides the value stored in a variable, without changing it.

![](help/variables-get-variable.png)

It is possible, but a bad idea, to write a program in which a **get** appears without a corresponding **set**.

# Example

Consider the following example code:

![](help/variables-example.png)

The first row of blocks creates a variable named "age" and sets its initial value to the number 12.  The second row of blocks gets the value 12, adds 1 to it, and stores the sum (13) into the variable.  The final row displays the message: "Happy birthday!  You are now 13"
