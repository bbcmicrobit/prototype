#!/usr/bin/env python
#
# Simple experiment to build a parser capable of handling
# non-hinted semantic whitespace using ply
#
# Uses the PLY parsing toolkit from:
#            http://systems.cs.uchicago.edu/ply/
#

from Lexer import myLexer # ,tokens
from types import ModuleType
r=[]

import sys
import ply.yacc as yacc
# import yacc
parse = 1

class Grammar(object):
   from Lexer import Tokens as tokens
   precedence = (
      ( 'right',"COMMA"),
      ( 'left', "BRA","DOT","BRA2","COLON"), # Hmm...
   )

   def p_error(self,p):
      print "Syntax error at", p

   def p_program(self,p):
      "program : block"
      p[0] = ["program", p[1] ]

   def p_block_1(self,p):
      "block : BLOCKSTART statement_list BLOCKEND";
      p[0] = ["block", p[2] ]

   def p_block_2(self,p):
      "block : BLOCKSTART BLOCKEND"
      p[0] = ["block", [] ]

   def p_statement_list_1(self,p):
      "statement_list : statement statement_list"
      p[0] = ["statement_list", p[1], p[2] ]

   def p_statement_list_2(self,p):
      "statement_list : statement"
      p[0] = ["statement_list", p[1] ]

   def p_statement_1(self,p):
      "statement : EOL"
      p[0] = ["nullstatement", None]

   def p_statement_2(self,p):
      "statement : expression EOL"
      p[0] = ["exprstatement", p[1]]

   def p_statement_3(self,p):
      "statement : expression ASSIGNMENT expression EOL"
      p[0] = ["assignment", p[2], p[1],p[3]] # Assignment op might be interesting...

   def p_expression_2(self,p):
      "expression : oldexpression COMMA expression"
      p[0] = ["explist", p[1],p[3]]

   def p_expression_2list_1(self,p):
      "expression : BRA2 expression KET2"
      p[0] = ["explist", p[2]]

   def p_expression_2list_2(self,p):
      "expression : BRA2 KET2"
      p[0] = ["explist", None]

   def p_expression_2a(self,p):
      "expression : oldexpression"
      p[0] = ["explist", p[1]]

   def p_expression_2b(self,p):
      "oldexpression : factor INFIXOPERATOR expression"
      p[0] = ["infixepr", p[2],p[1],p[3]]

   def p_expression_2c(self,p):
      "oldexpression : factor COLON expression"
      p[0] = ["colonepr",p[1],p[3]]

   def p_expression_1a(self,p):
      "oldexpression : factorlist"
      p[0] = ["oldexpression", p[1]]

   def p_factorlist_1b(self,p):
      "factorlist : factor factorlist"
      p[0] = ["factorlist", p[1],p[2]]

   def p_factorlist_1a(self,p):
      "factorlist : factor"
      p[0] = ["factorlist", p[1]]

   def p_factoid(self,p):
      "factor : factoid"
      p[0] = ["factor", p[1]]

   def p_factor_3a(self,p):
      "factor : factoid dotexpression"
      p[0] = ["dottedfactor", p[1],p[2]]

   def p_expression_1b(self,p):
      "factoid : bracketedexpression"
      p[0] = ["bracketedexpression", p[1]]

   def p_expression_1c(self,p):
      "factoid : constructorexpression"
      p[0] = ["constructorexpression", p[1]]

   def p_factor_1(self,p):
      "factoid : NUMBER"
      p[0] = ["number", p[1]]

   def p_factor_2(self,p):
      "factoid : STRING"
      p[0] = ["string", p[1]]

   def p_factor_3(self,p):
      "factoid : ID"
      p[0] = ["ID", p[1]]

   def p_factor_7(self,p):
      "factoid : factor trailer"
      p[0] = ["trailedfactor", p[1],p[2]]

   def p_factor_8(self,p):
      "factoid : factor trailertoo"
      p[0] = ["trailedfactor", p[1],p[2]]

   def p_dotexpression_2(self,p):
      "dotexpression : DOT factor"
      p[0] = ["dottedfactor", p[2]]   # Used for attributes *and* floats

   def p_bracketedexpression_1(self,p):
      "bracketedexpression : BRA expression KET"
      p[0] = ["bracketedexpression", p[2]]

   def p_bracketedexpression_2(self,p):
      "bracketedexpression : BRA KET"
      p[0] = ["bracketedexpression", None ]

   def p_constructorexpression_1(self,p):
      "constructorexpression : BRA3 KET3"
      p[0] = ["constructorexpression", None ]

   def p_constructorexpression_2(self,p):
      "constructorexpression : BRA3 expression KET3"
      p[0] = ["constructorexpression", p[2] ]

   def p_trailer_1(self,p):
      "trailer : BRA2 expression KET2"
      p[0] = ["bracketedtrailer", p[2]]

   def p_trailer_2(self,p):
      "trailertoo : COLON EOL block"
      p[0] = ["blocktrailer", p[3]]

def parse(source,lexer):
   yacc.yacc(module=Grammar())
   result = yacc.parse(lexer=lexer)
   return result

def displayResult(result,quiet):
   if not quiet:
      print "The result of parsing your program:"
      print result
      print
      if not result:
         print "Rule match/evaluation order"
         for rule in r:
            print "   ", rule
   else:
      if result is None:
         print "Parse failed"
      else:
         print "Success"

def run(source, lexonly=False,trace=False,quiet=False):
   sourceLines=source.split("\n")
   lexer=myLexer(sourceLines,trace)
   if lexonly:
      for t in lexer.tokeniser(): 
         print t
   else:
      displayResult(parse(source=sourceLines, lexer=lexer),quiet)

if __name__ == "__main__":
   import sys
   lexonly=False
   trace=False
   quiet = False
   if sys.argv[1:]:
      source = open(sys.argv[1]).read()
   else:
      source = """
if (__name__ == "__main__"):
   import sys
   lexonly = False
   trace = False
   quiet = False
   if sys.argv[1:1]:  # HELLO World!
      source = (read (open sys.argv[1]))
   end
end

def myfunction [arg1=>2,arg1=>2,arg3=>3]:
   print "docstring"
   print "hello"
end

class token [object]:
   struct:
      type
      value
      lineno
   end
end

print "woot!"

"""
   try:
      if sys.argv[2]:
         if sys.argv[2]=="lexer":
            lexonly = True
         elif sys.argv[2]=="trace":
            trace = True
         elif sys.argv[2]=="quiet":
            quiet = True
   except IndexError:
      pass

   run(source,lexonly,trace,quiet)
