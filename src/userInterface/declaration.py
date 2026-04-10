import pygame

from src.event_emitter import EventEmitter


class UITextElement(pygame.sprite.Sprite):
	def __init__(
		self,
		text: str,
		text_font: pygame.Font,
		text_color: str,
		position: tuple[int, int],
		groups: list[pygame.sprite.Group]
	) -> None:

		super().__init__(groups)
		self.image: pygame.Surface = text_font.render(text, True, color=text_color)
		self.rect: pygame.Rect = self.image.get_rect(topleft=position)
		self.event_emitter: EventEmitter = EventEmitter()
	
	def update(self) -> None:
		pass


class UIStaticElement(pygame.sprite.Sprite):
	def __init__(
		self,
		image_path: str,
		position: tuple[int, int],
		groups: list[pygame.sprite.Group]
	) -> None:

		super().__init__(groups)
		self.image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect(topleft=position)
		self.event_emitter = EventEmitter()
		
	def update(self) -> None:
		pass


POWER_USAGE = {
	"bars": 2,
	"left_percentage": 100
}


def increase_power_usage() -> None:
	POWER_USAGE["bars"] += 1


def decrease_power_usage() -> None:
	POWER_USAGE["bars"] -= 1


def define_power_usage_percentage(
	percentage: int
) -> None:

	POWER_USAGE["left_percentage"] = percentage


def draw_power_bars(
	display_surface: pygame.Surface,
	power_usage: int
) -> None:

	x = 130
	y = 650
	x_offset = 21
	
	for number in range(1, power_usage):

		color: str = "green"
		
		if number == 3:
			color = "yellow"
		
		elif number == 4:
			color = "red"

		pygame.draw.rect(display_surface,
						 pygame.Color(color),
						 ((x+(x_offset*number), y),
						 	   (16, 32)))


# flip_button = UIStaticElement(
# 	"FNAF ASSETS REORGANIZED BY ENTEREST/6-CAMERAS/0-FLIP.png",
# 	(
# 		pygame.display.get_window_size()[0]//2-(600//2)-50,
# 		pygame.display.get_window_size()[1]-90
# 	),
# 	[
# 		elements_off_camera_group,
# 		elements_on_camera_group
# 	]
# )

# map_icon = UIStaticElement(
# 	"FNAF ASSETS REORGANIZED BY ENTEREST/6-CAMERAS/1-MAP.png",
# 	(840, 320),
# 	[elements_off_camera_group]
# )

# rec_icon = UIStaticElement(
# 	"FNAF ASSETS REORGANIZED BY ENTEREST/6-CAMERAS/0-REC.png",
# 	(50, 50),
# 	[elements_off_camera_group]
# )

# power_left_percentage = UITextElement(
# 	f"Power Left: {POWER_USAGE["left_percentage"]:>02}%\n\nUsage: ",
# 	setup.FONT,
# 	pygame.Color("white"),
# 	(50, 620),
# 	[elements_off_camera_group]
# )
