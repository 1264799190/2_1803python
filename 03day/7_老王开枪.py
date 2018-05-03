class person():
	def __init__(self,name):
		self.name = name
		self.gun = None
	def shot(self,clip,bullet):
		clip.addbullet(bullet)
	def sunandsteel(self,clip):
		gun.addclip(clip)
	def take_gun(self,gun):
		self.gun = gun
	def shoot(self,enemy):
		bullet = self.gun.popbullet()
class gun():
	def __init__(self,name):
		self.name = name
		self.clip = None
	def sunandsteel(self,clip):
		self.clip = clip
		print(id(sunandsteel))
	def popgunbullet(self):
		return self.clip.popbullet()
class clip():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	def addbullet(self,bullet):
		self.bullet_list.append(bullet)
		print(len(self.bullet_list))
	def popbullet(self):
		return self.bullet_list.pop()
class bullet():
	pass
laowang = person('老王')
AK47 = gun('AK47')
clip = clip
for i in range(20):
	bullet = bullet()
	laowang.shot(clip,bullet)
laowang.sunandsteel(AK47,clip)

xiaowang = person('小王')
laowang.take_gun(AK47)	
laowang.shoot('xiaowang')

