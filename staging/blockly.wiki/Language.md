# Language Design Philosophy

The primary users of Blockly are novice programmers.  However, in addition to wanting to enable these users to do useful work, we also want to actively support a smooth migration to JavaScript once they outgrow Blockly.  This drives several design decisions.

## One-based Lists

Novice programmers freak out when they encounter zero-based lists for the first time.  As a result, Blockly follows the lead of Lua and Lambda Moo by making list and string indexing one-based.

## Variable Names

Novice programmers do not expect that ` location_X ` and ` location_x ` are different variables.  As a result, Blockly follows the lead of BASIC and HTML by making variables case-insensitive.  Also, Blockly does not require that variables conform to the typical ` [_A-Za-z][_A-Za-z0-9]* ` scheme.  If one wants to name a variable ` List of zip codes ` or 