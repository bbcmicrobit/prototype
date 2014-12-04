**[Installation](wiki/Installation): Language Generators**

# Introduction

Most applications of Blockly require the user's program to be translated into JavaScript,
Python, Dart, or some other language.  This action is performed on the client-side by Blockly.

## Generating Code

The first step is to include the generator for the language in question.
Right after ` blockly_compressed.js ` is loaded, load the generator(s) needed.
Here is the JavaScript generator:

```
  <script type="text/javascript" src="blockly/javascript_compressed.js"></script>
```

The user's blocks may be exported to code at any time from your application with this call:

```
  var code = Blockly.JavaScript.workspaceToCode();
```

Replace ` JavaScript ` with ` Python ` or ` Dart ` in all preceding lines to switch the language generated.

## Realtime Generation

Generating code is an extremely fast operation, so there's no harm in calling this function frequently.  A common strategy is to generate and display code in realtime by adding a listener to Blockly's change event:

```
  function myUpdateFunction() {
    var code = Blockly.JavaScript.workspaceToCode();
    document.getElementById('textarea').value = code;
  }
  Blockly.addChangeListener(myUpdateFunction);
```

## Running JavaScript Code

If JavaScript code is generated, it may be executed right in the browser:

```
  Blockly.JavaScript.addReservedWords('code');
  var code = Blockly.JavaScript.workspaceToCode();
  try {
    eval(code);
  } catch (e) {
    alert(e);
  }
```

Basically, the above snippet just generates the code and evals it.  However, there are a couple of refinements.
One refinement is that the eval is wrapped in a ` try `/` catch ` so that any runtime errors are visible, instead of failing quietly.
Another refinement is that ` code ` is added to the list of reserved words so that if the user's code contains a variable of that name it will be automatically renamed instead of colliding.  Any local variables should be reserved in this way.

## Infinite Loops

Although the resulting code is guaranteed to be syntactically correct at all times, it may contain infinite loops.
Since solving the [Halting problem](https://en.wikipedia.org/wiki/Halting_problem) is beyond Blockly's scope (!) the best approach for dealing with these cases is to maintain a counter and decrement it every time an iteration is performed.
To accomplish this, just set ` Blockly.JavaScript.INFINITE_LOOP_TRAP ` to a code snippet which will be inserted into every loop and every function.  Here is an example:

```
  window.LoopTrap = 1000;
  Blockly.JavaScript.INFINITE_LOOP_TRAP = 'if(--window.LoopTrap == 0) throw "Infinite loop.";\n';
  var code = Blockly.JavaScript.workspaceToCode();
```

## JS Interpreter

Instead of using ` eval() `, a completely different way to run JavaScript code is to use a [JavaScript Interpreter](wiki/JSInterpreter).  This allows for step-by-step execution at any speed.  Blocks may be highlighted as they are executed.  Infinite loops are no longer an issue.  Security is guaranteed.  The JS Interpreter is recommended for any non-trivial applications.

## Example

Here is [a live demo](https://blockly-demo.appspot.com/static/demos/generator/index.html) of generating and executing JavaScript.