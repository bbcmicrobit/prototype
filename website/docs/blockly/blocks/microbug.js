'use strict';

goog.provide('Blockly.Blocks.microbug');

goog.require('Blockly.Blocks');

Blockly.Blocks['microbug_scrollstring'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("scrollstring");
    this.appendValueInput("Message")
        .setCheck("String")
        .appendField("String");
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

Blockly.Blocks['microbug_toggleeye'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("toggleEye");
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

Blockly.Blocks['microbug_buildsprite'] = {
    init: function()
    {
        this.setColour(160);
        this.appendDummyInput().appendField("build sprite");
        this.appendDummyInput().appendField("4").appendField(new Blockly.FieldCheckbox("FALSE"), "LED04").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED14").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED24").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED34").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED44");
        this.appendDummyInput().appendField("3").appendField(new Blockly.FieldCheckbox("FALSE"), "LED03").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED13").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED23").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED33").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED43");
        this.appendDummyInput().appendField("2").appendField(new Blockly.FieldCheckbox("FALSE"), "LED02").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED12").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED22").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED32").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED42");
        this.appendDummyInput().appendField("1").appendField(new Blockly.FieldCheckbox("FALSE"), "LED01").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED11").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED21").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED31").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED41");
        this.appendDummyInput().appendField("0").appendField(new Blockly.FieldCheckbox("FALSE"), "LED00").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED10").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED20").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED30").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED40");
        this.appendDummyInput().appendField("    0     1     2     3     4");
        this.setOutput(!0);
    }
};

Blockly.Blocks['microbug_buildbigsprite'] = {
    init: function()
    {
        this.setColour(160);
        this.appendDummyInput().appendField("build big sprite");

        this.appendDummyInput().appendField("4").appendField(new Blockly.FieldCheckbox("FALSE"), "LED04").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED14").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED24").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED34").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED44")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "LED54").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED64").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED74").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED84").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED94");

        this.appendDummyInput().appendField("3").appendField(new Blockly.FieldCheckbox("FALSE"), "LED03").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED13").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED23").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED33").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED43")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "LED53").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED63").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED73").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED83").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED93");

        this.appendDummyInput().appendField("2").appendField(new Blockly.FieldCheckbox("FALSE"), "LED02").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED12").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED22").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED32").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED42")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "LED52").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED62").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED72").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED82").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED92");

        this.appendDummyInput().appendField("1").appendField(new Blockly.FieldCheckbox("FALSE"), "LED01").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED11").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED21").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED31").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED41")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "LED51").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED61").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED71").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED81").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED91");

        this.appendDummyInput().appendField("0").appendField(new Blockly.FieldCheckbox("FALSE"), "LED00").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED10").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED20").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED30").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED40")
            .appendField(new Blockly.FieldCheckbox("FALSE"), "LED50").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED60").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED70").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED80").appendField(" ").appendField(new Blockly.FieldCheckbox("FALSE"), "LED90");        

        this.appendDummyInput().appendField("    0     1     2     3     4     5     6     7     8     9");

        this.setOutput(!0);
    }
};

Blockly.Blocks['microbug_setdisplay'] = {
    init: function()
    {
        this.setColour(160);
        this.appendDummyInput().appendField("setdisplay");
        this.appendValueInput("SPRITE").appendField("sprite");
        this.setInputsInline(!0);
        this.setPreviousStatement(!0);
        this.setNextStatement(!0);
    }
};

Blockly.Blocks['microbug_showviewport'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("showviewport");
    this.appendValueInput("sprite")
//        .setCheck("sprite")
        .appendField("sprite");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("x");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("y");
    this.setTooltip('');
    this.setPreviousStatement(!0);
    this.setNextStatement(!0);
  }
};

Blockly.Blocks['microbug_scrollimage'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("scrollimage");
    this.appendValueInput("sprite")
//      .setCheck("sprite")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("sprite");
    this.appendValueInput("delay")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("delay");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

Blockly.Blocks['microbug_imagepoint'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("imagepoint");
    this.appendValueInput("id")
        .setCheck("sprite")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("sprite");
    this.appendValueInput("x")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("x");
    this.appendValueInput("y")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("y");
    this.setOutput(true);
    this.setTooltip('');
  }
};

Blockly.Blocks['microbug_setimagepoint'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(260);
    this.appendDummyInput()
        .appendField("setimagepoint");
    this.appendValueInput("id")
        .setCheck("sprite")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("sprite");
    this.appendValueInput("x")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("x");
    this.appendValueInput("y")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("y");
    this.appendValueInput("value")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("value");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

// Blockly.Blocks['microbug_scrollsprite'] = {
//   init: function() {
//     this.setHelpUrl('http://www.example.com/');
//     this.setColour(260);
//     this.appendDummyInput()
//         .appendField("scrollsprite");
//     this.appendValueInput("id")
//         .setCheck("sprite")
//         .setAlign(Blockly.ALIGN_RIGHT)
//         .appendField("sprite");
//     this.appendValueInput("delay")
//         .setCheck("Number")
//         .setAlign(Blockly.ALIGN_RIGHT)
//         .appendField("delay");
//     this.setPreviousStatement(true);
//     this.setNextStatement(true);
//     this.setTooltip('');
//   }
// };

