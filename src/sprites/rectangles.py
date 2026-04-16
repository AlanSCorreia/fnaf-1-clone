import pygame

import src.setup_surfaces as setup_surfaces


CURRENT_ROOM_ON_CAMERA: str = "SHOW_STAGE"

BACKGROUNDS = {
	"OFFICE": setup_surfaces.BACKGROUNDS["OFFICE"	 ]["empty"].get_rect(topleft=(0, 0)),
	"CAMERA": setup_surfaces.BACKGROUNDS["SHOW_STAGE"]["empty"].get_rect(topleft=(0, 0)),
}

INANIMATED_PROPS = {
	"LEFT_BUTTONS_PANEL" : setup_surfaces.INANIMATED_PROPS["LEFT_BUTTONS_PANEL" ]["all_off"].get_rect(topleft=(  15, 315)),
	"RIGHT_BUTTONS_PANEL": setup_surfaces.INANIMATED_PROPS["RIGHT_BUTTONS_PANEL"]["all_off"].get_rect(topleft=(1465, 315)),
	"LEFT_DOOR"		  	 : setup_surfaces.INANIMATED_PROPS["LEFT_DOOR"		    ]["close"  ].get_rect(topleft=(   0,   0)),
	"RIGHT_DOOR"		 : setup_surfaces.INANIMATED_PROPS["RIGHT_DOOR"		    ]["close"  ].get_rect(topleft=(   0,   0)),
	"LEFT_DOOR_BUTTON"	 : pygame.Rect((  45, 369), (40, 55)),
	"RIGHT_DOOR_BUTTON"  : pygame.Rect((1488, 369), (40, 55)),
	"LEFT_LIGHT_BUTTON"  : pygame.Rect((  45, 447), (40, 55)),
	"RIGHT_LIGHT_BUTTON" : pygame.Rect((1488, 447), (40, 55)),
}

CAMERA_BUTTONS = {
	"SHOW_STAGE"	  : setup_surfaces.CAMERA_BUTTONS["SHOW_STAGE"		].get_rect(topleft=( 965,  364)),
	"DINING_AREA"	  : setup_surfaces.CAMERA_BUTTONS["DINING_AREA"	 	].get_rect(topleft=( 920,  400)),
	"PIRATE_COVE"	  : setup_surfaces.CAMERA_BUTTONS["PIRATE_COVE"	 	].get_rect(topleft=( 895,  475)),
	"WEST_HALL"	   	  : setup_surfaces.CAMERA_BUTTONS["WEST_HALL"		].get_rect(topleft=( 950,  620)),
	"WEST_HALL_CORNER": setup_surfaces.CAMERA_BUTTONS["WEST_HALL_CORNER"].get_rect(topleft=( 950,  650)),
	"SUPPLY_CLOSET"   : setup_surfaces.CAMERA_BUTTONS["SUPPLY_CLOSET"   ].get_rect(topleft=( 875,  580)),
	"EAST_HALL"	      : setup_surfaces.CAMERA_BUTTONS["EAST_HALL"		].get_rect(topleft=(1055,  620)),
	"EAST_HALL_CORNER": setup_surfaces.CAMERA_BUTTONS["EAST_HALL_CORNER"].get_rect(topleft=(1055,  650)),
	"BACKSTAGE"	   	  : setup_surfaces.CAMERA_BUTTONS["BACKSTAGE"		].get_rect(topleft=( 840,  415)),
	"KITCHEN"		  : setup_surfaces.CAMERA_BUTTONS["KITCHEN"		 	].get_rect(topleft=(1150,  570)),
	"RESTROOMS"	   	  : setup_surfaces.CAMERA_BUTTONS["RESTROOMS"		].get_rect(topleft=(1150,  440))
}
