from setup import font
import pygame


ui_next_id: int = 0
ui_surfaces: dict[int, pygame.Surface] = dict()
ui_rectangles: dict[int, pygame.Rect ] = dict()
ui_power_usage_bars: int = 2
ui_power_left_percentage: int = 100


def ui_increase_next_id() -> None:
	global ui_next_id

	ui_next_id += 1


def ui_import_static_icon(surface_path: str,
						  topleft_point: tuple[int, int]) -> None:
	global ui_surfaces, ui_rectangles
	
	surface: pygame.Surface = pygame.image.load(surface_path).convert_alpha()
	rectangle: pygame.Rect = surface.get_rect(topleft=topleft_point)
	
	ui_surfaces[ui_next_id  ] = surface
	ui_rectangles[ui_next_id] = rectangle

	ui_increase_next_id()


def ui_create_static_text(text: str,
						  font: pygame.Font,
						  color: pygame.Color,
						  topleft_point: tuple[int, int]) -> None:
	global ui_surfaces, ui_rectangles
	
	text_surface: pygame.Surface = font.render(text, True, color=color)
	text_rectangle: pygame.Rect = text_surface.get_rect(topleft=topleft_point)

	ui_surfaces[ui_next_id  ] = text_surface
	ui_rectangles[ui_next_id] = text_rectangle

	ui_increase_next_id()


def increase_power_usage() -> None:
	global ui_power_usage_bars

	ui_power_usage_bars += 1


def decrease_power_usage() -> None:
	global ui_power_usage_bars

	ui_power_usage_bars -= 1


def define_power_usage_percentage(percentage: int) -> None:
	global ui_power_left_percentage

	ui_power_left_percentage = percentage


def draw_energy_bars(display_surface: pygame.Surface,
					 usage: int) -> None:

	x = 130
	y = 650
	x_offset = 21
	
	for number in range(1, usage):

		color: str = "green"
		
		if number == 3:
			color = "yellow"
		
		elif number == 4:
			color = "red"

		pygame.draw.rect(display_surface,
						 pygame.Color(color),
						 ((x+(x_offset*number), y),
						 	   (16, 32)))


ui_import_static_icon("FNAF ASSETS REORGANIZED BY ENTEREST\\6-CAMERAS\\0-FLIP.png",
					  (pygame.display.get_window_size()[0]//2-(600//2)-50,
					  pygame.display.get_window_size()[1]-90))

ui_import_static_icon("FNAF ASSETS REORGANIZED BY ENTEREST\\6-CAMERAS\\1-MAP.png",
					  (840, 320))

ui_import_static_icon("FNAF ASSETS REORGANIZED BY ENTEREST\\6-CAMERAS\\0-REC.png",
					  (50, 50))

ui_create_static_text(f"Power Left: {ui_power_left_percentage:>02}%\n\nUsage: ",
					  font,
					  pygame.Color("white"),
					  (50, 620))
