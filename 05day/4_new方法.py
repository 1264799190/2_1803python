class Dog():
	def __init__(self):
		print('init')
	def __str__(self):
		return 'str'
	def __del__(self):
		print('del')
	def __new__(cls):
		

dog = Dog()
