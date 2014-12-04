**[Installation](Installation): Defining the Toolbox**

# Introduction

The toolbox is the side menu from whence the user may create new blocks.
The structure of the toolbox is specified with XML, which may be either a tree
of nodes, or a string representation.  This XML is passed to Blockly when it is
injected into the page.

Here is a minimal example, using a tree of nodes:

```
  <xml id="toolbox" style="display: none">
    <block type="controls_if"></block>
    <block type="controls_whileUntil"></block>
  </xml>
  <script type="text/javascript">
    Blockly.inject(document.getElementById('blocklyDiv'),
        {path: './', toolbox: document.getElementById('toolbox')});
  </script>
```

Here is the same example, using a string representation:

```
  <script type="text/javascript">
    var toolbox = '<xml>';
    toolbox += '  <block type="controls_if"></block>';
    toolbox += '  <block type="controls_whileUntil"></block>';
    toolbox += '</xml>';
    Blockly.inject(document.getElementById('blocklyDiv'),
        {path: './', toolbox: toolbox});
  </script>
```

## No Categories

If there are a small number of blocks, then they may be displayed without any
categories.  In this mode all the available blocks are shown in the toolbox,
there are no scrollbars on the main workspace, and the trashcan is not needed.


## Categories

The blocks in the toolbox may be organized in categories.  Here are two
categories ('Control' and 'Logic'), each of which contain three blocks:

```
  <xml id="toolbox" style="display: none">
    <category name="Control">
      <block type="controls_if"></block>
      <block type="controls_whileUntil"></block>
    </category>
    <category name="Logic">
      <block type="logic_compare"></block>
      <block type="logic_operation"></block>
      <block type="logic_boolean"></block>
    </category>
  </xml>
```

There are two categories that have special behaviours.  Variable and procedure
categories are defined with no contents, but with a ` 'custom' ` property of
` 'VARIABLE' ` or ` 'PROCEDURE' ` respectively.  These categories will be populated
automatically with the appropriate blocks.

```
  <category name="Variables" custom="VARIABLE"></category>
  <category name="Functions" custom="PROCEDURE"></category>
```

## Tree of Categories

Categories may be nested within other categories.  Here are two top-level
categories ('Core' and 'Custom'), each of which contain two sub-categories,
each of which contain blocks:

```
  <xml id="toolbox" style="display: none">
    <category name="Core">
      <category name="Control">
        <block type="controls_if"></block>
        <block type="controls_whileUntil"></block>
      </category>
      <category name="Logic">
        <block type="logic_compare"></block>
        <block type="logic_operation"></block>
        <block type="logic_boolean"></block>
      </category>
    </category>
    <category name="Custom">
      <block type="start"></block>
      <category name="Move">
        <block type="move_forward"></block>
        <block type="move_backward"></block>
      </category>
      <category name="Turn">
        <block type="turn_left"></block>
        <block type="turn_right"></block>
      </category>
    </category>
  </xml>
```

Note that it is possible for a category to contain both sub-categories and blocks.
In the above example, 'Custom' has two sub-categories ('Move' and 'Turn'), as well
as a block of its own ('start').

## Block Groups

The XML may contain groups of blocks, or customized blocks.  Here are three blocks:
  1. A simple ` logic_boolean ` block.
  1. A ` math_number ` block that has been modified to display the number 42 instead of the default of 0.
  1. A ` controls_for ` block that has two ` math_number ` blocks that appear connected to it.

```
  <xml id="toolbox" style="display: none">
    <category name="Blocks">
      <block type="logic_boolean"></block>
      <block type="math_number">
        <field name="NUM">42</field>
      </block>
      <block type="controls_for">
        <value name="FROM">
          <block type="math_number">
            <field name="NUM">1</field>
          </block>
        </value>
        <value name="TO">
          <block type="math_number">
            <field name="NUM">10</field>
          </block>
        </value>
      </block>
    </category>
  </xml>
```

The XML for these groups or customized blocks is the same as Blockly's XML save format.
Thus, the easiest way to construct the XML for such blocks is to use the
[Code application](https://blockly-demo.appspot.com/static/apps/code/en.html) to
build the blocks, then switch to the XML tab and copy the result.

## Changing the Toolbox

The application may change the blocks available in the toolbox at any time with a single function call:
```
  Blockly.updateToolbox(newTree);
```

As was the case during initial configuration, ` newTree ` may either be a tree of nodes, or a string representation.  The only restriction is that the mode cannot be changed; that is if there were categories in the initially-defined toolbox then the new toolbox must also have categories (though the categories may change).  Likewise, if the initially-defined toolbox did not have any categories, then the new toolbox may not have any categories.

Be aware that at this time updating the toolbar causes some minor UI resets:
  * In a toolbox with categories, the flyout will close if it was open.
  * In a toolbox without categories, any fields changed by the user (such as a dropdown) will revert to the default.
  * Any toolbox so long that it extends beyond the page will have its scrollbar jump to the top.

Here is [a live demo](https://blockly-demo.appspot.com/static/demos/toolbox/index.html) of a tree with categories and block groups.