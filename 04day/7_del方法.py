class Dog():	 
	def __init__(self): 
		pass 
	def __str__(self): 
		return "" 
	def __del__(self): 
		print("del方法执行了") 
taidi = Dog() 
hashiqi = taidi 
del taidi 
#del hashiqi 
print("程序结束了") 
