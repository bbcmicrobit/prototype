#
# This example file is representative of the sort of thing
# you might get in an SML-like language using this parser.
#
# Clearly this parser doesn't add any semantics to this, but
# the following *is* valid syntax.
#
structure Stk = struct :
   exception EmptyStack_exception
   datatype 'x stack = EmptyStack | push of ('x * 'x stack)
   fun pop(push(x,y)) = y
   fun pop EmptyStack = raise EmptyStack_exception
   fun top(push(x,y)) = x
   fun top EmptyStack = raise EmptyStack_exception
end

let:
   # This really would be pretty naff in reality, but this is intended to be suggestive
   val x = EmptyStack
   val x = push(5,x)
   val x = push(4,x)
   val x = push(3,x)
   val x = push(2,x)
in:
   top x
   val x = pop x
   top x
   val x = pop x
   top x
   val x = pop x
   top x
end
