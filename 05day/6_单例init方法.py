class dog(object):
	instance = None
	init_flag = False
	def __init__(self,name):
		if dog.init_flag == False:
			self.name = name
			dog.init_flag = True
	def __new__(cls,name):
		if cls.instance == None:
			cls.instance = object.__new__(cls)
			return cls.instance
		else:
			return cls.instance
Dog = dog('小王')
Dog1 = dog('小李')
print(id(Dog))
print(id(Dog1))
print(Dog.name)
print(Dog1.name)
