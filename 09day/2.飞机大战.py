import pygame
from Plan_Sprite import *
#pygame.mixer.init()
#pygame.mixer.music.load('./1314.MP3')
#pygame.mixer.music.play()
CREATE_ENEMY_EVENT = pygame.USEREVENT
screen = pygame.display.set_mode(SCREEN_RECT.size)
class PlanGame(object):
	def __init__(self):
		print('游戏初始化')
		self.screen = pygame.display.set_mode((480, 700))
		self.clock = pygame.time.Clock()
		self.__create_sprite()
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
		
	def start_Game(self): 
		print('开始游戏')	
		while True:
			self.clock.tick(60)	
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
	def __create_sprite(self):
		self.back_group = pygame.sprite.Group()
		self.enemy_group = pygame.sprite.Group()
		self.hero_group = pygame.sprite.Group()
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlanGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				self.enemy_group.add(Enemy())
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
				self.hero.fire()
	def __check_collide(self):
		pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
		if len(enemies) > 0:
			self.hero.kill()
			PlaneGame.__game_over()
		pass
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)

	def __game_over(self):
		print('游戏结束')
		pygame.quit()
		exit()
if __name__ == '__main__':
	plangame = PlanGame()
	plangame.start_Game()