class Boy():
	def __init__(self,age):
		self.age = age
		self.games = ['粪车','飞车','卡丁车']
	def opencar(self,car):
		print('一定会开车%s'%car)
	def showage(self):
		print('年龄%d'%self.age)	
	def showgames(self):
		for i in self.games:
			print(i)
xiaojun = Boy(12)
xiaojun.showage()
xiaojun.showgames()
xiaojun.opencar('卡车')
