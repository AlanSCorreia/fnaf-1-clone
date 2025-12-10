import pygame


class StaticUI:
	def __init__(self,
				 powerLeft: int,
				 usage: int) -> None:
		
		self.camera_button_surf   = pygame.image.load("assets\\6-CAMERAS\\0-FLIP.png").convert_alpha()
		self.camera_button_rect = self.camera_button_surf.get_rect(topleft=(pygame.display.get_window_size()[0]/2-self.camera_button_surf.get_width()/2-50, pygame.display.get_window_size()[1]-90))
		
		self.power_left_surf = font.render(f"Power Left: {powerLeft:>02}%\n\nUsage: ",
									   		 True,
											 pygame.Color("white"))
		self.power_left_rect = self.power_left_surf.get_rect(topleft=(50, 620))

		self.usage = usage

	def set_power_bars(self,
				   	  uso):
		
		if not uso:
			return None

		x = 130
		x_offset = 21
		y = 650

		for quantidade in range(uso):
			if quantidade == 0:
				pygame.draw.rect(display_surface,
					 			 pygame.Color("green"),
								 ((x, y),
		  						 (16, 32)))
			
			elif quantidade == 1:
				pygame.draw.rect(display_surface,
					 			 pygame.Color("green"),
								 ((x+(x_offset), y),
		  						 (16, 32)))
			
			elif quantidade == 2:
				pygame.draw.rect(display_surface,
					 			 pygame.Color("yellow"),
								 ((x+(x_offset*2), y),
		  						 (16, 32)))
			
			elif quantidade == 3:
				pygame.draw.rect(display_surface,
					 			 pygame.Color("red"),
								 ((x+(x_offset*3), y),
		  						 (16, 32)))
			
			elif quantidade == 4:
				pygame.draw.rect(display_surface,
					 			 pygame.Color("red"),
								 ((x+(x_offset*4), y),
		  						 (16, 32)))

	def draw(self):

		display_surface.blit(self.camera_button_surf,
						   		 self.camera_button_rect)
		display_surface.blit(self.power_left_surf,
						   		 self.power_left_rect)
		self.set_power_bars(self.usage)


class CameraStaticUI:
	def __init__(self) -> None:
		
		self.minimap_surf = pygame.image.load("assets\\6-CAMERAS\\1-MAP.png").convert_alpha()
		self.minimap_rect = self.minimap_surf.get_rect(topleft=(840, 320))

		self.rec_icon_surf = pygame.image.load("assets\\6-CAMERAS\\0-REC.png").convert_alpha()
		self.rec_icon_rect = self.rec_icon_surf.get_rect(topleft=(50, 50)) 
	
	def draw(self):
		pygame.draw.rect(display_surface,
				   		 pygame.color.Color(255, 255, 255),
						 ((25, 25), (1215, 670)), 3)
		display_surface.blit(self.minimap_surf,
					  		self.minimap_rect)
		display_surface.blit(self.rec_icon_surf,
					  		self.rec_icon_rect)


pygame.init()
window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width, window_height),
										  pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")
debug_font = pygame.font.Font("fonte\\LcdSolid.ttf", 12)
font = pygame.font.Font("fonte\\LcdSolid.ttf")
clock = pygame.time.Clock()

static_ui = StaticUI(100, 1)
camera_static_ui = CameraStaticUI()
