**[Installation](wiki/Installation): Injecting Resizable Blockly**

# Introduction

The most flexible way to put Blockly into a web page is to inject it into an 'iframe'.
This is slightly more complicated than [injecting Blockly into a div](wiki/InjectingFixedSize), but using an iframe allows
Blockly to resize to fill the page, and it allows more than one instance of Blockly to exist on the page.
The only limitation of using an iframe is that for security reasons Blockly will not execute in Chrome when served directly off the local file system with the ` file:// ` protocol.

## Injection

Include the following snippet in your web page:

```
  <script>
    function blocklyLoaded(blockly) {
      // Called once Blockly is fully loaded.
      window.Blockly = blockly;
    }
  </script>
  <iframe src="frame.html"></iframe>
```

The iframe is where Blockly will appear.  It will be sized as needed using tables, CSS, or JavaScript.  The next step is to create the frame for the editor.  Here's a good starting snippet for ` frame.html `.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <script type="text/javascript" src="blockly_compressed.js"></script>
    <script type="text/javascript" src="blocks_compressed.js"></script>
    <script type="text/javascript" src="msg/js/en.js"></script>
    <style>
      html, body {
        background-color: #fff;
        margin: 0;
        padding: 0;
        overflow: hidden;
        height: 100%;
      }
      .blocklySvg {
        height: 100%;
        width: 100%;
      }
    </style>
    <script>
      function init() {
        Blockly.inject(document.body,
            {path: '../../', toolbox: document.getElementById('toolbox')});
        // Let the top-level application know that Blockly is ready.
        window.parent.blocklyLoaded(Blockly);
      }
    </script>
  </head>
  <body onload="init()">
    <xml id="toolbox" style="display: none">
      <block type="controls_if"></block>
      <block type="controls_repeat_ext"></block>
      <block type="logic_compare"></block>
      <block type="math_number"></block>
      <block type="math_arithmetic"></block>
      <block type="text"></block>
      <block type="text_print"></block>
    </xml>
  </body>
</html>
```

The script tags in the above snippet load the core Blockly script (` blockly_compressed.js `), the core blocks set (` blocks_compressed.js `), and selects the user's language to be English (` msg/js/en.js `).

Adjust the paths as needed to enable inclusion of these script files.  Likewise, the ` Blockly.inject ` line has a path that needs to point to Blockly's root directory so that media such as the trash can and the sounds may be loaded.

Test the page in a browser.  You should see Blockly's editor filling the iframe, with four block categories in the toolbox.

Here is [a live demo](https://blockly-demo.appspot.com/static/demos/iframe/index.html) of an iframe nested in a table that fills the screen.