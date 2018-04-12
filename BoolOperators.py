def TAU(*args): return True
def CONTR(*args): return False
def NOT(val): return not val
def ID(val): return val
def AND(a, b): return a and b
def OR(a, b): return a or b
def NAND(a, b): return not (a and b)
def NOR(a, b): return not (a or b)
def ANDN(a, b): return (a and b) or not a
def ORN(a, b): return a and (not b)
def NANDN(a, b): return a or (not b)
def NORN(a, b): return (not a) and b
def XNOR(a, b): return (a and b) or ((not a) and (not b))
def XOR(a, b): return (a and (not b)) or ((not a) and b)

class Boolean(int):

	def __init__(self, _bool):
		self._bool = bool(_bool)

	def __bool__(self):
		if self == 0: return False
		elif self == 1: return True

	def __str__(self):
		if self == False: return 'False'
		elif self == True: return 'True'

	def __int__(self):
		if self == False: return 0
		elif self == True: return 1

	def __neg__(self): return not self
	def __add__(self, other): return self or other
	def __sub__(self, other): return self and (not other)
	def __mul__(self, other): return self and other
	def __or__(self,  other): return self or other
	def __and__(self, other): return self and other
	def __xor__(self, other): return self ^ other
