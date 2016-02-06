'''

SLR PARSING

'''

from Grammar import Grammar
from Goto import GotoGenerator
from ParsingTable import Table
from LR_Parser import LR_Parser

grammar = """
S' := S
S := A c A
S := B c c B
A := c A
A := a
B := c c B
B := b
"""

input = "a c c a"

grammar = """
S' := S
S := q A B C
A := a | b b D
B := a | E
C := b | E
D := C | E
"""
input = "q a a b"


# grammar = """
# # S' := S
# # S := q A B C
# # A := B b b D
# # B := C | E
# # C := b | E
# # D := C | E
# # """


# grammar = """
# S' := S
# S := L = R
# S := R
# L := * R
# L := id
# R := L
# """


# input = "a a b b a a b b"
# input = "q a b"

def main():
  global input, grammar

  g = Grammar(grammar)
  g.parse()
  gotos = GotoGenerator(g)
  gotos.generate()
  gotos.display()

  g.first_follow.display()

  parsing_table = Table(g, gotos)
  parsing_table.generate()

  lr_parser = LR_Parser(g, parsing_table, input)
  lr_parser.parse()

  # print parsingTable.get("5", "$")

if __name__ == '__main__':
  main()
