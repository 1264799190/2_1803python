class Dog():
	count = 1
	def __init__(self,name):
		self.name = name
	def walk(self):
		print('汪汪叫')
	@ classmethod
	def text(cls):
		print('这是类方法')
'''
	@classmethod
	def tet(cls):
		count += 1
		return cls.count
'''
taidi = Dog('泰迪')
print(taidi.name)
#print(tet.count)
taidi.walk()
taidi.text()
