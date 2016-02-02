'''
Grammar class

Note: Make sure that each word in raw is separated by a space

January 27, 2016
'''

from Production import ProductionGenerator

class Grammar(object):
  def __init__(self, raw):
    # Raw grammar.
    self.raw = raw

    # Parsed grammar.
    self.grammar = []

    self.non_terminals = []
    self.terminals = []

  def parse(self):
    for line in self.raw.split("\n"):
      if line.find(":=") < 0: continue

      # Raw production may have splitter "|". So, it is split into multiple
      # productions to generate a list.
      ps = ProductionGenerator(line, self).generate()

      for p in ps:
        self.grammar.append(p)
        for symbol in p.production:
          if symbol.symbol not in self.terminals:
            self.terminals.append(symbol.symbol)
        if p.non_terminal not in self.non_terminals:
          self.non_terminals.append(p.non_terminal)
    
    for symbol in self.non_terminals:
      if symbol in self.terminals: self.terminals.remove(symbol)

  def __str__(self):
    r = ""
    for production in self.grammar:
      r += str(production) + "\n"
    return r
