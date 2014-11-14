'use strict';

goog.provide('Blockly.Blocks.microbug');

goog.require('Blockly.Blocks');

Blockly.Blocks['microbug_scrollstring'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(300);
    this.appendValueInput("Message")
        .setCheck("String")
        .appendField("Message");
    this.appendValueInput("Speed")
        .setCheck("Number")
        .appendField("Speed");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

// https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#83qc3o
Blockly.Blocks['microbug_seteye'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("setEye");
    this.appendValueInput("id")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("id");
    this.appendValueInput("state")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("state");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
    }   
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#jgkr8y
Blockly.Blocks['microbug_eyeon'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("eyeOn");
    this.appendValueInput("id")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("id");
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};
Blockly.Blocks['microbug_eyeoff'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("eyeOff");
    this.appendValueInput("id")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("id");
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#tmkc86
Blockly.Blocks['microbug_printmessage'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("print message");
    this.appendValueInput("message")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Message");
    this.appendValueInput("pausetime")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Pausetime");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#xiu9u7
Blockly.Blocks['microbug_showletter'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("showLetter");
    this.appendValueInput("letter")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT);
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#oxk4nt
Blockly.Blocks['microbug_getbutton'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("getButton");
    this.appendValueInput("id")
        .setCheck("String")
        .appendField("id");
    this.setInputsInline(true);
    this.setOutput(true);
    this.setTooltip('');
  }
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#nwf7c5
Blockly.Blocks['microbug_cleardisplay'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("clearDisplay");
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#rhpgfx
Blockly.Blocks['microbug_plot'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("plot");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("x");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("y");
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};
Blockly.Blocks['microbug_unplot'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("unplot");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("x");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("y");
    this.setInputsInline(true);
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#jw5b4i
Blockly.Blocks['microbug_point'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("point");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("x");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("y");
    this.setInputsInline(true);
    this.setOutput(true);
    this.setTooltip('');
  }
};