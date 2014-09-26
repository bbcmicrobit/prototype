#!/usr/bin/env python
#
# Simple experiment to build a parser capable of handling
# non-hinted semantic whitespace using ply
#
# Uses the PLY parsing toolkit from:
#            http://systems.cs.uchicago.edu/ply/
#
"""
Changelog: 1.5-1.6
   * Removed tokens INDENTLEVEL and SPACE. Their functions
     are subsumed into BLOCKSTART
   * Added token FUNCID. This needs more work, but this is needed
     to disambiguate the grammar between normal IDs and standard
     IDs. This may or may not work as required. (Beginning to think
     it'll fail badly. Works fine for builtins, but the question is
     how do we use the _results_ of parsing to parse the document?
     Will a backchannel when we recognise a function work? Doesn't
     this also mean that we gain semantic problems?)
   * Added trivial (naff) error handling
   * Improved block end handling
   * Made tracking of number of tokens forwarded better
   * Created code to allow blank lines to be skipped. (Currently
     commented out)
"""
import ply.lex as lex
# import lex
indent = 0

tokens = (
   "NUMBER",
   "STRING",
   "BLOCKSTART",
   "BLOCKEND",
   "IGNORE",
   "ID",
   "ASSIGNMENT",
   "COLON",
   "COMMA",
   "INFIXOPERATOR",
   "EOL",
   "BRA",
   "KET",
   "BRA2",
   "KET2",
   "BRA3",
   "KET3",
   "DOT",
   )
Tokens = [ x for x in tokens if "IGNORE" not in x ]
 
indentLevels = []

# A string containing ignored characters (tabs and newlines)
t_ignore  = '\t'
#
# First we define rules & (simple) actions
#
t_BRA2 = r'\['
t_KET2 = r'\]'
t_BRA3 = r'\{'
t_KET3 = r'\}'
#t_END = r'end'

#t_SPACE = r'\s+'

t_BRA = r'\('
t_KET = r'\)'
t_DOT = r'\.'
t_COMMA = r'\,'
t_COLON = r':'
t_ASSIGNMENT = r'=|[+\-*/|$%^&_~\\`<>:]='

t_IGNORE = r'(\s+|\#.*$)'

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

t_INFIXOPERATOR = r'\->|[+\-*/|!$%^&_~\\`<>]{1,2}|=>|==|<\-|=<|\.\.|::|<>|!='
def t_ID(t):
   r"[']*[@&$%A-Za-z_][A-Za-z_0-9]*[']*"
   return t

def t_BLOCKSTART(t):
    r'^\s+'
    global indent,indentLevels
    if len(t.value) > indent:
       t.type = 'BLOCKSTART'
       indent = len(t.value)
       indentLevels.append(indent)
       t.value=len(t.value)
    elif len(t.value) < indent:
       currindent = indent
       indent = len(t.value)
       t.value = 0
       currindent = indentLevels[-1]
       indentLevels = indentLevels[:-1]

       while currindent >indent:
          currindent = indentLevels[-1]
          indentLevels = indentLevels[:-1]
          t.value +=1
       t.value = t.value - 1
       indentLevels.append(indent)
       t.type = 'BLOCKEND'
    else:
       t.type = 'IGNORE'
       t.value=len(t.value) # Indent level
    return t

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

import re
# Then we build the lexer
lex.lex(reflags=re.MULTILINE)

#
# The lexer normally operates on full strings. Often however we deal with
# whole lines, so we repeatedly pass whole lines to the lexer, and logically
# join the results for parsing onto a grammar handler.
#
# In the case of handling semantic whitespace, the trickiest part is how to
# handle an indent level of 0. The approach this lexer takes is to look at
# the first lex'd token, and check to see if it relates to indentation. If it
# doesn't then we've switched to indent level 0, so we need to create an
# extra token for insertion into the token stream which indicates end of
# block
#

def newToken(toktype, value, lineno):
   newtok = lex.LexToken()
   newtok.type = toktype
   newtok.value = value
   newtok.lineno = lineno
   newtok.lexpos = lineno
   return newtok

import copy
class myLexer:
   def __init__(self,source,trace=False):
      self.gen = self.tokeniser()
      self.lineno = 0
      self.source = source
      self.trace = trace

   def token(self):
      try:
         return self.gen.next()
      except StopIteration:
         return

   def tokeniser(self):
      for i in self.tokeniser_():  
         if self.trace:
            print i
         yield i

   def tokeniser_(self):
      global indent,indentLevels
      yield newToken("BLOCKSTART", 0, self.lineno)
      self.lineno = 0
      for line in self.source:
         # Give it to the lexer!
         lex.input(line)
         self.lineno += 1
         t = 0 # Every line, reset the token count
         tseen = 0 # Every line, reset the token count
         tlist = []
         while 1:
             tok = lex.token()
             try:
                toktype = tok.type
             except AttributeError:
                toktype = None
             if toktype is "BLOCKEND":
                for i in xrange(tok.value):
                   X=newToken("BLOCKEND", (-1*i)-1, self.lineno)
                   tlist.append(X)
                   t += 1
                   yield newToken("BLOCKEND", (-1*i)-1, self.lineno)
             elif (tseen == 0 and
                   indent !=0 and
                   toktype not in ["BLOCKSTART", "IGNORE" ]) :
                "We're switching back to indent level 0 from non-zero."
                "We need to reinsert the right number of end blocks"
                currindent = indentLevels[-1]
                indentLevels = indentLevels[:-1]
                blocks = 0
                indent = 0
                while currindent >indent and len(indentLevels)>0:
                   currindent = indentLevels[-1]
                   indentLevels = indentLevels[:-1]
                   blocks +=1
                for i in xrange(0,blocks):
                   X=newToken("BLOCKEND", -10+blocks, self.lineno)
                   tlist.append(X)
                   t += 1
                   yield newToken("BLOCKEND", -10+blocks, self.lineno)
                X=newToken("BLOCKEND", -10+blocks, self.lineno)
                tlist.append(X)
                t += 1
                yield newToken("BLOCKEND", -10+blocks, self.lineno)
                indent = 0

             tseen += 1
             if not tok: break      # No more input on this line
             # Don't forward IGNORE indentation levels
             if toktype != "IGNORE" and tok is not None:#and tok.type != "SPACE" :
                tok.lineno = self.lineno
                tlist.append(tok)
                t += 1
                yield tok

         if len(tlist) >0:
            yield newToken("EOL", 0, self.lineno)

      yield newToken("BLOCKEND", 0, self.lineno)

if __name__ == "__main__":
   source = """
print hello world
""".split("\n")
   lexer=myLexer(source)
   for t in lexer.tokeniser(): 
      print t
