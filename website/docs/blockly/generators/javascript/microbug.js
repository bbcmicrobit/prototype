'use strict';

goog.provide('Blockly.JavaScript.microbug');

goog.require('Blockly.JavaScript');

var prefix = 'DALJS.'; //any prefix can be added to the function names, just in case they end up being namespaced or in an object

Blockly.JavaScript['microbug_scrollstring'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'Message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_speed = Blockly.JavaScript.valueToCode(block, 'Speed', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'scrollString(' + value_message + ',' + value_speed + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_seteye'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_state = Blockly.JavaScript.valueToCode(block, 'state', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'setEye(' + value_id + ',' + value_state + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_eyeon'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eyeOn(' + value_id + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_eyeoff'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eyeOff(' + value_id + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_toggleeye'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'toggleEye(' + value_id + ');';
  return code;
};

Blockly.JavaScript['microbug_printmessage'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_pausetime = Blockly.JavaScript.valueToCode(block, 'pausetime', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'printMessage(' + value_message + ',' + value_pausetime + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_showletter'] = function(block) {
  var value_letter = Blockly.JavaScript.valueToCode(block, 'letter', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'showLetter(' + value_letter + ');';
  return prefix+code;
}

Blockly.JavaScript['microbug_getbutton'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'getButton(' + value_id + ');';
  // TODO: Change ORDER_NONE to the correct strength.
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_cleardisplay'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'clearDisplay();';
  return prefix+code;
};

Blockly.JavaScript['microbug_plot'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'plot(' + value_x + ',' + value_y + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_unplot'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'unplot(' + value_x + ',' + value_y + ');';
  return prefix+code;
};

Blockly.JavaScript['microbug_point'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'point(' + value_x + ',' + value_y + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_buildsprite'] = function(block)
{
    for (var b = "buildSprite([", c = 0; 5 > c; c++)
    {
        for (var b = b + "[", d = 0; 5 > d; d++) b += "TRUE" == block.getFieldValue("LED" + d + c) ? 1 : 0, b += 4 > d ? ", " : "";
        b += "]";
        b += 4 > c ? ", " : ""
    }
    return [prefix + b + "])", Blockly.JavaScript.ORDER_FUNCTION_CALL];
};

Blockly.JavaScript['microbug_setdisplay'] = function(block)
{
  var value_var = Blockly.JavaScript.valueToCode(block, 'SPRITE', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'setDisplay(' + value_var + ');';
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
}

Blockly.JavaScript['microbug_showviewport'] = function(block) {
  var value_sprite = Blockly.JavaScript.valueToCode(block, 'sprite', Blockly.JavaScript.ORDER_ATOMIC);
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'showViewport(' + value_sprite + ',' + value_x + ',' + value_y + ');';
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_scrollimage'] = function(block) {
  var value_sprite = Blockly.JavaScript.valueToCode(block, 'sprite', Blockly.JavaScript.ORDER_ATOMIC);
  var value_delay = Blockly.JavaScript.valueToCode(block, 'delay', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'scrollImage(' + value_sprite + ',' + value_delay + ');';
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['microbug_imagepoint'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'imagePoint(' + value_id + ',' + value_x + ',' + value_y + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_setimagepoint'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'setImagePoint(' + value_id + ',' + value_x + ',' + value_y + ',' + value_value + ')';
  return [prefix+code, Blockly.JavaScript.ORDER_NONE];
};

// Blockly.JavaScript['microbug_scrollsprite'] = function(block) {
//   var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
//   var value_delay = Blockly.JavaScript.valueToCode(block, 'delay', Blockly.JavaScript.ORDER_ATOMIC);
//   // TODO: Assemble JavaScript into code variable.
//   var code = 'scrollSprite(' + value_id + ',' + value_delay + ');';
//   return [prefix+code, Blockly.JavaScript.ORDER_NONE];
// };


// FOREVER LOOP (while true?)



