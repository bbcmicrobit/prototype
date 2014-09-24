**[Installation](Installation): Injecting Fixed-sized Blockly**

# Introduction

The simplest way to put Blockly into a webpage is to inject it into an empty 'div' tag.  There are two major limitations of this approach:

  * One can't have more than one instance of Blockly on the same page.
  * Blockly cannot easily reflow as the window resizes.

Both of these issues may be solved by [injecting Blockly into an iframe](InjectingResizable).

## Injection

If neither of the above limitations are a concern, include the core Blockly script and the core blocks set.  Note that the path may vary, depending on where your page is in relation to Blockly:

```
  <script type="text/javascript" src="blockly_compressed.js"></script>
  <script type="text/javascript" src="blocks_compressed.js"></script>
```

Then include the messages for the user's language (in this case English):

```
  <script type="text/javascript" src="msg/js/en.js"></script>
```

Add an empty div to the page and set its size:

```
  <div id="blocklyDiv" style="height: 480px; width: 600px;"></div>
```

Add the structure of the toolbox (see [Defining the Toolbox](Toolbox) for more information):

```
  <xml id="toolbox" style="display: none">
    <block type="controls_if"></block>
    <block type="controls_repeat_ext"></block>
    <block type="logic_compare"></block>
    <block type="math_number"></block>
    <block type="math_arithmetic"></block>
    <block type="text"></block>
    <block type="text_print"></block>
  </xml>
```

Finally, call the following to inject Blockly into an empty div.  Set 'path' to be the relative path from your web page to Blockly's root directory.  This is used by Blockly so that media such as the trash can and the sounds may be loaded.

```
  <script type="text/javascript">
    Blockly.inject(document.getElementById('blocklyDiv'),
        {path: './', toolbox: document.getElementById('toolbox')});
  </script>
```

Test the page in a browser.  You should see Blockly's editor filling the div, with four block categories in the toolbox.  Here is [a live demo](https://blockly-demo.appspot.com/static/demos/fixed/index.html).