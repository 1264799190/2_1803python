def w1(fun):
	def inner():
		print('验证')
		fun()
	return inner
def test():
	print('hahaha')
test = w1(test)
test()
