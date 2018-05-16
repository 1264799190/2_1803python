class datetext():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def outdate(self):
		print('%s年%s月%s日'%(self.year,self.month,self.day))
	@classmethod
	def handdate(cls,date):
		a,b,c = date.split('-')
		d = cls(a,b,c)	
		return d
str = '2018-04-03'

d = datetext.handdate(str)

d.outdate()


