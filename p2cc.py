#!/usr/bin/python

import ply
import re
import ply.lex as lex

tokens = ( "NUMBER", "EOL")

def t_NUMBER(t):
    r'[-]?\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno,t.value)
         t.value = 0
    return t

t_EOL = r'\n'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

class Grammar(object):
    tokens = tokens
    def p_error(self,p):
        print "Syntax error at", p

    def p_program1(self,p):
        "program : statementlist"
        p[0] = ["program", p[1] ]

    def p_statementlist_1(self,p):
        "statementlist : statement"
        p[0] = ["statementlist", [ p[1] ] ]

    def p_statementlist_2(self,p):
        "statementlist : statement statementlist"
        assert p[2][0] == "statementlist"
        this_statement = p[1]
        following_statements = p[2][1]
        statement_list = [ this_statement ] +  following_statements
        p[0] = ["statementlist", statement_list ]

    def p_statement_1(self,p):
        "statement : expression"
        p[0] = ["statement", p[1] ]

    def p_statement_2(self,p):
        "statement : expression EOL"
        p[0] = ["statement", p[1] ]

    def p_expression(self,p):
        "expression : expressionatom"
        p[0] = ["expression", p[1] ]

    def p_expressionatom(self,p):
        "expressionatom : number"
        p[0] = ["expressionatom", p[1] ]

    def p_number(self,p):
        "number : NUMBER"
        p[0] = ["number", p[1] ]


lex.lex(reflags=re.MULTILINE)

import ply.yacc as yacc


def parse(source,lexer):
   yacc.yacc(module=Grammar())
   result = yacc.parse(lexer=lexer)
   return result

import pprint

for filename in [
                 "tests/progs/1.p",
                 "tests/progs/2.p",
                 "tests/progs/3.p"
                ]:
    print "PARSING", filename
    source = open(filename).read()
    yacc.yacc(module=Grammar())
    x = yacc.parse(source)
    pprint.pprint(x,width=120)
    print "-"*120

import os
os.unlink("parser.out")
os.unlink("parsetab.py")
os.unlink("parsetab.pyc")

