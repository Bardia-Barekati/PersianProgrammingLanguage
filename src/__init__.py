from sys import path, argv

path.append("../libs")

from lexer import PPLLexer
from parser import PPLParser
from execute import PPLExecute

if __name__ == '__main__':
	lexer = PPLLexer()
	parser = PPLParser()
	env = {}
	if len(argv) < 2:
		print('you must send a file name as an argument')
	with open(argv[1]) as f:
		for line in f.read().splitlines():
			tokens = lexer.tokenize(line)
			tree = parser.parse(tokens)
			PPLExecute(tree, env)
