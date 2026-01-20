import pygame

from components.nights import Nights
from components.game_states import GameStates
from surfaces_imports import import_all_assets


pygame.init()

display_surface: pygame.Surface = pygame.display.set_mode((1280, 720),
										  	  	   pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")

debug_font: pygame.Font  = pygame.font.Font("fonte\\LcdSolid.ttf", 12)
font	  : pygame.Font  = pygame.font.Font("fonte\\LcdSolid.ttf")
clock	  : pygame.Clock = pygame.time.Clock()

game_state	 : GameStates = GameStates.IN_GAME
current_night: Nights 	  = Nights.FIRST


position_offset_limits: dict[str, int] = {
	"left" : -320,
	"right": 10
}

office_objects_position_offset: dict[str, int] = {
	"vertical": 0,
	"base": 0
}

camera_background_position_offset: dict[str, int] = {
	"vertical": 0,
	"base": 0
}

import_all_assets()
