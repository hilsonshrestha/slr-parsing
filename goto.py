import copy

epsila = "E"
MAX_LOOP = 30
class Goto(object):
	def __init__(self, productions, closure, parent_goto, id):
		self.productions = productions
		self.closure = closure
		self.parent_goto = parent_goto
		self.id = id

	def __eq__(self, other):
		# print "check", self.productions, other.productions
		if len(self.productions) != len(other.productions):
			return False
		for production in self.productions:
			if production not in other.productions:

				return False


		# for i, production in enumerate(self.productions):
		# 	if not (production == other.productions[i]) or production.dot != other.productions[i].dot:
		# 		# print "check", production, other.productions[i]
		# 		return False
		return True


class GotoGenerator(object):
	"""docstring for GotoGenerator"""
	def __init__(self, grammar):
		super(GotoGenerator, self).__init__()
		self.grammar = grammar
		self.gotos = []
		self.expected_id = 0

		# create a goto sequence from given grammar.

		# first produce the symbol just after the dot.

		productions = self.grammar.grammar
		gotos_index = 0
		parent_goto = 0
		prev_parent_goto = 0
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
				if parent_goto >= prev_parent_goto:
					new_goto = self.get_goto(productions, symbol, parent_goto)
					# if new_goto not in 
					self.gotos.append(new_goto)
				# print "goto with ", symbol, self.gotos[-1]
			if gotos_index >= len(self.gotos):
				break
			productions = self.gotos[gotos_index].productions
			if parent_goto >= prev_parent_goto:
				prev_parent_goto = parent_goto

			parent_goto = self.gotos[gotos_index].id
			gotos_index += 1
			if gotos_index > MAX_LOOP:
				print "oopsie"
				break
		print gotos_index

		# print self.gotos[0][0]
		self.print_gotos()

	def get_goto(self, productions, symbol, parent_goto):
		r = []
		for production in productions:
			if production.next_symbol() == symbol:
				new_production = copy.copy(production)
				new_production.increment_dot()
				r.append(new_production)
		for production in r:
			self.recursive_non_terminal_lookup(production, r)

		# check for duplicate goto
		self.expected_id += 1
		r_goto = Goto(r, symbol, parent_goto, self.expected_id)
		for goto in self.gotos:
			if r_goto == goto:
				r_goto.id = goto.id
				self.expected_id -= 1
				break
		return r_goto

	def recursive_non_terminal_lookup(self, given_production, r):
		a = []
		if given_production.is_next_terminal() == False:
			for production in self.grammar.grammar:
				if production.non_terminal == given_production.next_symbol().symbol:
					a.append(production)
					if production not in r:
						r.append(production)
		for production in a:
			self.recursive_non_terminal_lookup(production, r)

	def print_gotos(self):
		for goto in self.gotos:
			print "GOTO[" + str(goto.parent_goto) + ", " + str(goto.closure) + "] => " + str(goto.id)
			for production in goto.productions:
				print production
			print ""
		