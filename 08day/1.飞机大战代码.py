import pygame
from PlanSprite import *
pygame.init()
#set_mode(resolution = (0,0),flag = 0,depth = 0)
screen = pygame.display.set_mode((480,700))
#创建背景
bg = pygame.image.load('../1.飞机大战/images/background.png')
screen.blit(bg,(0,0))
#pygame.display.update()
#创建飞机
hero = pygame.image.load('../1.飞机大战/images/hero.gif')
screen.blit(hero,(180,570))
clock = pygame.time.Clock()
#pygame.display.update()
hero_rect = pygame.Rect(180,500,200,200)
enemy = GameSprite('../1.飞机大战/images/enemy2.png',2)
enemy1 = GameSprite('../1.飞机大战/images/enemy-3.gif',3)
enemy1.rect.x = 100
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:
	clock.tick(60)
	hero_rect.y -= 5
	#if hero_rect.y + hero_rect.height <= 0:
	#	hero_rect.y = 700	
	screen.blit(bg,(0,0)) 
	screen.blit(hero,hero_rect)
	if hero_rect.bottom <= 0:
		hero_rect.y = 700
	enemy_group.update()
	enemy_group.draw(screen)
	for event in pygame.event.get():
# 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()	
# 直接退出系统
			exit()
#pygame.quit()
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()