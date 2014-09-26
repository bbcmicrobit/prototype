class Grammar(Parser):
   def id(a,b):
      if 1:
         print "hi"
      end
   end
end

if (__name__ == "__main__"):
   import sys
   assign lexonly False
   assign trace False
   if sys.argv[1]:
      assign source open(sys.argv[1]).read()
   else:
      assign source "junk"
   end
end
