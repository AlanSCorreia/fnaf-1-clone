import pygame

from src.events.event_emitter import GUIEventEmitter


class TextElement(pygame.sprite.Sprite):
	def __init__(
		self,
		text_font: pygame.Font,
		text_content: str,
		text_color: str,
		position: tuple[int, int],
		groups: list[pygame.sprite.Group]
	) -> None:

		from src.animations.user_interface import FadeAnimation
		
		super().__init__(groups)
		self.text_font: pygame.Font = text_font
		self.image: pygame.Surface = self.text_font.render(
			text_content,
			True,
			color=text_color
		)
		self.rect: pygame.Rect = self.image.get_rect(topleft=position)
		self.event_emitter: GUIEventEmitter = GUIEventEmitter()

		self.fade_animation: FadeAnimation = FadeAnimation(self)

	def fade_in(self) -> None:

		self.fade_animation.start_fade_in()
		# print("Fade in started")
	
	def fade_out(self) -> None:

		self.fade_animation.start_fade_out()
	
	def update(self) -> None:
		
		self.fade_animation.update()
