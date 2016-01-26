import copy

epsila = "E"

class Goto(object):
	def __init__(self, productions, closure):
		self.productions = productions
		self.closure = colsure


class GotoGenerator(object):
	"""docstring for GotoGenerator"""
	def __init__(self, grammar):
		super(GotoGenerator, self).__init__()
		self.grammar = grammar
		self.gotos = []

		# create a goto sequence from given grammar.

		# first produce the symbol just after the dot.

		productions = self.grammar.grammar
		gotos_index = 0
		max = 30
		while True:
			symbol_after_dot = []

			for production in productions:
				print ">>>> " , production
				next_symbol = production.next_symbol()
				if next_symbol and next_symbol not in symbol_after_dot:
					symbol_after_dot.append(next_symbol)
			rr = "\n\n["
			for j in symbol_after_dot:
				rr += str(j) + " "
			print rr + "]"

			for symbol in symbol_after_dot:
				self.gotos.append(self.get_goto(productions, symbol))
				# print "goto with ", symbol, self.gotos[-1]
			if gotos_index >= len(self.gotos):
				break
			productions = self.gotos[gotos_index]
			gotos_index += 1
			if gotos_index > max:
				print "oopsie"
				break
		print gotos_index

		# print self.gotos[0][0]
		self.print_gotos()

	def get_goto(self, productions, symbol):
		r = []
		for production in productions:
			if production.next_symbol() == symbol:
				new_production = copy.copy(production)
				new_production.increment_dot()
				r.append(new_production)
				self.recursive_non_terminal_lookup(new_production, r)
		return r

	def recursive_non_terminal_lookup(self, given_production, r):
		a = []
		if given_production.is_next_terminal() == False:
			for production in self.grammar.grammar:
				if production.non_terminal == given_production.next_symbol().symbol:
					a.append(production)
					r.append(production)
		for production in a:
			self.recursive_non_terminal_lookup(production, r)

	def print_gotos(self):
		for productions in self.gotos:
			for production in productions:
				print production
			print "==="
		# for produc
		