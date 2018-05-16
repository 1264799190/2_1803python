class dog(object):
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
Dog = dog()
Dog1 = dog()
print(id(Dog))
print(id(Dog1))
