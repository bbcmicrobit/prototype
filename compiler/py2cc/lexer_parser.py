#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import ply
import re
import ply.lex as lex
import ply.yacc as yacc
import pprint
import sys

quiet_mode = False

states = (
  ('CODE', 'exclusive'),
  ('BLOCKS', 'exclusive'),
  ('EMITDEDENTS', 'exclusive'),
)

reserved_words = ["print", "while", "True", "False", "if", "else", "elif",
                  "for", "in", "from", "import", "def", "yield",
                  "and", "or", "not", "pass"]

tokens = [ "NUMBER", "EOL", "STRING", "COLON",
           "IDENTIFIER", "PLUS", "MINUS", "TIMES", "DIVIDE", "POWER",
           "PARENL", "PARENR", "COMMA", "EQUALS",
           "COMP_OP",
           "INDENT", "DEDENT" # , "WS"
          ] + [x.upper() for x in reserved_words]

tadwidth = 8

t_CODE_INITIAL_PRINT = r'print'
t_CODE_INITIAL_COLON = r':'

t_CODE_INITIAL_EQUALS = r'='
t_CODE_INITIAL_MINUS = r'\-'
t_CODE_INITIAL_PLUS = r'\+'
t_CODE_INITIAL_POWER = r'\*\*'
t_CODE_INITIAL_TIMES = r'\*'
t_CODE_INITIAL_DIVIDE = r'/'
t_CODE_INITIAL_PARENL = r'\('
t_CODE_INITIAL_PARENR = r'\)'
t_CODE_INITIAL_COMMA = r','

def t_CODE_INITIAL_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved_words: # Check reserved words
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
          v += tadwidth

  t.lexer.curr_indent = v


def t_BLOCKS_WS(t):
    r'[ \t]+'
    # We reach this state only after a new line. The number of spaces on this line
    # is therefore the current number of spaces.
    count = 0
    for char in t.value:
      if char == " ":
          count += 1
      if char == "\t":
          count += tadwidth

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
    r'(0x[abcdef\d]+|\d+)'
    # r'[-]?\d+'
    try:
        base = 10
        if t.value[:2]=="0x":
            base = 16
        t.value = int(t.value, base)
    except ValueError:
        if not quiet_mode:
             print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_CODE_INITIAL_COMP_OP(t):
    r'(<|>|==|>=|<=|<>|!=|in|not +in|is|is +not)'
    return t



t_ignore  = ' \t'

def t_CODE_INITIAL_DSTRING(t):
    r'"([^\\"]|(\\.))*"'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\\'', '\'')
    t.type = "STRING"
    return t

def t_CODE_INITIAL_SSTRING(t):
    r"'([^\\']|(\\.))*'"
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\\'', '\'')
    t.type = "STRING"
    return t

def t_ANY_error(t):
    if not quiet_mode:
        print "PARSER STATE", t.lexer.lexstate
        print "Illegal character '%s'" % t.value[0]
    t.skip(1)

class Grammar(object):
    precedence = (
        ('right', 'MINUS'),
    )
    tokens = tokens
    def p_error(self,p):
        if not quiet_mode:
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
        "statement : fullexpression"
        p[0] = ["statement", p[1] ]

    def p_statement_4(self,p):
        "statement : while_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_5(self,p):
        "statement : if_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_6(self,p):
        "statement : for_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_7(self,p):
        "statement : import_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_8(self,p):
        "statement : def_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_9(self,p):
        "statement : yield_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_10(self,p):
        "statement : assignment_statement"
        p[0] = ["statement", p[1] ]

    def p_statement_11(self,p):
        "statement : pass_statement"
        p[0] = ["statement", p[1] ]

    # --------------------------------------------
    # Full Expression - replaces expression
    #
    def p_fullexpression_1(self,p):
        """fullexpression : or_expression"""
        p[0] = p[1]

    def p_fullexpression_2(self,p):
        "or_expression : and_expression"
        p[0] = p[1]

    def p_fullexpression_3(self,p):
        "or_expression : and_expression OR or_expression"
        p[0] = ["or_expression", p[1], p[3] ]

    def p_fullexpression_4(self,p):
        "and_expression : not_expression"
        p[0] = p[1]

    def p_fullexpression_5(self,p):
        "and_expression  : not_expression AND not_expression"
        p[0] = ["expression", ["and_expression", p[1], p[3] ] ]

    def p_fullexpression_6(self,p):
        "not_expression : comparison"
        p[0] = p[1]

    def p_fullexpression_7(self,p):
        "not_expression : NOT not_expression"
        p[0] = ["expression", ["not_expression", p[2] ] ]


    def p_fullexpression_8(self,p):
        "comparison : expression"
        p[0] = p[1]

    def p_fullexpression_9(self,p):
        "comparison : expression COMP_OP expression"
        p[0] = ["comparison", p[2], p[1], p[3]]








    # --------------------------------------------
    # WHILE Statement
    #

    def p_while_statement_1(self,p):
        "while_statement : WHILE fullexpression COLON EOL block"
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

        p[0] = ["while_statement", p[2],p[5][1] ]

    #---------------------------------------------------
    # IF Statement
    # FIXME: elif_clauses are currently nested, they'd be better flattened to make the AST nicer
    #
    def p_if_statement_1(self,p):
        "if_statement : IF fullexpression COLON EOL block"
        p[0] = ["if_statement", p[2], p[5][1] ]

    def p_if_statement_2(self,p):
        "if_statement : IF fullexpression COLON EOL block if_trailer"
        p[0] = ["if_statement", p[2], p[5][1], p[6]]

    def p_if_trailer_1(self,p):
        """if_trailer : elif_clauses"""
        p[0] = p[1]

    def p_elif_clauses_1(self,p):
        """elif_clauses : elif_clause"""
        p[0] = p[1]

    def p_elif_clauses_2(self,p):
        """elif_clauses : elif_clause if_trailer"""
        p[0] = [ p[1], p[2] ]

    def p_if_trailer_2(self,p):
        """if_trailer : else_clause"""
        p[0] = p[1]

    def p_elif_clause_1(self,p):
        "elif_clause : ELIF fullexpression COLON EOL block"
        p[0] = ["elif_clause", p[2], p[5][1] ]

    def p_else_clause_1(self,p):
        "else_clause : ELSE COLON EOL block"
        p[0] = ["else_clause", p[4][1]]

    #-------------------------------------------------
    # PRINT statement
    #
    def p_print_statement_1(self,p):
        "print_statement : PRINT fullexpression"
        p[0] = ["print_statement", p[2] ]

    #-------------------------------------------------
    # PASS statement
    #
    def p_pass_statement_1(self,p):
        "pass_statement : PASS"
        p[0] = ["pass_statement" ]

    #-------------------------------------------------
    # YIELD statement
    #
    def p_yield_statement_1(self,p):
        "yield_statement : YIELD fullexpression"
        p[0] = ["yield_statement", p[2] ]

    #-------------------------------------------------
    # YIELD statement
    #
    def p_assignment_statement_1(self,p):
        "assignment_statement : identifier EQUALS fullexpression"
        p[0] = ["assignment_statement", p[2],p[1],p[3] ]

    #-------------------------------------------------
    # IMPORT statement
    #
    def p_import_statement_1(self,p):
        "import_statement : FROM identifier IMPORT identifier"
        p[0] = ["from_import_statement ", p[2][1], p[4][1] ]

    def p_import_statement_2(self,p):
        "import_statement : IMPORT identifier"
        p[0] = ["import_statement ", p[2][1] ]

    #-------------------------------------------------
    # FOR statement
    #
    def p_for_statement_1(self,p):
        "for_statement : FOR identifier IN fullexpression COLON EOL block"
        p[0] = ["for_statement", p[2], p[4][1], p[7][1] ]

    #-------------------------------------------------
    # DEF statement
    #
    def p_def_statement_1(self,p):
        "def_statement : DEF identifier PARENL PARENR COLON EOL block"
        p[0] = ["def_statement", p[2], None, p[7][1] ]

    def p_def_statement_2(self,p):
        "def_statement : DEF identifier PARENL ident_list PARENR COLON EOL block"
        p[0] = ["def_statement", p[2], p[4], p[8][1] ]


    # ---------------------------------------------------------------------
    # Expressions : literals, functional calls
    # TBD: infix expressions
    # ---------------------------------------------------------------------
    def p_expression_1(self,p):
        "expression : arith_expression"
        p[0] = ["expression", p[1] ]






    def p_expression_3(self,p):
        """expression : arith_expression TIMES expression
                      | arith_expression DIVIDE expression
                      | arith_expression POWER expression"""
        p[0] = ["infix_expression", p[2], p[1], p[3] ]

    def p_expression_4(self,p):
        """arith_expression : expression_atom"""
        p[0] = p[1]

    def p_expression_5(self,p):
        """arith_expression : expression_atom PLUS arith_expression
                            | expression_atom MINUS arith_expression"""
        p[0] = ["infix_expression", p[2], p[1],  p[3] ]

    # ---------------------------------------------------------------------
    # Literal Values : number, identifier, string
    #  TBD: boolean, real, array
    # ---------------------------------------------------------------------

    def p_expressionatom_1(self,p):
        "expression_atom : number"
        p[0] = ["literalvalue", p[1] ]

    def p_expressionatom_2(self,p):
        "expression_atom : identifier"
        p[0] = ["literalvalue", p[1] ]

    def p_expressionatom_3(self,p):
        "expression_atom : string"
        p[0] = ["literalvalue", p[1] ]

    def p_expressionatom_4(self,p):
        "expression_atom : boolean"
        p[0] = ["literalvalue", p[1] ]

    def p_expressionatom_5(self,p):
        "expression_atom : func_call"
        p[0] = ["expression", p[1] ]

    #def p_expression_2(self,p):
    def p_expressionatom_6(self,p):
        "expression_atom : PARENL fullexpression PARENR"
        p[0] = p[2]


    def p_func_call1(self,p):
        "func_call : IDENTIFIER PARENL PARENR"
        p[0] = ["func_call", p[1] ]

    def p_func_call2(self,p):
        "func_call : IDENTIFIER PARENL expr_list PARENR"
        p[0] = ["func_call", p[1], p[3] ]

    def p_number_1(self,p):
        "number : NUMBER"
        p[0] = ["number", p[1] ]

    def p_number_2(self,p):
        "number : MINUS number"
        p[0] = ["number", -p[2][1] ]

    def p_string_1(self,p):
        "string : STRING"
        p[0] = ["string", p[1] ]

    #def p_string_2(self,p):
        #"string : STRING STRING"
        #p[0] = ["string", p[1]+p[2] ]

    def p_boolean(self,p):
        """boolean : TRUE
                   | FALSE"""
        p[0] = ["boolean", p[1] ]

    def p_identifier(self,p):
        "identifier : IDENTIFIER"
        p[0] = ["identifier", p[1] ]

    # ------------------------------
    # FIXME: these lists are currently nested, they'd be better flattened
    # FIXME: These should probably be "fullexpression"s
    def p_expr_list1(self,p):
        "expr_list : expression "
        p[0] = ["expr_list", p[1] ]

    def p_expr_list2(self,p):
        "expr_list : expression COMMA expr_list"
        p[0] = ["expr_list", p[1], p[3] ]

    def p_ident_list1(self,p):
        "ident_list : identifier"
        p[0] = ["ident_list", p[1] ]

    def p_ident_list2(self,p):
        "ident_list : identifier COMMA ident_list"
        p[0] = ["ident_list", p[1], p[3] ]

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
    global lexer
    lexer =  lex.lex(reflags=re.MULTILINE)
    lexer.curr_spaces_indent = 0

    lexer.indentation_stack = []
    lexer.indentation_stack.append(lexer.curr_spaces_indent)

    def trace(lexer, *argv):
        token = lexer.token_()
        if not quiet_mode:
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
