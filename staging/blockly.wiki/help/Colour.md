
# Introduction

Blockly users can choose, create, and blend colours.  Colours are primarily used in [the turtle graphics application](https://blockly-demo.appspot.com/static/apps/turtle/index.html) but are also available in [the coding application](https://blockly-demo.appspot.com/static/apps/code/index.html).  Note that we use the British spelling of "colour".

# Blocks
## Picking a colour from a palette

The simplest way to get a colour is with the **colour picker**.  It appears as a red rounded rectangle.  When the user clicks on it, a palette of colours pops open, from which the user can choose the desired colour by again clicking.

![](help/colour-select.png)

## Creating a colour from red, green, and blue components

The **colour with** block allows the user to specify the desired percent of red, green, and blue.  This block builds a colour with the maximum amounts of red and blue and no green (making purple):

![](help/colour-with.png)

Note that we use [a range from 0 to 100 (inclusive) for each component](http://www.december.com/html/spec/colorper.html), not the less intuitive range of 0 to 255 generally used by programmers and graphic designers.

The ability to specify colours with changing numbers allows some beautiful turtle graphic applications, such as [this contest winner](https://plus.google.com/105063463762828771517/posts/HzzPaimTLwu) (see code):

## Generating a random colour

The **random colour** block generates colours at random.

![](help/colour-random-colour.png)

Specifically, each of the red, green, and blue components is a number from 0 to 255 (inclusive), with equal likelihood.

## Blending colours

Unlike traditional turtle graphics systems, Blockly provides a means for blending two colours, as though one were blending two different colours of paint.  The following block provides the colour that would be obtained by mixing equal amounts of red paint (actually, [red light](http://www.newton.dep.anl.gov/askasci/gen99/gen99557.htm)) and yellow paint:

![](help/colour-blend.png)

If the ratio were 0, the result would have no red and all yellow.  If the ratio were 1, the result would be all red and no yellow.

# Technical details

Blockly colours are represented as text of the form "#rrggbb" where "rr", "gg", and "bb" represent the red, green, and blue components, respectively, in the hexadecimal range 00 to ff.  Since colours are usually passed to the "set colour" block in the turtle graphics application, most users are never aware of this, but it is exposed by the following program:

![](help/colour-print.png)

which prints "#ff0000".

Note that [blending light is different from blending pigments](http://www.newton.dep.anl.gov/askasci/gen99/gen99557.htm).  Blending red, green, and blue light in equal ratios yields white light, while blending red, green, and blue paint yields a muddy colour.
