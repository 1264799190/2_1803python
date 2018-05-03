class pig:
	def sleep(self):
		print('呼呼呼')
	def eat(self):
		print('猪饲料')
	def introduce(self):
		print('姓名%s年龄%d颜色%s'%(self.name,self.age,self.color))
pq = pig()
pq.name = '佩琪'
pq.age = 12
pq.color = '粉色'
pq.sleep()
pq.eat()
pq.introduce()

wq = pig()
wq.name = '巴拉拉小魔仙'
wq.age = 12
wq.color = '屎黄色'
wq.sleep()
wq.eat()
wq.introduce()
