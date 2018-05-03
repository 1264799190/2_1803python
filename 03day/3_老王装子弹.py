class person():
	def __init__(self,name):
		self.name = name
	def shot(self,clip,bullet):
		clip.addbullet(bullet)
class gun():
	def __init__(self,name):
		self.name = name

class clip():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	def addbullet(self,bullet):
		self.bullet_list.append(bullet)
		print(len(self.bullet_list))

class bullet():
	
laowang = person('老王')
AK47 = gun('AK47')
clip = clip
for i in range(20):
	bullet = bullet()
	laowang.shot(clip,bullet)

	
