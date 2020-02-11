import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
image = pygame.image.load('textures/background/backr.jpg').convert(24)
image.set_alpha(128)
window.fill((0, 0, 0))
window.blit(image, (0, 0))
image = pygame.transform.scale(image,(800, 600))
pygame.display.flip()
while True:
    for i in range(255):
        image.set_alpha(i)
        window.fill((0, 0, 0))
        window.blit(image, (0, 0))
        pygame.display.flip()
        if i == 254:
            for e in range(255):
                image.set_alpha(254-e)
                window.fill((0, 0, 0))
                window.blit(image, (0, 0))
                pygame.display.flip()