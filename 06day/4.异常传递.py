def test1(): 
	print(num) 
def test2(): 
	test1() 
def test3(): 
	try: 
		test2() 
	except Exception as ret: 
		print(ret) 
		print("抓到异常了") 
test3() 
