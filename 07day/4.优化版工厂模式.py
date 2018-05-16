class Op(object):
	def __init__(self,num1 = 0,num2 =0):
		self.num1 = num1
		self.num2 = num2
	def getreturn(self):
		pass

class jia(Op):
	def getreturn(self):
		return self.num1 + self.num2

class jian(Op):
	def getreturn(self):
		return self.num1 - self.num2

class cheng(Op):
	def getreturn(self):
		return self.num1 * self.num2

class chu(Op):
	def getreturn(self):
		if self.num != 0:
			return self.num1 / self.num2

class factory(object):
	def create_op(self,type):
		if type == '+':
			return jia()
		elif type == '-':
			return jian()
		elif type == '*':
			return cheng()
		elif type == '/':
			return chu()

wq = factory()
Jia = wq.create_op('+')
Jia.num1 = 1
Jia.num2 = 2
print(Jia.getreturn())	
