# This isn't really real, it hopefully LOOKS it though!
#
# This is a direct translation/snapshot of the current parser code
# into something parsable by the parser.
#
# Simple experiment to build a parser capable of handling
# non-hinted semantic whitespace using ply
#
# Uses the PLY parsing toolkit from:
#            http://systems.cs.uchicago.edu/ply/
#

from Lexer import myLexer # ,tokens
from types import ModuleType
r={}
import yacc,sys
parse = 1

class Grammar(object):
   from Lexer import Tokens as tokens
   precedence = ( ( "left", "DOT"))
   def p_error(self,p):
      print "Syntax error at", p
   end
   def p_program(self,p):
      "program : block"
      p[0] = {"program", p[1] }
   end
   def p_block_1(self,p):
      "block : BLOCKSTART statement_list BLOCKEND"
      p[0] = {"block", p[2] }
   end
   def p_block_2(self,p):
      "block : BLOCKSTART BLOCKEND"
      p[0] = {"block", {} }
   end
   def p_statement_list_1(self,p):
      "statement_list : statement statement_list"
      p[0] = {"statement_list", p[1], p[2] }
   end
   def p_statement_list_2(self,p):
      "statement_list : statement"
      p[0] = {"statement_list", p[1] }
   end
   def p_statement_1(self,p):
      "statement : EOL"
      p[0] = {"nullstatement", None}
   end
   def p_statement_2(self,p):
      "statement : expression EOL"
      p[0] = {"exprstatement", p[1]}
   end
   def p_statement_3(self,p):
      "statement : expression ASSIGNMENT expression EOL"
      p[0] = {"assignment", p[1],p[3]}
   end
   def p_expression_1(self,p):
      "expression : factor"
      p[0] = {"expression", p[1]}
   end
   def p_expression_1a(self,p):
      "expression : factor factorlist"
      p[0] = {"functioncall", p[1],p[2]}
   end
   def p_factorlist_1a(self,p):
      "factorlist : factor"
      p[0] = {"factorlist", p[1]}
   end
   def p_factorlist_1b(self,p):
      "factorlist : factorlist factor"
      p[0] = {"factorlist", p[1],p[2]}
   end
   def p_expression_2(self,p):
      "expression : expression INFIXOPERATOR factor"
      p[0] = {"infixepr", p[2],p[1],p[3]}
   end
   def p_expression_1b(self,p):
      "factor : bracketedexpression"
      p[0] = {"bracketedexpression", p[1]}
   end
   def p_expression_1c(self,p):
      "factor : constructorexpression"
      p[0] = {"constructorexpression", p[1]}
   end
   def p_factor_1(self,p):
      "factor : NUMBER"
      p[0] = {"number", p[1]}
   end
   def p_factor_2(self,p):
      "factor : STRING"
      p[0] = {"string", p[1]}
   end
   def p_factor_3(self,p):
      "factor : ID"
      p[0] = {"ID", p[1]}
   end
   def p_factor_3a(self,p):
      "factor : factor dotexpression"
      p[0] = {"dottedfactor", p[1],p[2]}
   end
   def p_dotexpression_1(self,p):
      "dotexpression : DOT ID bracketedexpression"
      p[0] = {"methodcall", p[2],p[3]}
   end
   def p_dotexpression_2(self,p):
      "dotexpression : DOT ID"
      p[0] = {"attribute", p[2]}
   end
   def p_bracketedexpression_1(self,p):
      "bracketedexpression : BRA expression KET"
      p[0] = {"bracketedexpression", p[2]}
   end
   def p_bracketedexpression_2(self,p):
      "bracketedexpression : BRA KET"
      p[0] = {"bracketedexpression", None }
   end
   def p_constructorexpression_1(self,p):
      "constructorexpression : BRA3 KET3"
      p[0] = {"constructorexpression", None }
   end
   def p_constructorexpression_2(self,p):
      "constructorexpression : BRA3 expression KET3"
      p[0] = {"constructorexpression", p[2] }
   end
   def p_factor_7(self,p):
      "factor : factor trailer"
      p[0] = {"trailedfactor", p[1],p[2]}
   end
   def p_factor_8(self,p):
      "factor : factor trailertoo"
      p[0] = {"trailedfactor", p[1],p[2]}
   end
   def p_trailer_1(self,p):
      "trailer : BRA2 expression KET2"
      p[0] = {"bracketedtrailer", p[2]}
   end
   def p_trailer_2(self,p):
      "trailertoo : COLON EOL block"
      p[0] = {"blocktrailer", p[3]}
   end
end

def parse(source,lexer):
   yacc.yacc(module => (Grammer None) )
   result = yacc.parse(lexer => lexer)
   return result
end

def displayResult(result,quiet):
   if not quiet:
      print "The result of parsing your program:"
      print result
      print
      if not result:
         print "Rule match/evaluation order"
         for rule in r:
            print "   ", rule
         end
      end
   else:
      if result is None:
         print "Parse failed"
      else:
         print "Success"
      end
   end
end

def run(source, lexonly=>False,trace=>False,quiet=>False):
   sourceLines=source.split("\n")
   lexer=myLexer(sourceLines,trace)
   if lexonly:
      for t in lexer.tokeniser():
         print t
      end
   else:
      displayResult(parse(source=>sourceLines, lexer=>lexer),quiet)
   end
end
