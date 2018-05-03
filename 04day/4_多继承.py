class A():
	def helpA(self):
		print('------A-------')
	def help(self):
		print('-----help------')
class B():
	def helpB(self):
		print('------B-------')
	def help(self):
		print('-----helpC-----')
class C(A,B):
	pass

c = C()
c.helpA()
c.helpB()
c.help()
