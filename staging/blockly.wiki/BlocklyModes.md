Blockly has two modes: simple and advanced.

Simple mode has a fixed toolbox with a small number of blocks, no scrollbars, and usually no trashcan:
https://blockly-demo.appspot.com/static/demos/fixed/index.html

Advanced mode has flyout toolboxes organized by category, an infinite scrolling workspace, and usually a trashcan:
https://blockly-demo.appspot.com/static/demos/toolbox/index.html

These two modes are mutually incompatible.  Consider what happens when one drags a block to the toolbox.  In one mode the block is deleted.  In the other mode the workspace grows to the left.  A scrolling workspace next to a fixed toolbox would be bad.

The determining factor for the existence of a scrolling workspace is whether there are categories in the toolbox.  See the second link, above.