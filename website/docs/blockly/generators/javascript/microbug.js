'use strict';

goog.provide('Blockly.JavaScript.microbug');

goog.require('Blockly.JavaScript');

Blockly.JavaScript['microbug_scroll_string'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'Message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_speed = Blockly.JavaScript.valueToCode(block, 'Speed', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'scroll_string(' + value_message + ',' + value_speed + ');';
  return code;
};

Blockly.JavaScript['microbug_set_eye'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_state = Blockly.JavaScript.valueToCode(block, 'state', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'set_eye(' + value_id + ',' + value_state + ');';
  return code;
};

Blockly.JavaScript['microbug_eye_on'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eye_on(' + value_id + ');';
  return code;
};

Blockly.JavaScript['microbug_eye_off'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eye_off(' + value_id + ');';
  return code;
};

Blockly.JavaScript['microbug_toggle_eye'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'toggle_eye(' + value_id + ');';
  return code;
};

Blockly.JavaScript['microbug_print_message'] = function(block) {
  var value_message = Blockly.JavaScript.valueToCode(block, 'message', Blockly.JavaScript.ORDER_ATOMIC);
  var value_pausetime = Blockly.JavaScript.valueToCode(block, 'pausetime', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'print_message(' + '""+'value_message + ',' + value_pausetime + ');';
  return code;
};

Blockly.JavaScript['microbug_show_letter'] = function(block) {
  var value_letter = Blockly.JavaScript.valueToCode(block, 'letter', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'show_letter(' + value_letter + ');';
  return code;
}

Blockly.JavaScript['microbug_get_button'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'get_button(' + value_id + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_clear_display'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'clear_display();';
  return code;
};

Blockly.JavaScript['microbug_plot'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'plot(' + value_x + ',' + value_y + ');';
  return code;
};

Blockly.JavaScript['microbug_unplot'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'unplot(' + value_x + ',' + value_y + ');';
  return code;
};

Blockly.JavaScript['microbug_point'] = function(block) {
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'point(' + value_x + ',' + value_y + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_build_image'] = function(block)
{
    var b = "'5,5,";
    for (var c = 0; 5 > c; c++)
    {
        for (var d = 0; 5 > d; d++) b += "TRUE" == block.getFieldValue("LED" + d + c) ? 1 : 0, b += 4 > d ? ", " : "";
        b += 4 > c ? ", " : ""
    }
//    console.log("buildsprite " + b);
    return ["makeImage(" + b + "')", Blockly.JavaScript.ORDER_FUNCTION_CALL];
};

Blockly.JavaScript['microbug_build_big_image'] = function(block)
{
    var w = 10;
    var h = 5;
    var b = "'10,5,"; //sprite dimension comes first
    for (var c = 0; h > c; c++)
    {
       for (var d = 0; w > d; d++) b += "TRUE" == block.getFieldValue("LED" + d + c) ? 1 : 0, b += (w-1) > d ? "," : "";
       b += (h-1) > c ? "," : "";
    }
    return ["makeImage(" + b + "')", Blockly.JavaScript.ORDER_FUNCTION_CALL];
};


Blockly.JavaScript['microbug_show_image'] = function(block)
{
  var value_var = Blockly.JavaScript.valueToCode(block, 'SPRITE', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'show_image(' + value_var + ');';
//  console.log(code);
  return code;
}

Blockly.JavaScript['microbug_show_image_offset'] = function(block) {
  var value_sprite = Blockly.JavaScript.valueToCode(block, 'sprite', Blockly.JavaScript.ORDER_ATOMIC);
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'show_image_offset(' + value_sprite + ',' + value_x + ',' + value_y + ');';
  return code;
};

Blockly.JavaScript['microbug_scroll_image'] = function(block) {
  var value_sprite = Blockly.JavaScript.valueToCode(block, 'sprite', Blockly.JavaScript.ORDER_ATOMIC);
  var value_delay = Blockly.JavaScript.valueToCode(block, 'delay', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'scroll_image(' + value_sprite + ',' + value_delay + ');';
  return code;
};

Blockly.JavaScript['microbug_get_image_point'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'get_image_point(' + value_id + ',' + value_x + ',' + value_y + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_set_image_point'] = function(block) {
  var value_id = Blockly.JavaScript.valueToCode(block, 'id', Blockly.JavaScript.ORDER_ATOMIC);
  var value_x = Blockly.JavaScript.valueToCode(block, 'x', Blockly.JavaScript.ORDER_ATOMIC);
  var value_y = Blockly.JavaScript.valueToCode(block, 'y', Blockly.JavaScript.ORDER_ATOMIC);
  var value_value = Blockly.JavaScript.valueToCode(block, 'value', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'set_image_point(' + value_id + ',' + value_x + ',' + value_y + ',' + value_value + ');';
  return code;
};

Blockly.JavaScript['microbug_make_StringImage'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  //prepend string with space to 'fix' scrolling issue
  //var fixed_value_name = value_name.substr(0, 1) + " " + value_name.substr(1);
  var code = 'new StringImage( " " + ' + value_name + ')';
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_scroll_string_image'] = function(block) {
  var value_string = Blockly.JavaScript.valueToCode(block, 'string', Blockly.JavaScript.ORDER_ATOMIC);
  var value_speed = Blockly.JavaScript.valueToCode(block, 'speed', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'scroll_string_image(' + value_string + ',' + value_speed + ');';
  return code;
};

Blockly.JavaScript['microbug_pause'] = function(block) {
  var value_pause = Blockly.JavaScript.valueToCode(block, 'pause', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'pause(' + value_pause + ');'
  return code;
};

Blockly.JavaScript['microbug_forever'] = function(block) {
  var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
  var code = 'while (true) {' + statements_name + '}';
  return code;
};

Blockly.JavaScript['microbug_get_eye'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'get_eye(' + value_name + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['microbug_logic_onoff_states'] = function(block) {
  var code = (block.getFieldValue('STATE') == 'ON') ? 'ON' : 'OFF';
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['microbug_logic_button_states'] = function(block) {
  var code = (block.getFieldValue('STATE') == 'PRESSED') ? 'PRESSED' : 'NOT_PRESSED';
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

Blockly.JavaScript['microbug_comment'] = function(block) {
  var value_comment = Blockly.JavaScript.valueToCode(block, 'comment', Blockly.JavaScript.ORDER_ATOMIC);
  // Don't generate comments for javascript since nobody's gonna see it
  var code = '';
  return code;
};
