'use strict';

goog.provide('Blockly.Python.microbug');

goog.require('Blockly.Python');

Blockly.Python['microbug_scroll_string'] = function(block) {
    var value_message = Blockly.Python.valueToCode(block, 'Message', Blockly.Python.ORDER_ATOMIC);
    var value_speed = Blockly.Python.valueToCode(block, 'Speed', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'scroll_string(' + value_message + ',' + value_speed + ')\n';
    return code;
};

Blockly.Python['microbug_set_eye'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'set_eye(' + value_id + ',' + value_state + ')\n';
    return code;
};

Blockly.Python['microbug_eye_on'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'eye_on(' + value_id + ')\n';
    return code;
};

Blockly.Python['microbug_eye_off'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'eye_off(' + value_id + ')\n';
    return code;
};

Blockly.Python['microbug_toggle_eye'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'toggle_eye(' + value_id + ')\n';
    return code;
};

Blockly.Python['microbug_print_message'] = function(block) {
    var value_message = Blockly.Python.valueToCode(block, 'message', Blockly.Python.ORDER_ATOMIC);
    var value_pausetime = Blockly.Python.valueToCode(block, 'pausetime', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'print_message(' + value_message + ',' + value_pausetime + ')\n';
    return code;
};

Blockly.Python['microbug_show_letter'] = function(block) {
    var value_letter = Blockly.Python.valueToCode(block, 'letter', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'show_letter(' + value_letter + ')\n';
    return code;
}

Blockly.Python['microbug_get_button'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'get_button(' + value_id + ')';
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['microbug_clear_display'] = function(block) {
    // TODO: Assemble JavaScript into code variable.
    var code = 'clear_display()\n';
    return code;
};

Blockly.Python['microbug_plot'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'plot(' + value_x + ',' + value_y + ')\n';
    return code;
};

Blockly.Python['microbug_unplot'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'unplot(' + value_x + ',' + value_y + ')\n';
    return code;
};

Blockly.Python['microbug_point'] = function(block) {
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'point(' + value_x + ',' + value_y + ')';
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['microbug_build_image'] = function(block) {
    var rows = [0,0,0,0,0];
    for (var row = 0; row < 5; row++) {
        for (var col = 0; col < 5; col++) {
            var isSet = ("TRUE" == block.getFieldValue("LED" + col + row) ? 1 : 0);
            if (isSet)
            	rows[row] += Math.pow(2, col);
        }
		rows[row] = '0x' + rows[row].toString(16);
    }
    return ["make_image(" + rows[0] + "," + rows[1] + "," + rows[2] + "," + rows[3] + "," + rows[4] +")\n", Blockly.Python.ORDER_FUNCTION_CALL];
};

Blockly.Python['microbug_build_big_image'] = function(block) {
    var rows = [0,0,0,0,0];
    for (var row = 0; row < 5; row++) {
        for (var col = 0; col < 10; col++) {
            var isSet = ("TRUE" == block.getFieldValue("LED" + col + row) ? 1 : 0);
            if (isSet)
            	rows[row] += Math.pow(2, col);
        }
        rows[row] = '0x' + rows[row].toString(16);
    }
    return ["make_big_image(" + rows[0] + "," + rows[1] + "," + rows[2] + "," + rows[3] + "," + rows[4] +")\n", Blockly.Python.ORDER_FUNCTION_CALL];
};

Blockly.Python['microbug_show_image'] = function(block) {
    var value_var = Blockly.Python.valueToCode(block, 'SPRITE', Blockly.Python.ORDER_ATOMIC);
    var code = 'show_image(' + value_var + ')\n';
    return code;
}

Blockly.Python['microbug_show_image_offset'] = function(block) {
    var value_sprite = Blockly.Python.valueToCode(block, 'sprite', Blockly.Python.ORDER_ATOMIC);
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
    var code = 'show_image_offset(' + value_sprite + ',' + value_x + ',' + value_y + ')\n';
    return code;
};

Blockly.Python['microbug_scroll_image'] = function(block) {
    var value_sprite = Blockly.Python.valueToCode(block, 'sprite', Blockly.Python.ORDER_ATOMIC);
    var value_delay = Blockly.Python.valueToCode(block, 'delay', Blockly.Python.ORDER_ATOMIC);
    var code = 'scroll_image(' + value_sprite + ',' + value_delay + ')\n';
    return code;
};

Blockly.Python['microbug_get_image_point'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
    var code = 'get_image_point(' + value_id + ',' + value_x + ',' + value_y + ')';
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['microbug_set_image_point'] = function(block) {
    var value_id = Blockly.Python.valueToCode(block, 'id', Blockly.Python.ORDER_ATOMIC);
    var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
    var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
    var value_value = Blockly.Python.valueToCode(block, 'value', Blockly.Python.ORDER_ATOMIC);
    var code = 'set_image_point(' + value_id + ',' + value_x + ',' + value_y + ',' + value_value + ')\n';
    return code;
};

Blockly.Python['microbug_make_StringImage'] = function(block) {
    var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
    //prepend string with space to 'fix' scrolling issue
    var fixed_value_name = value_name.substr(0, 1) + " " + value_name.substr(1);
    var code = 'StringImage(' + fixed_value_name + ')';
    return [code, Blockly.Python.ORDER_NONE];
};




Blockly.Python['microbug_scroll_string_image'] = function(block) {
    var value_string = Blockly.Python.valueToCode(block, 'string', Blockly.Python.ORDER_ATOMIC);
    var value_speed = Blockly.Python.valueToCode(block, 'speed', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'scroll_string_image(' + value_string + ',' + value_speed + ')\n';
    return code;
};

Blockly.Python['microbug_pause'] = function(block) {
    var value_pause = Blockly.Python.valueToCode(block, 'pause', Blockly.Python.ORDER_ATOMIC);
    var code = 'pause(' + value_pause + ')\n'
    return code;
};

Blockly.Python['microbug_forever'] = function(block) {
    var statements_name = Blockly.Python.statementToCode(block, 'NAME');
    // TODO: Assemble JavaScript into code variable.
    var code = 'while True:\n' + statements_name;
    return code;
};

Blockly.Python['microbug_get_eye'] = function(block) {
    var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'get_eye(' + value_name + ')';
    // TODO: Change ORDER_NONE to the correct strength.
    return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['microbug_logic_onoff_states'] = function(block) {

    var code = (block.getFieldValue('STATE') == 'ON') ? 'ON' : 'OFF';
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['microbug_logic_button_states'] = function(block) {
    var code = (block.getFieldValue('STATE') == 'PRESSED') ? 'PRESSED' : 'NOT_PRESSED';
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['microbug_comment'] = function(block) {
    var value_comment = Blockly.Python.valueToCode(block, 'comment', Blockly.Python.ORDER_ATOMIC);
    var code = '# ' + comment + '\n';
    return code;
};
