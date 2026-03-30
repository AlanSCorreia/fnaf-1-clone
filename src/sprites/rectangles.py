import pygame

import src.sprites.surfaces as surfaces


CURRENT_ROOM_ON_CAMERA: str = "SHOW_STAGE"

BACKGROUNDS = {
	"OFFICE": surfaces.CURRENT_BACKGROUNDS["OFFICE"	   ].get_rect(topleft=(0, 0)),
	"CAMERA": surfaces.CURRENT_BACKGROUNDS["SHOW_STAGE"].get_rect(topleft=(0, 0)),
}

INANIMATED_PROPS = {
	"LEFT_BUTTONS_PANEL" : surfaces.CURRENT_INANIMATED_PROPS["LEFT_BUTTONS_PANEL" ].get_rect(topleft=(  15, 315)),
	"RIGHT_BUTTONS_PANEL": surfaces.CURRENT_INANIMATED_PROPS["RIGHT_BUTTONS_PANEL"].get_rect(topleft=(1465, 315)),
	"LEFT_DOOR"		  	 : surfaces.CURRENT_INANIMATED_PROPS["LEFT_DOOR"		  ].get_rect(topleft=(	 0,   0)),
	"RIGHT_DOOR"		 : surfaces.CURRENT_INANIMATED_PROPS["RIGHT_DOOR"		  ].get_rect(topleft=(	 0,   0)),
	"LEFT_DOOR_BUTTON"	 : pygame.Rect((  45, 369), (40, 55)),
	"RIGHT_DOOR_BUTTON"  : pygame.Rect((1488, 369), (40, 55)),
	"LEFT_LIGHT_BUTTON"  : pygame.Rect((  45, 447), (40, 55)),
	"RIGHT_LIGHT_BUTTON" : pygame.Rect((1488, 447), (40, 55)),
}

PANELS_BUTTONS = {
	"LEFT_DOOR_BUTTON"  : pygame.Rect(),
	"LEFT_LIGHT_BUTTON" : pygame.Rect(),
	"RIGHT_DOOR_BUTTON" : pygame.Rect(),
	"RIGHT_LIGHT_BUTTON": pygame.Rect(),
}

CAMERA_BUTTONS = {
	"SHOW_STAGE"	   : surfaces.CURRENT_CAMERA_BUTTONS["SHOW_STAGE"		].get_rect(topleft=( 965,  364)),
	"DINING_AREA"	   : surfaces.CURRENT_CAMERA_BUTTONS["DINING_AREA"	 	].get_rect(topleft=( 920,  400)),
	"PIRATE_COVE"	   : surfaces.CURRENT_CAMERA_BUTTONS["PIRATE_COVE"	 	].get_rect(topleft=( 895,  475)),
	"WEST_HALL"	   	   : surfaces.CURRENT_CAMERA_BUTTONS["WEST_HALL"		].get_rect(topleft=( 950,  620)),
	"WEST_HALL_CORNER" : surfaces.CURRENT_CAMERA_BUTTONS["WEST_HALL_CORNER"	].get_rect(topleft=( 950,  650)),
	"SUPPLY_CLOSET"    : surfaces.CURRENT_CAMERA_BUTTONS["SUPPLY_CLOSET"   	].get_rect(topleft=( 875,  580)),
	"EAST_HALL"	       : surfaces.CURRENT_CAMERA_BUTTONS["EAST_HALL"		].get_rect(topleft=(1055,  620)),
	"EAST_HALL_CORNER" : surfaces.CURRENT_CAMERA_BUTTONS["EAST_HALL_CORNER"	].get_rect(topleft=(1055,  650)),
	"BACKSTAGE"	   	   : surfaces.CURRENT_CAMERA_BUTTONS["BACKSTAGE"		].get_rect(topleft=( 840,  415)),
	"KITCHEN"		   : surfaces.CURRENT_CAMERA_BUTTONS["KITCHEN"		 	].get_rect(topleft=(1150,  570)),
	"RESTROOMS"	   	   : surfaces.CURRENT_CAMERA_BUTTONS["RESTROOMS"		].get_rect(topleft=(1150,  440))
}
