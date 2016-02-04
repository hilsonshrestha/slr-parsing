'''

SLR PARSING

'''

from Grammar import Grammar
from Goto import GotoGenerator
from ParsingTable import Table
grammar = """
S' := S
S := A c A
S := B c c B
A := c A
A := a
B := c c B
B := b
"""


# grammar = """
# S' := S
# S := q A B C
# A := a | b b D
# B := a | E
# C := b | E
# D := C | E
# """


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
  g.parse()
  gotos = GotoGenerator(g)
  gotos.generate()
  gotos.display()

  g.first_follow.display()
  # goto_2 = Goto()

  parsingTable = Table(g, gotos)
  parsingTable.generate()

  # print g
  # parser = Parser(Grammar(grammar), input)

  # print parser
  # parser.parse()

if __name__ == '__main__':
  main()
