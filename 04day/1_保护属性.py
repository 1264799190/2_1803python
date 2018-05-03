class Person():
	def __init__(self):
		self.__money = 100

	def getmoney(self):
		return self.__money

	def setmoney(self,money):
		if money <= 0:
			print('输入非法')
		else:
			self.__money = money	

xiaoming = Person()
xiaoming.setmoney(-20)
print(xiaoming.getmoney())
