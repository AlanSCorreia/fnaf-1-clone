import pygame


class UIEstatico:
	def __init__(self,
				 powerLeft: int,
				 usage: int) -> None:
		
		self.botaoCameraSurface   = pygame.image.load("assets\\6-CAMERAS\\0-FLIP.png").convert_alpha()
		self.botaoCameraRectangle = self.botaoCameraSurface.get_rect(topleft=(pygame.display.get_window_size()[0]/2-self.botaoCameraSurface.get_width()/2-50, pygame.display.get_window_size()[1]-90))
		
		self.powerLeftSurface = fonte.render(f"Power Left: {powerLeft:>02}%\n\nUsage: ",
									   		 True,
											 pygame.Color("white"))
		self.powerLeftRectangle = self.powerLeftSurface.get_rect(topleft=(50, 620))

		self.usage = usage

	def definirBarras(self,
				   	  uso):
		
		if not uso:
			return None

		x = 130
		x_offset = 21
		y = 650

		for quantidade in range(uso):
			if quantidade == 0:
				pygame.draw.rect(displaySurface,
					 			 pygame.Color("green"),
								 ((x, y),
		  						 (16, 32)))
			
			elif quantidade == 1:
				pygame.draw.rect(displaySurface,
					 			 pygame.Color("green"),
								 ((x+(x_offset), y),
		  						 (16, 32)))
			
			elif quantidade == 2:
				pygame.draw.rect(displaySurface,
					 			 pygame.Color("yellow"),
								 ((x+(x_offset*2), y),
		  						 (16, 32)))
			
			elif quantidade == 3:
				pygame.draw.rect(displaySurface,
					 			 pygame.Color("red"),
								 ((x+(x_offset*3), y),
		  						 (16, 32)))
			
			elif quantidade == 4:
				pygame.draw.rect(displaySurface,
					 			 pygame.Color("red"),
								 ((x+(x_offset*4), y),
		  						 (16, 32)))

	def desenhar(self):

		displaySurface.blit(self.botaoCameraSurface,
						   		 self.botaoCameraRectangle)
		displaySurface.blit(self.powerLeftSurface,
						   		 self.powerLeftRectangle)
		self.definirBarras(self.usage)


class UIEstaticoComCamera:
	def __init__(self) -> None:
		
		self.minimapaSurface = pygame.image.load("assets\\6-CAMERAS\\1-MAP.png").convert_alpha()
		self.minimapaRectangle = self.minimapaSurface.get_rect(topleft=(840, 320))

		self.recSurface = pygame.image.load("assets\\6-CAMERAS\\0-REC.png").convert_alpha()
		self.recRectangle = self.recSurface.get_rect(topleft=(50, 50)) 
	
	def desenhar(self):
		pygame.draw.rect(displaySurface,
				   		 pygame.color.Color(255, 255, 255),
						 ((25, 25), (1215, 670)), 3)
		displaySurface.blit(self.minimapaSurface,
					  		self.minimapaRectangle)
		displaySurface.blit(self.recSurface,
					  		self.recRectangle)


pygame.init()
janelaLargura, janelaAltura = 1280, 720
displaySurface = pygame.display.set_mode((janelaLargura, janelaAltura),
										 pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")
fonte = pygame.font.Font("fonte\\LcdSolid.ttf")
clock = pygame.time.Clock()

uiEstatico = UIEstatico(100, 1)
uiEstaticoComCamera = UIEstaticoComCamera()

