#
# Example based on defining grammars for L-Systems. 
#
# This example defines a representation of a biological tree
# using a stochastic L system.
# G defines a simple stem with a few leaves.
# T defines a "tunnel" - a stem without leaves
# F defines a "flat" - a leaf
#
# A, B and C are all defined as rotations.
#
#
OBJECT tree L_SYSTEM:
  ROOT  G
  RULES:
      G -> T { G } { A G } { B G } { C G } (0.00 .. 0.15)
      G -> T { A B G } { B A G } { C A G } (0.15 .. 0.30)
      G -> T { A C G } { B B G } { C B G } (0.30 .. 0.45)
      G -> T { A A G } { B C G } { C C G } (0.45 .. 0.60)
      G -> T { A G } { C G }         (0.70 .. 0.80)
      G -> T { A G } { B G }         (0.80 .. 0.95)
      G -> T { A G }                 (0.95 .. 1.00)
      T -> T                         (0.00 .. 0.75)
      T -> T { A F } { B F } { C F } (0.75 .. 1.00)
      F -> G                         (0.00 .. 0.50)
      F -> { A G } { B G } { B G }   (0.50 .. 1.00)
  ENDRULES
ENDOBJECT
