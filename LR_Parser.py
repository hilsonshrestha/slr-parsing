import copy
MAX_LOOP = 100

class LR_Parser(object):
	"""docstring for LR_Parser"""
	def __init__(self, grammar, parsing_table, input):
		super(LR_Parser, self).__init__()
		self.grammar = grammar
		self.parsing_table = parsing_table
		self.input = input.split(" ")
		self.input.append("$")

		self.stack = [0,]
		self.display_stack = []

		self.display_action = []
		self.display_input = []

		# self.display_input.append(copy.copy(self.input))

	def parse(self):
		loop = 0
		final_loop = False
		while (True):
			try:
				action = list(self.parsing_table.get(self.stack[-1], self.input[0])["value"])[0]
			except KeyError:
				print "invalid character ", self.input[0]
				return False


			self.display_stack.append(copy.copy(self.stack))
			self.display_input.append(copy.copy(self.input))
			self.display_action.append(action)
			# print final_loop
			if final_loop:
				break

			if action[0] == "S":
				self.stack.append(self.input.pop(0))
				self.stack.append(action[1:])
			if action[0] == "R":
				production = self.grammar.grammar[int(action[1:]) - 1]
				# print production
				idx = int(action[1:]) - 1
				length = len(production.production)
				self.stack =  self.stack[:-2 * length]
				self.stack.append(production.non_terminal)
				self.stack.append(list(self.parsing_table.get(self.stack[-2], self.stack[-1])["value"])[0])
				if list(self.parsing_table.get(self.stack[-1], self.input[0])["value"])[0] == "R1":
					# statement is valid.
					final_loop = True
				# print self.stack

			loop += 1
			if loop >= MAX_LOOP:
				print "Max loop reached."
				break


		def list_to_str(l):
			r = ""
			for x in l:
				r += str(x) + " "
			return r	

		# Actual display of table.
		print "\n ## String checking using stack\n"
		for i, stack in enumerate(self.display_stack):
			print "%3d | %-30s | %-30s | %-10s" %\
			(i, list_to_str(stack), list_to_str(self.display_input[i]), self.display_action[i])

		