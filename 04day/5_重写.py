class Father():
	def makemmoney(self):
		print('手挣钱')

class Son(Father):
	def money(self):
		print('脑子挣钱')
		super().makemoney()
wq = Son()
wq.money()
wq.makemoney()

