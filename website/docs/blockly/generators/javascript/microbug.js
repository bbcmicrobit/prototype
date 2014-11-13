'use strict';

goog.provide('Blockly.JavaScript.microbug');

goog.require('Blockly.JavaScript');

Blockly.JavaScript['microbug_scrollString'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'Message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_speed = Blockly.JavaScript.valueToCode(block, 'Speed', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'DALJS.scrollString(' + value_message + ',' + value_speed + ')';
  return code;
};