__all__ = ['text','jishu','oushu']
def jishu():
	for i in range(100):
		if i%2 != 0:
			print(i)	
def oushu():
	for i in range(100):
		if i%2 == 0:
			print(i)
def text():
	print('我是你爹，老板')
if __name__ == '__main__':
	jishu()
	oushu()
	text()
