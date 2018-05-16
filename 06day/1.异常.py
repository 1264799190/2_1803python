'''
try:
	print(num)
	open('xxx.txt')
except NameError:
	print('我糙')
finally:
	print('我插')
'''
try: 
#11/0 
#open("xxx.txt") 
	print(num) 
	print("hahahahahhaha") 
except (NameError,FileNotFoundError): 
	print("出错了") 
except Exception as ret: 
	print("大错特错") 
	print(ret) 
else: 
	print("没有错误会走这") 
finally: 
	print("有错没错都走") 
print("hehehehehe")	 
