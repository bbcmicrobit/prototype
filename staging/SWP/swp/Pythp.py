#!/usr/bin/env python
#
# Simple experiment to build a parser capable of handling
# non-hinted semantic whitespace using ply
#
# Uses the PLY parsing toolkit from:
#            http://systems.cs.uchicago.edu/ply/
#

from Parser import myParser
import Parser
from Lexer import myLexer

from samplePrograms import program
source = program["semantics_functioncall_singleexpression"].split("\n")

lexer=myLexer(source)
parser = myParser(lexer, source)
result = parser.parse()

print "The result of parsing your program:"
print result
print "RULES CHECKED"
for r in Parser.r:
   print "   ", r

#print

#result.walker.evaluate()
