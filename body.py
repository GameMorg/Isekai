import pygame
from save_game import *


class Hero(object):
	"""docstring for Hero"""
	def __init__(self, x, y, speed):
		super(Hero, self).__init__()
		self.x = x
		self.y = y
		self.speed = speed
	
	def x_set(self, x):
		self.x += x

	def y(self, y):
		self.y += y
		

class Camera(object):
	"""docstring for Camera"""
	def __init__(self, arg):
		super(Camera, self).__init__()
		self.arg = arg
		

def main():
	pygame.init()

	save = Save("Save")

	display_widht = 800
	display_height = 600
	win  = pygame.display.set_mode((display_widht, display_height))

	pygame.display.set_caption("Isekay")

	x = 100
	y = display_height/1.3
	widht = 32
	height = 64
	speed = 5



	hero = Hero(x, y, speed)

	run = True 
	while run:
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save("hero_x", hero.x)
				run = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and hero.x > 10:
			hero.x_set(-speed) 

		if keys[pygame.K_RIGHT] and hero.x < display_widht - 10 - widht:
			hero.x_set(speed) 




		win.fill((255,255,255))
		pygame.draw.rect(win, (0, 0, 255), (hero.x, hero.y, widht, height))
		pygame.display.update()




	pygame.quit()

