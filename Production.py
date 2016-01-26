"""

A := a b c

Following production is 
B := a b c | d e f

"""

from Symbol import Symbol

class Production(object):
	def __init__(self, non_terminal, production, grammar):
		super(Production, self).__init__()
		self.non_terminal = non_terminal
		self.production = production
		self.dot = 0
		self.is_terminal = True
		self.grammar = grammar

	def next_symbol(self):
		if self.dot < len(self.production):
			return self.production[self.dot]

	def increment_dot(self):
		self.dot += 1

	@staticmethod
	def get(str_productions, grammar):
		left, right = str_productions.split(":=")
		left = left.strip()
		productions_split = right.split("|")
		productions = []
		for str_production in productions_split:
			# productions.append([Symbol(symbol) for symbol in str_production.strip().split(" ")])
			q = []
			for symbol in str_production.strip().split(" "):
				if symbol != "E":
					q.append(Symbol(symbol, grammar))
			productions.append(q)

		return [Production(left, production, grammar) for production in productions]

	def __str__(self):
		r = ""
		i = 0
		for s in self.production:
			if i == self.dot:
				r += ". "
			r += "%s " %(s.symbol)
			i += 1
		if i == self.dot:
			r += "."

		return self.non_terminal + " := " + r

	def is_next_terminal(self):
		return self.next_symbol().is_terminal() if self.next_symbol() else None

def main():
	# ps = Production.get("B := a b c | d e f | x B")
	# ps = Production.get("B := a b c | d e f | x B")
	ps = Production.get("B := a b c | d e f | E", None)
	# ps = Production.get("S' := S")
	for p in ps:
		print p

if __name__ == '__main__':
	main()
