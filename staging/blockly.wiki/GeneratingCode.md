**[Creating Custom Blocks](CustomBlocks): Generating Code**

# Generating Code

First, go to the ` generators/ ` directory and choose the subdirectory that corresponds to the language you want to generate (JavaScript, Python, Dart, etc).

Assuming your block(s) don't fit in the existing categories, create a new JavaScript file.  This new JavaScript file needs to be included in the list of ` <script ...> ` tags in the editor's HTML file.

A typical block's code generator looks like this:
```
Blockly.JavaScript['text_indexOf'] = function(block) {
  // Search the text for a substring.
  var operator = block.getFieldValue('END') == 'FIRST' ? 'indexOf' : 'lastIndexOf';
  var argument0 = Blockly.JavaScript.valueToCode(block, 'FIND',
      Blockly.JavaScript.ORDER_NONE) || '\'\'';
  var argument1 = Blockly.JavaScript.valueToCode(block, 'VALUE',
      Blockly.JavaScript.ORDER_MEMBER) || '\'\'';
  var code = argument1 + '.' + operator + '(' + argument0 + ') + 1';
  return [code, Blockly.JavaScript.ORDER_MEMBER];
};
```

## Collecting the Arguments

The first task for any block's code generator is to collect all the arguments and field data.  There are several functions commonly used for this task:

  * [getFieldValue](#getFieldValue)
  * [valueToCode](#valueToCode)
  * [statementToCode](#statementToCode)

### getFieldValue

```
  block.getFieldValue('END')
```

This function returns the value from a field of the specified name.

  * In the case of a text field, this function returns the typed text.  E.g. "Hello World".

  * In the case of a dropdown, this function returns the language-neutral text associated with the selected option.  An English block might have a dropdown with the word "first" selected, whereas the same dropdown in German would display "erste".  Code generators should not have to know all possible human languages, thus the ` getFieldValue ` function will return the language-neutral text that was specified when the dropdown was created.

  * In the case of a variable dropdown, this function returns the user-facing name of a variable dropdown.  It is important to note that this name is not necessarily the same as the variable name used in the generated code.  For example, a variable name of "` for `" is legal in Blockly, but would collide with a reserved word in most languages and thus would be renamed to "` for2 `".  Likewise, an Arabic variable name of "