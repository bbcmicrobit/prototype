'use strict';

goog.provide('Blockly.Blocks.microbug');

goog.require('Blockly.Blocks');

Blockly.Blocks['microbug_scrollString'] = {
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