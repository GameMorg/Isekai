import pygame


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
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+display_widht / 2, -t+display_height / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-display_widht), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-display_height), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)  

def main():
	pygame.init()
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

