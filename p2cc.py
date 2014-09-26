#!/usr/bin/python

import ply
import re
import ply.lex as lex

tokens = ( "NUMBER", )

def t_NUMBER(t):
    r'[-]?\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno,t.value)
         t.value = 0
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

class Grammar(object):
    tokens = tokens
    def p_error(self,p):
        print "Syntax error at", p

    def p_program(self,p):
        "program : NUMBER"
        p[0] = ["program", p[1] ]


lex.lex(reflags=re.MULTILINE)

import ply.yacc as yacc


def parse(source,lexer):
   yacc.yacc(module=Grammar())
   result = yacc.parse(lexer=lexer)
   return result

sourcelines = open("tests/progs/1.p").read().split("\n")
sourcelines = [ x for x in sourcelines if x != "" ]
print repr(sourcelines )

yacc.yacc(module=Grammar())

for line in sourcelines:
    x = yacc.parse(line)
    print x


# parse(source=sourcelines, lexer=lexer)

