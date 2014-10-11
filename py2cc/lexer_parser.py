#!/usr/bin/python

import ply
import re
import ply.lex as lex
import ply.yacc as yacc
import pprint
import sys

states = (
  ('CODE', 'exclusive'),
  ('BLOCKS', 'exclusive'),
  ('EMITDEDENTS', 'exclusive'),
)

tokens = ( "NUMBER", "EOL", "PRINT", "STRING", "COLON",
           "IDENTIFIER", "WHILE", "TRUE", "FALSE", "IF", "ELSE", "ELIF",
           "PARENL", "PARENR", "COMMA",
           "INDENT", "DEDENT" # , "WS"
          )
# tokens = ( "NUMBER", "EOL", "PRINT", "STRING", "FOREVER", "COLON", "SPACE")

# t_EOL = r'\n'
t_CODE_INITIAL_PRINT = r'print'
# t_CODE_INITIAL_FOREVER = r'while\sTrue'
t_CODE_INITIAL_COLON = r':'
t_CODE_INITIAL_PARENL = r'\('
t_CODE_INITIAL_PARENR = r'\)'
t_CODE_INITIAL_COMMA = r','

def t_CODE_INITIAL_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in ["print", "while", "True", "False", "if", "else", "elif"]: # Check reserved words
        t.type = t.value.upper()
    return t

t_BLOCKS_ignore = ""
t_EMITDEDENTS_ignore = ""
t_CODE_ignore = " \t"

def t_ANY_EOL(t):
    r'\n+'
    # A new line should always switch the parser to the BLOCKS state. This
    # Allows processing of newlines and leading whitespace to inject
    # indent/dedent tokens

    # Also, reset current indentation level - since we haven't checked the
    # new line's indentation yet.
    lexer.curr_spaces_indent = 0
    t.lexer.lineno += len(t.value)
    if t.lexer.lexstate != 'BLOCKS':
        t.lexer.begin('BLOCKS')
    return t

def t_CODE_INITIAL_WS(t):
  r'[ \t]+'
  v = 0
  for char in t.value:
      if char == " ":
          v += 1
      elif char == "\t":
          v += 8
      else:
          v += 0

  t.lexer.curr_indent = v
#  return t

def t_BLOCKS_WS(t):
    r'[ \t]+'
    # We reach this state only after a new line. The number of spaces on this line
    # is therefore the current number of spaces.
    count = 0
    for char in t.value:
      if char == " ":
          count += 1
      if char == "\t":
          count += 8

    lexer.curr_spaces_indent = count

def t_BLOCKS_INDENT(t):
    r'[^ \t\n]'

    # We're checking indent, and have the first non-whitespace character.
    # We probably want to switch to parsing code not whitespace, and figure
    # out whether to emit a dedent or not.
    #
    # Since whitespace checking is look ahead, we jump back one char in the
    # input stream beforehand.
    t.lexer.lexpos -= 1

    # First of all, check out indent level.
    curr_spaces_indent = lexer.curr_spaces_indent

    dedents_needed = 0
    while lexer.indentation_stack[-1] > curr_spaces_indent:
        lexer.indentation_stack.pop()
        dedents_needed += 1

    if dedents_needed > 0:
        t.lexer.dedents_needed = dedents_needed
        t.lexer.begin('EMITDEDENTS')
        return

    # If we get here, then our next step is parsing code, switch to code mode:
    t.lexer.begin('CODE')

    # If we get here, and current indentation is greater than the stack, we're
    # indenting, so we need to add that to the indentation stack and emit an
    # indent token:
    if curr_spaces_indent > lexer.indentation_stack[-1]:
        lexer.indentation_stack.append(lexer.curr_spaces_indent)
        return t

def t_EMITDEDENTS_DEDENT(t):
    r'.'

    # This rule matches any char so it always runs in the EMITDEDENTS state
    # We need to push the char back so it's not skipped during parsing
    t.lexer.lexpos -= 1

    # This allows us to emit as many DEDENT tokens as necessary.
    if t.lexer.dedents_needed > 0:
        t.lexer.dedents_needed -= 1
        return t
    t.lexer.begin('CODE')



def t_CODE_INITIAL_NUMBER(t):
    r'[-]?\d+'
    try:
         t.value = int(t.value)
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno,t.value)
         t.value = 0
    return t

t_ignore  = ' \t'

def t_CODE_INITIAL_DSTRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    t.type = "STRING"
    return t

def t_CODE_INITIAL_SSTRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]
    t.type = "STRING"
    return t

def t_ANY_error(t):
    print "PARSER STATE", t.lexer.lexstate
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

class Grammar(object):
    tokens = tokens
    def p_error(self,p):
        print "Syntax error at", p

    # ---------------------------------------------------------------------
    #
    # High level program structure
    #
    # ---------------------------------------------------------------------
    def p_program1(self,p):
        "program : statementlist"
        p[0] = ["program", p[1] ]

    def p_statementlist_1(self,p):
        "statementlist : statement"
        statement = p[1]
        if statement[0] == "null_statement":
            p[0] = ["statementlist", [ ] ]
        else:
            p[0] = ["statementlist", [ p[1] ] ]

    def p_statementlist_2(self,p):
        "statementlist : statement statementlist"
        assert p[2][0] == "statementlist"

        this_statement = p[1]
        following_statements = p[2][1]

        # Filter out null statements
        if this_statement[0] == "null_statement":
            statement_list = following_statements
        else:
            if len(following_statements) == 1:
                if following_statements[0][0] == "null_statement":
                    following_statements = []
            statement_list = [ this_statement ] +  following_statements
        p[0] = ["statementlist", statement_list ]

    # ---------------------------------------------------------------------
    #
    # Block Structure
    #
    # ---------------------------------------------------------------------
    def p_block_1(self,p):
        "block : INDENT DEDENT"
        p[0] = ["block", [] ]

    def p_block_2(self,p):
        "block : INDENT statementlist DEDENT"
        p[0] = ["block", p[2] ]

    # ---------------------------------------------------------------------
    #
    # Statement types : empty, print, bare expression, forever
    # TBD: for, while, def
    # NOTE To be decided - class, import, etc
    # ---------------------------------------------------------------------
    def p_statement_0(self,p):
        "statement : EOL"
        p[0] = ["null_statement", p[1] ]

    def p_statement_1(self,p):
        "statement : print_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_2(self,p):
        "statement : expression"
        p[0] = ["statement", p[1] ]

    def p_statement_4(self,p):
        "statement : while_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_4(self,p):
        "statement : if_statement"
        p[0] = ["statement", p[1] ]

    def p_while_statement_1(self,p):
        "while_statement : WHILE expression COLON EOL block"
        if p[2][0] == "expression":
            expr = p[2][1]
            if expr[0] == "literalvalue":
                value = expr[1]
                if value[0] == "boolean":
                    if value[1] == "True":
                        p[0] = ["forever_statement", p[5][1] ]
                        return
                    elif value[1] == "False":
                        p[0] = ["never_statement", p[5][1] ]
                        return

        p[0] = ["while_statement", p[2][1],p[5][1] ]

    #---------------------------------------------------
    # IF Statement
    # This could do with some TLC to re-arrange the structure of the if statements here
    # 
    def p_if_statement_1(self,p):
        "if_statement : IF expression COLON EOL block"
        p[0] = ["if_statement", p[2][1], p[5][1] ]

    def p_if_statement_2(self,p):
        "if_statement : IF expression COLON EOL block if_trailer"
        p[0] = ["if_statement", p[2][1], p[5][1], p[6]]

    def p_if_trailer_1(self,p):
        """if_trailer : elif_clauses"""
        print "HERE", len(p), p[0], p[1]
        p[0] = p[1]

    def p_elif_clauses_1(self,p):
        """elif_clauses : elif_clause"""
        print "HERE", len(p), p[0], p[1]
        p[0] = p[1]

    def p_elif_clauses_2(self,p):
        """elif_clauses : elif_clause if_trailer"""
        print "HERE", len(p), p[0], p[1]
        p[0] = [ p[1], p[2] ]

    def p_if_trailer_2(self,p):
        """if_trailer : else_clause"""

        print "HERE", len(p), p[0], p[1]
        p[0] = p[1]

    #def p_elif_clauses_1(self,p):
        #"""elif_clauses : elif_clause
                        #| elif_clauses"""

        #print "THERE", len(p), p[0], p[1]
        #p[0] = p[1]

    def p_elif_clause_1(self,p):
        "elif_clause : ELIF expression COLON EOL block"
        p[0] = ["elif_clause", p[2][1], p[5][1] ]

    def p_else_clause_1(self,p):
        "else_clause : ELSE COLON EOL block"
        p[0] = ["else_clause", p[4][1]]

    def p_print_statement_1(self,p):
        "print_statement : PRINT expression"
        p[0] = ["print_statement", p[2] ]

    # ---------------------------------------------------------------------
    #
    # Expressions : literals, functional calls
    # TBD: infix expressions
    # ---------------------------------------------------------------------
    def p_expression(self,p):
        """expression : literalvalue
                      | func_call """
        p[0] = ["expression", p[1] ]

    def p_func_call1(self,p):
        "func_call : IDENTIFIER PARENL PARENR"
        p[0] = ["func_call", p[1] ]

    def p_func_call2(self,p):
        "func_call : IDENTIFIER PARENL func_args PARENR"
        p[0] = ["func_call", p[1], p[3] ]

    def p_func_args1(self,p):
        "func_args : expression "
        p[0] = ["func_args", p[1] ]

    def p_func_args2(self,p):
        "func_args : expression COMMA func_args"
        p[0] = ["func_args", p[1], p[3] ]


    # ---------------------------------------------------------------------
    #
    # Literal Values : number, identifier, string
    #  TBD: boolean, real, array
    # ---------------------------------------------------------------------
    def p_expressionatom(self,p):
        """literalvalue : number 
                        | identifier
                        | string
                        | boolean"""
        p[0] = ["literalvalue", p[1] ]

    def p_number(self,p):
        "number : NUMBER"
        p[0] = ["number", p[1] ]

    def p_string(self,p):
        "string : STRING"
        p[0] = ["string", p[1] ]

    def p_boolean(self,p):
        """boolean : TRUE
                   | FALSE"""
        p[0] = ["boolean", p[1] ]

    def p_identifier(self,p):
        "identifier : IDENTIFIER"
        p[0] = ["identifier", p[1] ]


def mktoken(type, value, lineno, lexpos):
    tok = lex.LexToken()
    tok.type = type
    tok.value = value
    tok.lineno = lineno
    tok.lexpos = lexpos
    return tok

def parse(source,lexer):
   yacc.yacc(module=Grammar())
   result = yacc.parse(source, lexer=lexer)
   return result


def configure_lexer():
    #    
    global lexer
    lexer =  lex.lex(reflags=re.MULTILINE)
    lexer.curr_spaces_indent = 0

    lexer.indentation_stack = []
    lexer.indentation_stack.append(lexer.curr_spaces_indent)

    def trace(lexer, *argv):
        token = lexer.token_()
        sys.stderr.write("TOKEN ")
        sys.stderr.write(repr( token ) )
        sys.stderr.write("\n")
        sys.stderr.flush()

        if token is not None:
            return token

        if len(lexer.indentation_stack) == 1:
            return 

        lexer.indentation_stack.pop()
        token = lex.LexToken()
        token.value = ''
        token.type = 'DEDENT'
        token.lineno = lexer.lineno
        token.lexpos = lexer.lexpos
        token.lexer = lexer
        return token


    lexer.token_ = lexer.token
    lexer.token = (lambda: trace(lexer))

    lexer.begin('BLOCKS')

    return lexer
#    return lex.lexer
