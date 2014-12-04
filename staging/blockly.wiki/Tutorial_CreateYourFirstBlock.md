# Tutorial - Create and add your first block - Step-by-step guide

![http://i289.photobucket.com/albums/ll234/syntax_photos/BlockFactory_MoveTo_Preview_zps16065a5d.png](http://i289.photobucket.com/albums/ll234/syntax_photos/BlockFactory_MoveTo_Preview_zps16065a5d.png)
<br>
<h2>Introduction</h2>

This tutorial a complete walk though for adding a block to the turtle app.<br>
By the end of the tutorial you will have a fully functional new block in the turtle tool box.<br>
This new block, called <b>move to</b> will move the turtle directly to a specified x/y location.<br>
<br>
<br>
<h2>Before you begin</h2>

The basic tools you need for this tutorial are:<br>
<br>
<ul><li>Subversion</li></ul>

<ul><li>A simple text editor (also an IDE for Javascript code editor would be good)</li></ul>

<ul><li>The Blockly source code</li></ul>

<ul><li>A browser</li></ul>

<br>
<h3>Installing Subversion</h3>
<hr />
For Linux its a simple matter of running this in a terminal window:<br>
<pre><code>	&gt; sudo apt-get install subversion<br>
</code></pre>

For Windows see <a href='http://tortoisesvn.net/'>http://tortoisesvn.net/</a>


<h3>Install the Blockly source code</h3>
<hr />
To get the latest verison of Blockly run the following from a terminal window:<br>
<pre><code>	&gt; svn checkout http://blockly.googlecode.com/svn/trunk/ blockly<br>
</code></pre>
Once everything is downloaded you will have a new <b>Blockly</b> folder containing the code and examples.<br>
Since this tutorial modifies the <b>turtle</b> app files you might want to copy the folder and contents for backup purposes.<br>
The folder in question is called "turtle" and exists in the "blockly/apps/" folder.<br>
<br>
<br>
<h3>Pre-checks</h3>

Open the <b>Blockly/apps/turtle</b> folder. Test the turtle app by double-clicking the <b>index.html</b> file.<br>
Make sure it runs in the browser.<br>
<br>
The files which are going to be modified are <b>turtle.js</b>, <b>blocks.js</b>, and <b>template.soy</b> within the folder.<br>
<br>
<br>
<br>
<h2>Step 1 - Designing the block</h2>

Let's start by designing the block itself. Open the online block designer. This designer helps to define how the new block will look and function.<br>
<br>
Open this link: <a href='https://blockly-demo.appspot.com/static/apps/blockfactory/index.html'>https://blockly-demo.appspot.com/static/apps/blockfactory/index.html</a>

Design the block as per this layout:<br>
<br>
<img src='http://i289.photobucket.com/albums/ll234/syntax_photos/BlockFactory_MoveTo_zps80888682.png' />

The preview block should look like this:<br>
<br>
<img src='http://i289.photobucket.com/albums/ll234/syntax_photos/BlockFactory_MoveTo_Preview_zps16065a5d.png' />

Once complete you can see two sets of generated code in the tables to the right.<br>
<br>
<h4>Blockly Language Code</h4>
<pre><code>Blockly.Blocks['move_to'] = {<br>
  init: function() {<br>
    this.setHelpUrl('http://www.example.com/');<br>
    this.setColour(160);<br>
    this.appendDummyInput()<br>
	.appendField("move to");<br>
    this.appendValueInput("XPOS")<br>
	.setCheck("Number")<br>
	.appendField("x");<br>
    this.appendValueInput("YPOS")<br>
	.setCheck("Number")<br>
	.appendField("y");<br>
    this.setInputsInline(true);<br>
    this.setPreviousStatement(true);<br>
    this.setNextStatement(true);<br>
    this.setTooltip('');<br>
}<br>
</code></pre>

<h4>Blockly JavaScript stub code</h4>
<pre><code>Blockly.JavaScript['move_to'] = function(block) {<br>
  var value_xpos = Blockly.JavaScript.valueToCode(block, 'XPOS', Blockly.JavaScript.ORDER_ATOMIC);<br>
  var value_ypos = Blockly.JavaScript.valueToCode(block, 'YPOS', Blockly.JavaScript.ORDER_ATOMIC);<br>
  // TODO: Assemble JavaScript into code variable.<br>
  var code = '...';<br>
  return code;<br>
};<br>
</code></pre>

For more details on block design see:<br>
<a href='https://code.google.com/p/blockly/wiki/DefiningBlocks'>https://code.google.com/p/blockly/wiki/DefiningBlocks</a>

For more details on the code generation see:<br>
<a href='https://code.google.com/p/blockly/wiki/GeneratingCode'>https://code.google.com/p/blockly/wiki/GeneratingCode</a>

<br>
<h2>Step 2 - Editing the blocks.js file</h2>


Open <b>blocks.js</b> via a standard text editor or IDE.<br>
<br>
Taking the above two blocks of code, paste both parts in <i>after</i> this section of code.<br>
<br>
<pre><code>Blockly.JavaScript['draw_move'] = function(block) {<br>
  ...<br>
};<br>
</code></pre>

The code will now need some modification. Replace the source code above with:<br>
<br>
<pre><code>Blockly.Blocks['draw_moveto'] = {<br>
  // move turtle to absolute x,y location<br>
  // for reference 0,0 is top/let and 200,200 is centre<br>
  init: function() {<br>
    this.setHelpUrl('');<br>
    this.setColour(160);<br>
    this.appendDummyInput()<br>
        .appendField(BlocklyApps.getMsg('Turtle_moveTo'));<br>
    this.appendValueInput("XPOS")<br>
        .setCheck("Number")<br>
        .appendField("x");<br>
    this.appendValueInput("YPOS")<br>
        .setCheck("Number")<br>
        .appendField("y");<br>
    this.setInputsInline(true);<br>
    this.setPreviousStatement(true);<br>
    this.setNextStatement(true);<br>
    this.setTooltip(BlocklyApps.getMsg('Turtle_moveToTooltip'));<br>
  }<br>
};<br>
<br>
Blockly.JavaScript['draw_moveto'] = function(block) {<br>
  // Generate JavaScript for moving to absolute position<br>
  var xpos = Blockly.JavaScript.valueToCode(block, 'XPOS', Blockly.JavaScript.ORDER_NONE) || '0';<br>
  var ypos = Blockly.JavaScript.valueToCode(block, 'YPOS', Blockly.JavaScript.ORDER_NONE) || '0';<br>
  return 'Turtle.moveTo(' + xpos + ',' + ypos + ', \'block_id_' + block.id + '\');\n';<br>
};<br>
</code></pre>

Now save the file changes.<br>
<br>
<br>
<br>
<h2>Step 3 - Editing the turtle.js file</h2>

Open <b>turtle.js</b> via a standard text editor or IDE.<br>
<br>
Look for the Turtle API section. It comes under the <b>// Turtle API</b> comment.<br>
<br>
Add the following API block of code after the <b>Turtle.moveBackward{}</b> API block.<br>
<pre><code>	Turtle.moveTo = function(xpos, ypos, id) {<br>
	  BlocklyApps.log.push(['MT', xpos, ypos, id]);<br>
	};<br>
</code></pre>
To cater for this API call another piece of code needs adding into the <b>Turtle.step{}</b> block.<br>
Drop this piece of code inside the <b>switch (command) {...}</b> block of the <b>Turtle.step</b> function.<br>
A sensible place is between the 'FD' (Forward) and 'RT' (Right Turn) sections:<br>
<pre><code>    case 'MT': // Move To<br>
		Turtle.x=values[0];<br>
		Turtle.y=values[1];<br>
		break;<br>
</code></pre>

Now save the file changes.<br>
<br>
<br>
<br>
<h2>Step 4 - Editing the template.soy file</h2>

Open the <b>template.soy</b> file for editing.<br>
<br>
Within the <b>{template .messages}</b> block open up some space and paste in the following.<br>
This is helper/documentation for the move_to block.<br>
A recommended location is after the <code>&lt;span id="Turtle_moveBackward"&gt; ... &gt;&lt;/span&gt;</code> part in the document.<br>
<pre><code>    &lt;span id="Turtle_moveToTooltip"&gt;{msg meaning="Turtle.moveToTooltip" desc="Moves the turtle to an absolute x and y location via 2 numbers. Top left is 0,0 whilst centre is 200,200 (default)."}Moves turtle to the absolute x/y location without drawing a mark{/msg}&lt;/span&gt;<br>
    &lt;span id="Turtle_moveTo"&gt;{msg meaning="Turtle.moveTo" desc="block text - Infinitive or imperative of a verb to move the turtle to an absolute x and y location via 2 numbers. Top left is 0,0 whilst centre is 200,200 (default)."}move to{/msg}&lt;/span&gt;<br>
</code></pre>
In order to make the new block appear in the tool box scroll down to the <code>{template .toolbox}</code> section and insert the following. A logical place for the "move to" block to appear in the tool box is after existing the "draw move" block. Therefore, paste this section after <pre><block type="draw_move"> ... <br>
<br>
Unknown end tag for </block><br>
<br>
</pre>

<pre><code>	&lt;block type="draw_moveto"&gt;<br>
		&lt;value name="XPOS"&gt;<br>
			&lt;block type="math_number"&gt;<br>
				&lt;field name="NUM"&gt;200&lt;/field&gt;<br>
			&lt;/block&gt;<br>
		&lt;/value&gt;<br>
		&lt;value name="YPOS"&gt;<br>
			&lt;block type="math_number"&gt;<br>
				&lt;field name="NUM"&gt;200&lt;/field&gt;<br>
			&lt;/block&gt;<br>
		&lt;/value&gt;<br>
	&lt;/block&gt;<br>
</code></pre>

Now save the file changes.<br>
<br>
<br>
<br>
<h2>Step 5 - Compling the code changes</h2>

Before continuing ensure all changes to the <b>turtle.js</b>, <b>blocks.js</b>, and <b>template.soy</b> files have been saved.<br>
<br>
Now that the code has been entered it's time to compile the changes.<br>
Open up a terminal window and navigate into the turtle folder. For example:<br>
<pre><code>&gt; cd &lt;myfolder&gt;/blockly/apps/turtle<br>
</code></pre>
Look at the top of the <b>template.soy</b> document. You should find an entry like this:<br>
<pre><code>	java -jar ../_soy/SoyToJsSrcCompiler.jar --outputPathFormat generated/en.js --srcs ../common.soy,template.soy<br>
</code></pre>
Copy this line then paste it into the terminal window. After a few seconds the compiling process should complete. If all went well (no reported errors) you can now test the new block.<br>
<br>
<br>
<br>
<h2>Step 6 - Testing the new block</h2>

From the turtles folder double-click <b>index.html</b>. This should launch the turtle blockly program in your browser.<br>
Open the toolbox and check to see if the new ''move to'' block is present.<br>
Hovering over the new block should reveal the help text popup balloon.<br>
<br>
Constuct a simple test block and run the code. Example:<br>
<br>
<img src='http://i289.photobucket.com/albums/ll234/syntax_photos/blockly_moveto_example_zps124a199d.png' />

You can check that the code is being correctly to generated by pressing the code button:<br>
<br>
<img src='http://i289.photobucket.com/albums/ll234/syntax_photos/Blockly_ShowCode_zpse5531019.png' />

The generated code should look like this:<br>
<pre><code>var x_position;<br>
<br>
Turtle.turnRight(30);<br>
for (x_position = 100; x_position &lt;= 300; x_position += 15) {<br>
  Turtle.moveTo(x_position,220);<br>
  Turtle.moveForward(50);<br>
}<br>
</code></pre>

<br><br>

<h2>END OF TUTORIAL</h2>

That's your first block under way. If you want to modify the blocks functionality/appearance then its just a matter of changing the code and re-compiling (as per Step 5).<br>
<br>
Note that you can leave the browser open but you will need to refresh the page in order to see new changes take place.<br>
<br>
(TODO: Link to Google+ page.)<br>
<br>
<b>Please send any questions you have to the <a href='https://groups.google.com/forum/#!forum/blockly'>support group</a>, not as a comment to this page.</b>