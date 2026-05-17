import sys

import pygame

import src.setup as setup


def draw_group(
	display_surface: pygame.Surface,
	entities_ids: list[int],
	surfaces: dict,
	rectangles: dict
) -> None:

	for entity_id in entities_ids:
		display_surface.blit(
			surfaces[entity_id],
			rectangles[entity_id]
		)


def get_delta_time(
	frames_per_second: int
) -> float:

	miliseconds = 1000
	return setup.CLOCK.tick(frames_per_second)/miliseconds


def exit_game(event) -> None:

	if event.type == pygame.QUIT\
	or event.type == pygame.KEYDOWN\
	and event.key == pygame.K_ESCAPE:
		pygame.quit()
		sys.exit()


def mouse_hover(
	mouse_position: tuple[int, int],
	rectangle: pygame.Rect
) -> bool:

	return rectangle.collidepoint(mouse_position)


def set_timer(interval: int) -> int:
	custom_event = pygame.event.custom_type()
	pygame.time.set_timer(custom_event, interval)

	return custom_event
