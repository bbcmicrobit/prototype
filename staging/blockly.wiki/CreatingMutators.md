**[Creating Custom Blocks](wiki/CustomBlocks): [Defining a Block](wiki/DefiningBlocks): Creating Mutators**

# Creating Mutators

Advanced blocks may use a mutator to be even more dynamic and configurable.  Mutators allow blocks to change in custom ways, beyond dropdown and text input fields.  The most common example is the pop-up dialog which allows ` if ` statements to acquire extra ` else if ` and ` else ` clauses.  But not all mutators are so visible.

## mutationToDom and domToMutation

The XML format used to load, save, copy, and paste blocks automatically captures and restores all data stored in editable fields.  However, if the block contains additional information, this information will be lost when the block is saved and reloaded.

A simple example of this is the ` Blockly.Language.text_trim ` block.  This block normally reads "` trim spaces from [both] sides `" where ` [both] ` is a dropdown with options ` both `, ` left `, and ` right `.  The latter two options result in a grammatical error, requiring the word ` sides ` to become ` side `.  This is easy to accomplish, one just adds a validation function on the dropdown which changes the text field.  When the dropdown is changed, so is the field.  However, since the field is not editable, it is not saved or restored when converted to and from XML.  To store this extra information, a mutation is stored.

Saving mutation data is accomplished by adding a ` mutationToDom ` function in the block's definition.  Here is the example from the aforementioned ` text_trim ` block:
```
  mutationToDom: function() {
    // Save whether the 'sides' field should be plural or singular.
    var container = document.createElement('mutation');
    var plural = (this.getFieldValue('MODE') == 'BOTH');
    container.setAttribute('plural', plural);
    return container;
  }
```
This function is called whenever a block is being written to XML.  If the function does not exist or returns null, then no mutation is recorded.  If the function exists and returns a 'mutation' XML element, then this element (and any properties or child elements) will be stored as part of the block's XML representation.  In the above case the XML will include this tag: ` <mutation plural="true"></mutation> `

The inverse function is ` domToMutation ` which is called whenever a block is being restored from XML.  Here is the example from the aforementioned ` text_trim ` block:
```
  domToMutation: function(xmlElement) {
    // Restore the 'sides' field as plural or singular.
    var plural = (xmlElement.getAttribute('plural') == 'true');
    this.setFieldText(plural ? 'sides' : 'side', 'SIDES');
  }
```
If this function exists, it is passed the block's 'mutation' XML element.  The function may parse the element and reconfigure the block based on the element's properties and child elements.  In the above case, a field is changed from singular to plural.

## compose and decompose

Mutation dialogs allow a user to explode a block into smaller sub-blocks and reconfigure them, thereby changing the shape of the original block.  The dialog button is added to a block in its [init function](wiki/DefiningBlocks#Init_Function).

```
  this.setMutator(new Blockly.Mutator(['controls_if_elseif', 'controls_if_else']));
```

![https://blockly.googlecode.com/svn/wiki/controls_if.png](https://blockly.googlecode.com/svn/wiki/controls_if.png)

The ` setMutator ` function takes one argument, a new Mutator.  The Mutator constructor takes one argument, a list of sub-blocks to show in the mutator's toolbox.  Creating a mutator for a sub-block is not advised at this time.

When a mutator dialog is opened, the block's ` decompose ` function is called to populate the mutator's workspace.
```
  decompose: function(workspace) {
    var ifBlock = new Blockly.Block(workspace, 'controls_if_if');
    ifBlock.initSvg();
    ...
    return ifBlock;
  }
```

At a minimum this function must create and initialize a top-level block for the mutator dialog, and return it.  This function should also populate this top-level block with any sub-blocks which are appropriate.

When a mutator dialog saves its content, the block's ` compose ` function is called to modify the original block according to the new settings.
```
  compose: function(ifBlock) {
    ...
  }
```

This function is passed the top-level block from the mutator's workspace (the same block that was created and returned by the ` compose ` function).  Typically this function would spider the sub-blocks attached to the top-level block, then update the original block accordingly.

This function should take care to ensure that any blocks already connected to the original block should remain connected to the correct inputs, even if the inputs are reordered.