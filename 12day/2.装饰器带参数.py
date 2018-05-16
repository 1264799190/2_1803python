def w2(p):
	def w1(fun):
		def inner(*args,**kwargs):
			if p == 'hehe':
				print('验证')
			elif p == 'haha':
				print('验证hehe')
			ren = fun(*args,**kwargs)
			return ren
		return inner
	return w1
@w2('q')
def test(a,b):
	print('a == %d b == %d'%(a,b))
	return 'haha'

@w2('w')
def test2(a,b):
	print('hehe')

@w2('E')
def test3():
	return 'gaga'

test(1,2)
test2(1,2)
print(test3())
