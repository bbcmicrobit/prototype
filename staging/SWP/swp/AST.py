#!/usr/bin/env python

import ASTWalkers

class _node(object):
   def __init__(self, *children):
      self.children = children[:]
      try:
         self.walkerClass = eval("ASTWalkers."+str(self.__class__).split(".")[1][:-2]+"_WALKER")
      except AttributeError:
         self.walkerClass = ASTWalkers._node_WALKER
      self.walker = self.walkerClass(self)
   def __repr__(self):
      return str(self.__class__).split(".")[1][:-2]+"("+", ".join([str(X) for X in self.children])+")"

class program(_node): pass
class block(_node): pass
class statementlist(list): pass
class statement(_node): pass
class expressionlist(list): pass
class simple_expression(_node): pass
class funccall(_node): pass
class infixexpression(_node): pass
class factorlist(list): pass
class factor(_node): pass
class number(factor): pass
class string(factor): pass
class id(factor): pass
class trailedfactor(factor): pass
class subexpression(_node): pass
class constructor(_node): pass
class trailer(_node): pass
class dotexpression(trailer): pass
class methodtrailer(dotexpression): pass
class dotfactortrailer(dotexpression): pass
class exprtrailer(trailer): pass
class blocktrailer(trailer): pass


class node_list(_node): pass

def node_join(node1, node2):
   X = list(node1.children)
   X.extend(list(node2.children))
   return node1.__class__(*X)

def node_append(node1, node2):
   X = list(node1.children)
   X.append(node2)
   return node1.__class__(*X)

if __name__ == "__main__":
   X=_node('hello', 'world')
   Y=block(_node('this',), _node('that',), _node('the', 'other'))

   assert str(X)=="_node('hello', 'world')"
   assert str(Y)=="block(_node('this',), _node('that',), _node('the', 'other'))"

   X=statement_list(1,2,3)
   print X
   Y=statement_list(4,5,6)
   print Y
   print "Y is X,",Y is X
   Z = node_join(X,Y)
   print "Z, ", Z

   X=statement_list()
   Y1=statement("stat1")
   Y2=statement("stat1")
   Y3=statement("stat1")
   X= node_append(X,Y1)
   X= node_append(X,Y2)
   X= node_append(X,Y3)
   print "APPENDED", X

"""
class program(_node): pass
#     program -> block

class block(_node): pass
#     block -> BLOCKSTART statement_list BLOCKEND
#     block -> BLOCKSTART BLOCKEND

class statementlist(list): pass
#     statement_list -> statement statement_list
#     statement_list -> statement

class statement(_node): pass
#     statement -> EOL
#     statement -> expression EOL
#     statement -> expression ASSIGNMENT expression EOL

class expressionlist(list): pass
#     expression -> oldexpression COMMA expression
#     expression -> oldexpression

class simple_expression(_node): pass
#     oldexpression -> factor
class funccall(_node): pass
#     oldexpression -> factor factorlist
class infixexpression(_node): pass
#     oldexpression -> factor INFIXOPERATOR expression

class factorlist(list): pass
#     factorlist -> factor
#     factorlist -> factorlist factor

class factor(_node): pass
#     factor -> bracketedexpression
#     factor -> constructorexpression

class number(factor): pass
#     factor -> NUMBER
class string(factor): pass
#     factor -> STRING
class id(factor): pass
#     factor -> ID

class trailedfactor(factor): pass
# factor -> factor DOT dotexpression          
# factor -> factor trailer
# factor -> factor trailertoo

class subexpression(_node): pass
# bracketedexpression -> BRA expression KET
# bracketedexpression -> BRA KET

class constructor(_node): pass
# constructorexpression -> BRA3 KET3
# constructorexpression -> BRA3 expression KET3

class trailer(_node): pass
class dotexpression(trailer): pass
class methodtrailer(dotexpression): pass
# dotexpression -> ID bracketedexpression

class dotfactortrailer(dotexpression): pass
# dotexpression -> factor

class exprtrailer(trailer): pass
# trailer -> BRA2 expression KET2

class blocktrailer(trailer): pass
# trailertoo -> COLON EOL block
"""
