#!/usr/bin/env python

storage = {}

_debug = 0
class _node_WALKER:
   def __init__(self,node):
      if _debug: print "Woo!", self.__class__, node
      self.node = node

   def evaluate(self): raise NotImplementedError,self.node

class PROGRAM_WALKER(_node_WALKER):
   def evaluate(self):
      for child in self.node.children:
          child.walker.evaluate()
      print "SCOPES", storage
      return None

class assignmentstatement_WALKER(_node_WALKER):
   def evaluate(self):
      kidnode = self.node.children[1]
      kidValue = kidnode.walker.evaluate()
      storage[self.node.children[0]] = kidValue
      return None

class NUMBER_WALKER(_node_WALKER):
   def evaluate(self):
      return self.node.children[0]

class STRING_WALKER(_node_WALKER):
   def evaluate(self):
      return self.node.children[0]

class statement_WALKER(_node_WALKER):
   def evaluate(self):
      try:
         return self.node.children[0].walker.evaluate()
      except IndexError:
         return None

class OP_WALKER(_node_WALKER):
   def evaluate(self):
      kv1 = self.node.children[1].walker.evaluate()
      kv2 = self.node.children[2].walker.evaluate()
      op = self.node.children[0]
      if op == "+": return kv2 + kv1
      if op == "-": return kv1 - kv2
      if op == "*": return kv1 * kv2
      if op == "/": return kv1 / kv2
      return None

class ID_WALKER(_node_WALKER):
   def evaluate(self):
      scopes = [storage, builtin.functions ]
      for scope in scopes:
         try: # First try the storage scope
            return scope[self.node.children[0]]
         except KeyError:
            pass

class funccall_WALKER(_node_WALKER):
   def evaluate(self):
      #print "funccall_WALKER"
      #print "kids", self.node.children
      values=[X.walker.evaluate() for X in self.node.children]
      #print "values", values
      #print self.node.children[0].walker.evaluate()
      func = values[0]
      del values[0]
      return func(*values)

class builtin(object):
   def Print(*args):
      for i in args:
         print i,
      print
   Print=staticmethod(Print)

   def Str(*args):
      r=[]
      for i in args:
         r.append(str(i))
      return "".join(r)
   Str=staticmethod(Str)

builtin.functions = {
   "print" : builtin.Print,
   "str" : builtin.Str,
}

