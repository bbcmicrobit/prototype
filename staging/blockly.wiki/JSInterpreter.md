**[Installation](Installation): [Language Generators](LanguageGenerators): JavaScript Interpreter**

## Eval is Evil

The quickest way to run your user's blocks is to generate JavaScript, then push the resulting code through the browser's ` eval() ` function.  This works very well for many simple applications.  The [Language Generators](LanguageGenerators) page describes how to do this, along with a couple of hacks such as how to deal with infinite loops and how not to collide with existing variables.

However, if you are serious about running the user's blocks properly, then the [JS Interpreter](https://github.com/NeilFraser/JS-Interpreter) is the way to go.  This project is separate from Blockly, but was specifically written for Blockly.

  * Execute code at any speed.
  * Pause/resume/step-through execution.
  * Highlight blocks as they execute.
  * Completely isolated from browser's JS.

## Run the Interpreter

First, download the JS Interpreter from GitHub and add it to your page:

```
  <script type="text/javascript" src="acorn_interpreter.js"></script>
```

The simplest method of calling it is to generate the JavaScript, create the interpreter, and run the code:

```
var code = Blockly.JavaScript.workspaceToCode();
var myInterpreter = new Interpreter(code);
myInterpreter.run();
```

## Step the Interpreter

In order to execute the code slower, or in a more controlled manner, replace the call to ` run ` with a loop that steps (in this case one step every 10ms):

```
function nextStep() {
  if (myInterpreter.step()) {
    window.setTimeout(nextStep, 10);
  }
}
nextStep();
```

Note that each step is not a line or a block, it is a semantic unit in JavaScript, which may be extremely fine-grained.

## Add an API

The JS Interpreter is a sandbox that is completely isolated from the browser.  Any blocks that perform actions with the outside world require an API added to the interpreter.  For a full description, see the documentation for the JS Interpreter.  But to start with, here is the API needed to support the alert and prompt blocks:

```
function initApi(interpreter, scope) {
  // Add an API function for the alert() block.
  var wrapper = function(text) {
    text = text ? text.toString() : '';
    return interpreter.createPrimitive(alert(text));
  };
  interpreter.setProperty(scope, 'alert',
      interpreter.createNativeFunction(wrapper));

  // Add an API function for the prompt() block.
  wrapper = function(text) {
    text = text ? text.toString() : '';
    return interpreter.createPrimitive(prompt(text));
  };
  interpreter.setProperty(scope, 'prompt',
      interpreter.createNativeFunction(wrapper));
}
```

Then modify your interpreter initialization to pass in the initApi function:

```
var myInterpreter = new Interpreter(code, initApi);
```

The alert and prompt blocks are the only two blocks in the default set of blocks that require a custom API for the interpreter.

## Highlight Blocks

Some applications that use Blockly will want to highlight the currently executing block as the code runs.  This may be done on a statement-by-statement level by setting ` STATEMENT_PREFIX ` prior to generating the JavaScript code:

```
Blockly.JavaScript.STATEMENT_PREFIX = 'highlightBlock(%1);\n';
Blockly.JavaScript.addReservedWords('highlightBlock');
```

This results in the statement ` highlight('123'); ` being added to before every statement, where ` 123 ` is the serial number of the block to be highlighted.  Then create the API for the highlighting function:

```
function initApi(interpreter, scope) {
  // Add an API function for highlighting blocks.
  var wrapper = function(id) {
    id = id ? id.toString() : '';
    return interpreter.createPrimitive(Blockly.mainWorkspace.highlightBlock(id));
  };
  interpreter.setProperty(scope, 'highlightBlock',
      interpreter.createNativeFunction(wrapper));
}
```

More sophisticated applications might wish to repeatedly execute steps without pause until a highlight command is reached, then pause.  This strategy simulates line-by-line execution.  The example below uses this approach.

## Example

Here is [a live demo](https://blockly-demo.appspot.com/static/demos/interpreter/index.html) of interpreting JavaScript step by step.