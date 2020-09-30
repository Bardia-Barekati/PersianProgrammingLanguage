class PPLExecute(object):
	def __init__(self, tree, env):
		self.env = env
		result = self.walk_tree(tree)
		if result is not None and isinstance(result, int):
			print(result)
		if isinstance(result, str) and result[0] == '"':
			print(result)

	def walk_tree(self, node):
		if isinstance(node, int) or isinstance(node, str) or node is None:
			return node
		if node[0] in [ 'num', 'str' ]:
			return node[1]
		if node[0] == 'raw_input':
			return '"' + input() + '"'
		if node[0] == 'num_input':
			try:
				return int(input())
			except TypeError:
				return 0
		if node[0] == 'if_stmt':
			result = self.walk_tree(node[1])
			if result:
				return self.walk_tree(node[2])
			if node[3]:
				return self.walk_tree(node[3])
		if node[0] == 'condition_eqeq':
			return self.walk_tree(node[1]) == self.walk_tree(node[2])
		if node[0] == 'condition_shomarande':
			return self.walk_tree(node[2]) % self.walk_tree(node[1]) == 0
		if node[0] == 'fun_def':
			self.env[node[1]] = node[2]
		if node[0] == 'fun_call':
			try:
				return self.walk_tree(self.env[node[1]])
			except LookupError:
				print('undefined function \'%s\'' % node[1])
				return 0
		if node[0] == 'addstr':
			return str(self.walk_tree(node[1])) + str(self.walk_tree(node[2]))
		elif node[0] == 'add':
			try:
				return int(self.walk_tree(node[1])) + int(self.walk_tree(node[2]))
			except TypeError:
				return 0
		elif node[0] == 'sub':
			try:
				return int(self.walk_tree(node[1])) - int(self.walk_tree(node[2]))
			except TypeError:
				return 0
		elif node[0] == 'mul':
			try:
				return int(self.walk_tree(node[1])) * int(self.walk_tree(node[2]))
			except TypeError:
				return 0
		elif node[0] == 'div':
			try:
				return int(self.walk_tree(node[1])) // int(self.walk_tree(node[2]))
			except TypeError:
				return 0
		if node[0] == 'var_assign':
			self.env[node[1]] = self.walk_tree(node[2])
			return node[1]
		if node[0] == 'var':
			try:
				return self.env[node[1]]
			except LookupError:
				print('undefined variable \'%s\'' % node[1])
				return 0
		if node[0] == 'for_loop':
			if node[1][0] == 'for_loop_setup':
				loop_setup = self.walk_tree(node[1])
				loop_counter = self.env[loop_setup[0]]
				loop_limit = loop_setup[1]
				for i in range(loop_counter, loop_limit + 1):
					self.env[loop_setup[0]] = i
					res = self.walk_tree(node[2])
					if res is not None:
						print(res)
		if node[0] == 'for_loop_setup':
			return (self.walk_tree(node[1]), self.walk_tree(node[2]))
