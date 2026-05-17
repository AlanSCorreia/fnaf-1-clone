import pygame

from src.userInterface.text_element import TextElement


class FadeAnimation:
	def __init__(
			self,
			image_context: TextElement
		) -> None:

		self.image_context = image_context

		self.delay = 20
		self.last_time = 0
		self._current_alpha_value = 255
		
		self.MAX_ALPHA_VALUE = 255
		self.MIN_ALPHA_VALUE = 0

		self.is_fading_in  = False
		self.is_fading_out = False
	
	@property
	def current_alpha_value(self) -> int:

		return self._current_alpha_value
	
	@current_alpha_value.setter
	def current_alpha_value(
		self,
		value: int
	) -> None:

		self._current_alpha_value = min(
			max(self.MIN_ALPHA_VALUE, value),
			self.MAX_ALPHA_VALUE
		)

	def _update_alpha_value(self) -> None:

		if self.is_fading_in:
			self.current_alpha_value += 1

		elif self.is_fading_out:
			self.current_alpha_value -= 1

	def _update_fade(
		self,
		current_time: int
	) -> None:

		# print(f"Last time the update ocurred: {self.last_time}")
		# print(f"Has delay passed: {current_time-self.last_time > self.delay}")

		if current_time-self.last_time > self.delay:

			self.image_context.image.set_alpha(self.current_alpha_value)
			self._update_alpha_value()
			self.last_time = current_time

			# print(f"Current alpha value set to {self.current_alpha_value}")
		
		self._end_fade_in()
		self._end_fade_out()
		
	def _end_fade_in(self) -> None:
		
		if self.current_alpha_value == self.MAX_ALPHA_VALUE:
			self.is_fading_in = False
			print("Fading in has ended")
	
	def _end_fade_out(self) -> None:

		if self.current_alpha_value == self.MIN_ALPHA_VALUE:
			self.is_fading_out = False
			# print("Fading out has ended")
	
	def start_fade_in(self) -> None:

		self.is_fading_in = True
		self.current_alpha_value = self.MIN_ALPHA_VALUE
		# print("Is fading in set to True")
		# print("Current alpha value set to MIN_ALPHA_VALUE")

	def start_fade_out(self) -> None:

		self.is_fading_out = True
		self.current_alpha_value = self.MAX_ALPHA_VALUE
		# print("Is fading out set to True")
		# print("Current alpha value set to MAX_ALPHA_VALUE")

	def update(self) -> None:

		if self.is_fading_in\
		or self.is_fading_out:
			self._update_fade(pygame.time.get_ticks())
			# print("Alpha value updated")
 