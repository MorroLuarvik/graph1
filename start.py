import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

screen.fill([255, 255, 255])
pygame.display.flip()

print(pygame.display.Info())

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				print("space pressed")
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				running = False

pygame.quit()