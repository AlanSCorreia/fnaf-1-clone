import pygame

from src.events.event_emitter import GUIEventEmitter


class StaticElement(pygame.sprite.Sprite):
	def __init__(
		self,
		image_path: str,
		position: tuple[int, int],
		groups: list[pygame.sprite.Group]
	) -> None:

		super().__init__(groups)
		self.image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect(topleft=position)
		self.event_emitter = GUIEventEmitter()
		
	def update(self) -> None:
		pass


# TODO: Precisa refatorar sá porra
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
