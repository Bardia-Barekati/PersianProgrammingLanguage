from sly import Lexer

class PPLLexer(Lexer):
	tokens = { RUN, RAW_INPUT, NUM_INPUT, EQEQ, SHOMARANDE, NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW }
	ignore = '\t '

	literals = { '=', '+', '-', '*', '/', '(', ')', ',', ';', '.' }

	# Define tokens
	IF = r'اگر'
	THEN = r'آنگاه'
	ELSE = r'وگرنه'
	FOR = r'برای'
	FUN = r'تابع'
	RUN = r'اجرای'
	TO = r'تا'
	ARROW = r'یعنی'
	EQEQ = r'برابر'
	SHOMARANDE = r'شمارنده'
	RAW_INPUT = r'ورودی'
	NUM_INPUT = r'عددگیر'
	NAME = r'[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]+'
	STRING = r'"(""|.)*?"'

	@_(r'\d+')
	def NUMBER(self, t):
		t.value = int(t.value)
		return t

	@_(r'#.*')
	def COMMENT(self, t):
		pass

	@_(r'\n+')
	def newline(self, t):
		self.lineno = t.value.count('\n')
