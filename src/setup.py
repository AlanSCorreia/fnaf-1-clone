import pygame


pygame.init()

DISPLAY_SURFACE: pygame.Surface = pygame.display.set_mode((1280, 720),
										  	  	   pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")

DEBUG_FONT: pygame.Font  = pygame.font.Font("fonts/LcdSolid.ttf", 12)
FONT	  : pygame.Font  = pygame.font.Font("fonts/LcdSolid.ttf")
CLOCK	  : pygame.Clock = pygame.time.Clock()


POSITIONS_OFFSET_OFFICE_LIMITS: dict[str, int] = {
	"left" : -320,
	"right": 10
}

POSITIONS_OFFSET: dict[str, dict[str, int]] = {
	"OFFICE": {
		"vertical": 0,
		"base": 0
	},

	"CAMERA": {
		"vertical": 0,
		"base": 0
	}
}
