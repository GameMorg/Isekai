import pygame
from save_game import *
from button import *


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
		


def rect(win, color, x=0, y=0, w=70, h=30):
	pygame.draw.rect(win(color), (x, y, w, h))
	

def load_img():
	pass

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

def menu():
	show = True

	pygame.init()

	save = Save("Save")

	BLUE = (0, 0, 255)

	display_widht = 800
	display_height = 600
	win  = pygame.display.set_mode((display_widht, display_height))


	while show:
		pygame.time.delay(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				show = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pygame.draw.rect(win, BLUE, (event.pos[0]-10, event.pos[1]-10, 20, 20))
					pygame.display.update()

		win.fill((255, 255, 255))
		pygame.draw.rect(win, (0, 0, 255), (50, 50, 50, 50))
		pygame.display.update()
