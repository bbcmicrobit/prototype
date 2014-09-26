#
# Sample logo like language using the parser
#

shape square:
   pen down
   repeat 4:
      forward 10
      rotate 90
   end
   pen up
end

repeat (360/5):
   square()
   rotate 5
end
