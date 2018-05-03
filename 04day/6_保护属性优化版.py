class Dog(): 
	def __init__(self): 
		self.__age = 1
		pass 
	def wark(self): 
		print("汪汪叫") 
	def setAge(self,age): 
		if age <= 0: 
			print("传入年龄有误") 
		else: 
			self.__age = age 	 
	def getAge(self): 
		return self.__age 
	def __str__(self): 
		return "狗的年龄是%d"%self.__age 
xiaohuang = Dog() 
xiaohuang.setAge(10) 
print(xiaohuang.getAge()) 
print(xiaohuang) 
xiaohuang.wark() 

