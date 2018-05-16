def fid(times):
	n = 0
	a,b = 0,1
	while n < times:
		print('hehe')
		temp = yield b
		print('haha')
		a,b = b,a+b
		n+=1
fid()

