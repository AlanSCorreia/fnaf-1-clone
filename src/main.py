import sys

from configuracoes import pygame, display_surface, clock, escritorio_group


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				print(pygame.mouse.get_pos())
		
	delta_time = clock.tick(60)/1000

	escritorio_group.update()
	
	escritorio_group.draw(display_surface)

	pygame.display.update()
