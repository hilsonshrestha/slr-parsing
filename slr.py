'''

SLR PARSING

'''

from Grammar import Grammar
from goto import GotoGenerator
grammar = """
S' := S
S := q A B C
A := a | b b D
B := a | E
C := b | E
D := C | E
"""
# grammar = """
# S' := S
# S := q A B C
# A := B b b D
# B := C | E
# C := b | E
# D := C | E
# """

input = "aabbaabb"



def main():
  global input, grammar

  g = Grammar(grammar)
  goto_1 = GotoGenerator(g)
  # goto_2 = Goto()

  # print g
  # parser = Parser(Grammar(grammar), input)

  # print parser
  # parser.parse()

if __name__ == '__main__':
  main()
