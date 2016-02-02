"""
table = {
	"0c" : "r5"
	"0S" : "1"
}
"""
class Table(object):
	"""Table"""
	def __init__(self, grammar, gotos, terminals, non_terminals, states):
		super(Table, self).__init__()
		self.grammar = grammar
		self.gotos = gotos
		self.terminals = terminals
		self.non_terminals = non_terminals

		# Total number of states (total gotos)
		self.states = states
		self.table = {}
		# self.action = [[None] * (terminals)] * states
		# self.goto = [[None] * (non_terminals)] * states

	def fillTable(self):
		pass

	def key(self, state, action):
		return str(state) + str(action)

	def insert(self, state, action, value):
		self.table[self.key(state, action)] = value


		