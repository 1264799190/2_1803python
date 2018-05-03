class Roastpig():
	def __init__(self):
		self.cookedlever = 0
		self.cookedtar = '生的'
		self.condliments = []

	def cook(self,time):
		self.cooktoast += time
		if self.cookedlever > 0 and self.cooktoast <= 3:
			self.cookedtar = '半生不熟'
		elif self.cookedlever > 3 and self.cooktoast <= 6:
			self.cookedtar = '熟了'
		elif self.cookedlever <= 6 :
			self,cookedtar = '糊了'

	def add




