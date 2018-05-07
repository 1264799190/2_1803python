class ShowError(Exception):
	def __init__(self,length,atleast):
		self.length = length
		self.atleast = atleast
def main():
	try:
		s = input('请输入')
		if len(s) < 3:
			raise ShowError(len(3),3)
	except ShowError as result:
		print('ShowError:输入的长度是%d,长度至少是'%(result.length,result.atleast))
	else:
		print('没有异常发生')
main()

