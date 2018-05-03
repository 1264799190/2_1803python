class home():
	def __init__(self,area,price,address):
		self.area = area
		self.price = price
		self.address = address
		self.jiaju = []
		self.dengs = []
	def __str__(self):
		return '面积是%d平方米价格是%f美金地址是%s'%(self.area,self.price,self.address)	
	def addbed(self,bed):
		if self.area >= bed.getarea():
			self.jiaju.append(bed)
			self.area -= bed.getarea()
			print('加入成功')
			print(self.area)
		else:
			print('加入失败')
	def addlight(self,light):
		self.dengs.append(light)
	def switch(self):
		if self.dengs[0].getisopen():
			self.dengs[0].close()
		else:
			self.dengs[0].open()
class bed():
	def __init__(self,name,area):
		self.name = name
		self.area = area
	def __str__(self):
		return '名%s面积为%d'%(self.name,self.area)
	def getarea(self):
		return self.area
class light():
	def __init__(self,name):
		self.name = name 
		self.isopen = False
	def __str__(self):
		return '我叫%s灯'%self.name
	def open(self):
		self.isopen = True
		print('灯亮了')
	def close(self):
		self.isopen = False
		print('灯灭了')
	def getisopen(self):
		return self.isopen
my_home = home(120,1200,'北京天安门')
print(my_home)

my_bed = bed('杜蕾斯',20)
print(my_bed)

my_light = light('拉登')
print(my_light)

my_home.append(my_light)

my_home.addbed(my_bed)
my_home.addbed(my_bed)
my_home.addbed(my_bed)
my_home.addbed(my_bed)
my_home.addbed(my_bed)
my_home.addbed(my_bed)


