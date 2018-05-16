def fid():
	n = 0
	a,b = 0,1
	while n < 5:
		print('hehe')
		yield b
		print('haha')
		a,b = b,a+b
		n+=1
fid()

