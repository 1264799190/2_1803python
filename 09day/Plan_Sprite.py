import pygame 
import random 
SCREEN_RECT = pygame.Rect(0,0,480,700) 
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite): 
	def __init__(self,image_name,speed=1): 
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y += self.speed
class Enemy(GameSprite): 
	def __init__(self): 
		super().__init__("./images/enemy1.png")
		self.speed = random.randint(1, 3)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, max_x)
	def update(self): 
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			print("敌机飞出屏幕...")
class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
 		super().update()
 		if self.rect.y >= SCREEN_RECT.height:
 			self.rect.y = -self.rect.height 
class Enemy(GameSprite):
	def __init__(self):
		image_name = "./images/enemy-1.gif"
		super().__init__(image_name) 
		self.speed = random.randint(1,3)
		max_x = SCREEN_RECT.width - self.rect.width 
		self.rect.x = random.randint(0,max_x)
		self.rect.bottom = 0 
	def update(self): 
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
	def __del__(self):
		print('删除%s'%self.rect)
class Hero(GameSprite):
	def __init__(self):
		super().__init__('./images/hero.gif',0) 
		self.rect.centerx = SCREEN_RECT.centerx	
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()
	def fire(self):
		bullet = Bullet()
		bullet.rect.bottom = self.rect.y-20
		bullet.rect.centerx = self.rect.centerx
		self.bullets.add(bullet)
	def update(self):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.rect.x += 10
		if keys_pressed[pygame.K_LEFT]:
			self.rect.x -= 10
		if keys_pressed[pygame. K_UP]:
			self.rect.y -= 10
		if keys_pressed[pygame.K_DOWN]:
			self.rect.y += 10
		if keys_pressed[pygame.K_SPACE]:
			self.fire()
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
class Bullet(GameSprite):
	def __init__(self):
		super().__init__('./images/bullet1.png',-10)
	def update(self):
		super().update()		
		if self.rect.bottom < 0:
			self.kill()