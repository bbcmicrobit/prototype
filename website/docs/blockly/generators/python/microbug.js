'use strict';

goog.provide('Blockly.Python.microbug');

goog.require('Blockly.Python');

var prefix = ''; //any prefix can be added to the function names, just in case they end up being namespaced or in an object

Blockly.Python['microbug_scrollstring'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'Message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_speed = Blockly.JavaScript.valueToCode(block, 'Speed', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'scrollString(' + value_message + ',' + value_speed + ')\n';
  return prefix+code;
};

Blockly.Python['microbug_seteye'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_state = Blockly.JavaScript.valueToCode(block, 'state', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'setEye(' + value_id + ',' + value_state + ')\n';
  return prefix+code;
};

Blockly.Python['microbug_eyeon'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eyeOn(' + value_id + ')\n';
  return prefix+code;
};

Blockly.Python['microbug_eyeoff'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eyeOff(' + value_id + ')\n';
  return prefix+code;
};

Blockly.Python['microbug_printmessage'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_pausetime = Blockly.JavaScript.valueToCode(block, 'pausetime', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'printMessage(' + value_message + ',' + value_pausetime + ')\n';
  return prefix+code;
};

Blockly.Python['microbug_showletter'] = function(block) {
  var value_letter = Blockly.JavaScript.valueToCode(block, 'letter', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'showLetter(' + value_letter + ')\n';
  return prefix+code;
}

Blockly.Python['microbug_getbutton'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'getButton(' + value_id + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Python['microbug_cleardisplay'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'clearDisplay()\n';
  return prefix+code;
};

Blockly.Python['microbug_plot'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'DALJS.plot(' + value_x + ',' + value_y + ')\n';
  return prefix+code;
};

Blockly.Python['microbug_unplot'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'unplot(' + value_x + ',' + value_y + ')\n';
  return prefix+codecode;
};

Blockly.Python['microbug_point'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'point(' + value_x + ',' + value_y + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

// FOREVER LOOP (while true?)

