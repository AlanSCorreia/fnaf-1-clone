import sys
import pygame


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")
clock = pygame.time.Clock()

image = {"escritorio": pygame.image.load("FNAF ASSETS REORGANIZED BY ENTEREST\\3-THE_OFFICE\\1-OFFICE.png").convert_alpha(),
		 "ventilador": pygame.image.load("FNAF ASSETS REORGANIZED BY ENTEREST\\3-THE_OFFICE\\FAN\\1.png")}
rect  = {"escritorio": image["escritorio"].get_rect(topleft=(0, 0)),
		 "ventilador": image["ventilador"].get_rect(topleft=(783, 303))}

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if  event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				print(pygame.mouse.get_pos())
		
	delta_time = clock.tick(60)/1000
	camera_speed = 10

	if pygame.mouse.get_pos()[0] > 1100 and rect["escritorio"].x >= -320:
		rect["escritorio"].x -= camera_speed
		rect["ventilador"].x -= camera_speed
	elif pygame.mouse.get_pos()[0] < 200 and rect["escritorio"].x <= 10:
		rect["escritorio"].x += camera_speed
		rect["ventilador"].x += camera_speed

	for key in image.keys():
		WINDOW.blit(image[key], rect[key])

	pygame.display.update()
