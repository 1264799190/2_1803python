import pygame
SCREEN_RECT = pygame.Rect(0,0,700,700) 
class GameSprite(pygame.sprite.Sprite): 
	def __init__(self,image_name,speed = 1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self,*args):
		self.rect.y += self.speed