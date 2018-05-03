class Father():

	def __init__(self):
		self.__girl = 4
	
	def getgirl(self):
		return self.__girl

	def eat(self):
		print('吃饭')

	def sleep(self):
		print('睡觉')
	
class Son(Father):
	pass

son = Son()
son.eat()
son.sleep()
print(son.getgirl()) 

