class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.HP = 100
	def shot(self,clip,bullet):
		clip.addBullet(bullet)
	def Sunandsteel(self,gun,clip):
		gun.Sunandsteel(clip)
	def take_Gun(self,gun):
		self.gun = gun
	def shoot(self,enemy):
		bullet = self.gun.popGunBullet()
		bullet.kill(enemy)

class Gun():
	def __init__(self,name):
		self.name = name
		self.clip = None
	def Sunandsteel(self,clip):
		self.clip = clip
	def popGunBullet(self):
		return self.clip.popBullet()

class Clip():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	def addBullet(self,bullet):
		self.bullet_list.append(bullet)
		print(len(self.bullet_list))
	def popBullet(self):
		return self.bullet_list.pop()

class Bullet():
	def __init__(self):
		self.power = 10
	def kill(self,enemy):
		enemy.HP -= self.power
		print('剩余血量%d'%enemy.HP)
laowang = Person('老王')

AK47 = Gun('AK47')
bullet = Bullet()
clip = Clip(20)
for i in range(20):
	bullet = Bullet()
	laowang.shot(clip,bullet)
laowang.Sunandsteel(AK47,clip)
xiaowang = Person('小王')
laowang.take_Gun(AK47)	
laowang.shoot(xiaowang)

laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
laowang.shoot(xiaowang)
