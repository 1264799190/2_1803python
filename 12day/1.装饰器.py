def w1(fun):
	def inner(*args,**kwargs):
		print('验证')
		print(*args)
		ren = fun(*args,**kwargs)
		return ren
	return inner
@w1
def test(a,b):
	print('a == %d b == %d'%(a,b))
	return 'haha'

@w1
def test2(a,b):
	print('hehe')
@w1
def test3():
	return 'gaga'

test(1,2)
test2(1,2)
print(test3())
