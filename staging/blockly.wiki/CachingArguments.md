**[Creating Custom Blocks](CustomBlocks): [Generating Code](GeneratingCode): Caching Arguments**

# Caching Arguments

When generating code from blocks one often finds the need to use the returned value of a sub-block more than once.  Consider a value block that finds and returns the last element of a list.  The block itself would have one input (a list), and would return a value (the last element).  Here is the generator for JavaScript:
```
  var code = arg0 + '[' + arg0 + '.length - 1]';
```
If ` arg0 ` is a variable name, this generator returns perfectly acceptable JavaScript:
```
  aList[aList.length - 1]
```
However, this generator may have unintended behaviour if ` arg0 ` were a function call.  Consider the following code:
```
  randomList()[randomList().length - 1]
```
The two returned values might be of different lengths, resulting in an out of range condition.  Additionally, if the function call has side-effects, then calling it twice could be undesirable.

There are two solutions to this problem.  Statement blocks should use temporary variables.  Value blocks should use utility functions.

## Temporary Variables

The simplest solution is to assign the offending input to a temporary variable.  Care must be taken that this variable does not accidentally collide with an existing variable.  The following code shows an example of a temporary variable in a statement block which alerts the last element of a list.
```
  var listVar = Blockly.JavaScript.variableDB_.getDistinctName(
      'temp_list', Blockly.Variables.NAME_TYPE);
  var code = 'var ' + listVar + ' = ' + arg0 + ';\n';
  code += 'alert(' + listVar + '[' + listVar + '.length - 1]);\n';
```
The ` getDistinctName ` call takes an argument of the desired variable name ("temp\_list") and will return an non-colliding name to use (possibly "temp\_list2").

The downside of temporary variables is that if the offending input was already a variable, then one generates redundant code:
```
  var temp_list = foo;
  alert(temp_list[temp_list.length - 1]);
```
To produce cleaner code, check to see if the offending input is a simple literal, and generate code accordingly:
```
if (argument0.match(/^\w+$/)) {
  var code = 'alert(' + arg0 + '[' + arg0 + '.length - 1]);\n';
} else {
  var listVar = Blockly.JavaScript.variableDB_.getDistinctName(
      'temp_list', Blockly.Variables.NAME_TYPE);
  var code = 'var ' + listVar + ' = ' + arg0 + ';\n';
  code += 'alert(' + listVar + '[' + listVar + '.length - 1]);\n';
}
```

See ` Blockly.JavaScript.controls_forEach ` for a working example of temporary variables.

Temporary variables work well in statement blocks (in this case an alert) where the generated code may span multiple lines.  However they are unworkable in value blocks which must be on a single line.  For value blocks one must use a utility function instead of temporary variables.

## Utility Functions

Defining a utility function is a powerful way to create blocks that operate at a higher level than the underlying language.  Utility functions are not generated unless they are used, and they are only generated once regardless of the number of times they are used.  The following example includes inline comments.

```
  // Only define a utility function if it hasn't already been defined.
  // The 'definitions_' property of the generator stores all the utility functions.
  if (!Blockly.JavaScript.definitions_['list_lastElement']) {
    // Obtain a non-colliding function name.
    var functionName = Blockly.JavaScript.variableDB_.getDistinctName(
        'list_lastElement', Blockly.Generator.NAME_TYPE);
    // Save this name in a place that can be accessed by all blocks of this type.
    Blockly.JavaScript.list_lastElement.utilityFunction = functionName;
    // Build the function line by line.  Ensure that the name is dynamic.
    var func = [];
    func.push('function ' + functionName + '(aList) {');
    func.push('  // Return the last element of a list.');
    func.push('  return aList[aList.length - 1];');
    func.push('}');
    // Add the completed function to the code generator.
    Blockly.JavaScript.definitions_['list_lastElement'] = func.join('\n');
  }
  // Generate the function call for this block.
  var code = Blockly.JavaScript.list_lastElement.utilityFunction + '(' + arg0 + ')';
  return [code, Blockly.JavaScript.ORDER_FUNCTION_CALL];
```

See ` Blockly.JavaScript.text_endString ` for a working example of a utility function.