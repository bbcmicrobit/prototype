#!/usr/bin/python

import ply
import re
import ply.lex as lex
import ply.yacc as yacc
import pprint

tokens = ( "NUMBER", "EOL", "PRINT", "STRING", "FOREVER", "COLON")

t_EOL = r'\n'
t_PRINT = r'print'
t_FOREVER = r'forever'
t_COLON = r':'


def t_NUMBER(t):
    r'[-]?\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno,t.value)
         t.value = 0
    return t

t_ignore  = ' \t'

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

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
        "statement : print_statement"
        p[0] = ["statement", p[1] ]

    def p_print_statement_1(self,p):
        "print_statement : PRINT expression"
        p[0] = ["print_statement", p[2] ]

    def p_print_statement_2(self,p):
        "print_statement : PRINT expression EOL"
        p[0] = ["print_statement", p[2] ]

    def p_statement_2(self,p):
        "statement : expression"
        p[0] = ["statement", p[1] ]

    def p_statement_3(self,p):
        "statement : expression EOL"
        p[0] = ["statement", p[1] ]

    def p_expression(self,p):
        "expression : literalvalue"
        p[0] = ["expression", p[1] ]

    def p_expressionatom(self,p):
        """literalvalue : number 
                        | string"""
        p[0] = ["literalvalue", p[1] ]

    def p_number(self,p):
        "number : NUMBER"
        p[0] = ["number", p[1] ]

    def p_string(self,p):
        "string : STRING"
        p[0] = ["string", p[1] ]


lex.lex(reflags=re.MULTILINE)

def parse(source,lexer):
   yacc.yacc(module=Grammar())
   result = yacc.parse(lexer=lexer)
   return result

def configure_lexer():
    lex.lex(reflags=re.MULTILINE)

def configure_parser():
    yacc.yacc(module=Grammar())

def do_parse(source):
    x = yacc.parse(source)
    return x
