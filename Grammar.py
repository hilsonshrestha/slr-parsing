'''
Grammar class

Note: Make sure that each word in raw is separated by a space

'''

from Production import Production

class Grammar(object):
	def __init__(self, raw):
		self.raw = raw #.replace(" ", "")
		self.grammar = []
		self.non_terminals = []
		root = False
		for line in self.raw.split("\n"):
			if line.find(":=") < 0: continue
			# print line
			ps = Production.get(line, self)
			for p in ps:
				self.grammar.append(p) 
				if p.non_terminal not in self.non_terminals:
					self.non_terminals.append(p.non_terminal)
				# print p		
		# print "==="
		# print self.non_terminals

		# for production in self.grammar:
		# 	if production.non_terminal in self.non_terminals:
		# 		production.is_terminal = False

	def __str__(self):
		return str(self.grammar)


