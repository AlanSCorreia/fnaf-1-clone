import pygame


surfaces = dict()
rectangles = dict()
energy_usage = 0


def create_static_icon(_id: int,
					   surface_path: str,
					   rectangle_coordinate: tuple[int, int]) -> None:
	global surfaces, rectangles
	
	surface: pygame.Surface = pygame.image.load(surface_path).convert_alpha()
	rectangle: pygame.Rect = surface.get_rect(topleft=rectangle_coordinate)
	
	surfaces[_id] = surface
	rectangles[_id] = rectangle


def create_text(text: str,
				font: pygame.Font,
				color: pygame.Color,
				rectangle_coordinate: tuple[int, int]) -> None:
	
	pass


def set_energy_bars(self,
					display_surface: pygame.Surface,
					usage: int):

	x = 130
	x_offset = 21
	y = 650
	
	pygame.draw.rect(display_surface,
						pygame.Color("green"),
						((x+(x_offset*usage), y),
						(16, 32)))


class StaticUI:
	def __init__(self,
				 powerLeft: int,
				 usage: int) -> None:
		
		self.camera_button_surf = pygame.image.load("assets\\6-CAMERAS\\0-FLIP.png").convert_alpha()
		self.camera_button_rect = self.camera_button_surf.get_rect(topleft=(pygame.display.get_window_size()[0]/2-self.camera_button_surf.get_width()/2-50,
																	                 pygame.display.get_window_size()[1]-90))
		
		self.power_left_surf = font.render(f"Power Left: {powerLeft:>02}%\n\nUsage: ",
									                True,
													pygame.Color("white"))
		self.power_left_rect = self.power_left_surf.get_rect(topleft=(50, 620))

		self.usage = usage

    # subscription pattern
	

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


class Publisher:
	def __init__(self) -> None:
		self.subscribers: list[Subscriber] = []
	
	def add_subscriber(self, subscriber) -> None:
		self.subscribers.append(subscriber)
	
	def remove_subscriber(self, subscriber) -> None:
		self.subscribers.remove(subscriber)
	
	def send(self, ) -> None:
		pass


class Subscriber:
	def __init__(self) -> None:
		self.publisher = []

