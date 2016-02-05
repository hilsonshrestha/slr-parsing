import copy
MAX_LOOP = 100

class LR_Parser(object):
	"""docstring for LR_Parser"""
	def __init__(self, parsing_table, input):
		super(LR_Parser, self).__init__()
		self.parsing_table = parsing_table
		self.input = input.split(" ")

		self.stack = [0,]
		self.display_stack = []

		self.display_action = []
		self.display_input = []

		self.display_input.append(copy.copy(self.input))

	def parse(self):
		loop = 0
		while (True):		
			try:
				action = self.parsing_table.get(self.stack[-1], self.input[0])
			except KeyError:
				print "invalid character ", self.input[0]
				return False

			self.display_action.append(action)
			# if action[0] == "S":
			# 	self.stack.append(self.input.pop(0))




			loop += 1
			if loop >= MAX_LOOP:
				print "Max loop reached."
				return False


		