class Symbol(object):
	def __init__(self, symbol, grammar):
		self.symbol = symbol.strip()
		self.grammar = grammar
		self.terminal = None

	def is_terminal(self):
		if self.terminal == None:
			self.terminal = self.symbol not in self.grammar.non_terminals
		# print self.symbol, self.terminal
		return self.terminal

	def __str__(self):
		return self.symbol

	def __eq__(self, other):
		if isinstance(other, Symbol) and other.symbol == self.symbol:
			return True
		elif isinstance(other, int) and other == self.symbol:
			return True
		return False