import pygame

from ..entities import flags
from ..surfaces_imports import backgrounds, inanimate, animated, rooms_buttons


rectangles = {
	"backgrounds": {
		flags.Flags.OFFICE		  : backgrounds[flags.Flags.OFFICE	 	   ]["empty" ][0].get_rect(topleft=(0, 0)),
		flags.Flags.SHOW_STAGE	  : backgrounds[flags.Flags.SHOW_STAGE 	   ]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.DINING_AREA	  : backgrounds[flags.Flags.DINING_AREA	   ]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.PIRATE_COVE	  : backgrounds[flags.Flags.PIRATE_COVE	   ]["stage1"].get_rect(topleft=(0, 0)),
		flags.Flags.WEST_HALL	  	  : backgrounds[flags.Flags.WEST_HALL  	   ]["empty" ][0].get_rect(topleft=(0, 0)),
		flags.Flags.WEST_HALL_CORNER: backgrounds[flags.Flags.WEST_HALL_CORNER]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.SUPPLY_CLOSET   : backgrounds[flags.Flags.SUPPLY_CLOSET   ]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.EAST_HALL	  	  : backgrounds[flags.Flags.EAST_HALL	   ]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.EAST_HALL_CORNER: backgrounds[flags.Flags.EAST_HALL_CORNER]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.BACKSTAGE	  	  : backgrounds[flags.Flags.BACKSTAGE	   ]["empty" ].get_rect(topleft=(0, 0)),
		flags.Flags.KITCHEN		  : backgrounds[flags.Flags.KITCHEN		   ][0		 ].get_rect(topleft=(0, 0)),
		flags.Flags.RESTROOMS	  	  : backgrounds[flags.Flags.RESTROOMS	   ]["empty" ].get_rect(topleft=(0, 0))
	},
	"inanimate": {
		flags.Flags.LEFT_BUTTONS_PANEL : inanimate[flags.Flags.LEFT_BUTTONS_PANEL ][0].get_rect(topleft=(  15, 315)),
		flags.Flags.RIGHT_BUTTONS_PANEL: inanimate[flags.Flags.RIGHT_BUTTONS_PANEL][0].get_rect(topleft=(1465, 315)),
		flags.Flags.LEFT_DOOR_BUTTON   : pygame.Rect((  45, 369), (40, 55)),
		flags.Flags.RIGHT_DOOR_BUTTON  : pygame.Rect((1488, 369), (40, 55)),
		flags.Flags.LEFT_LIGHT_BUTTON	 : pygame.Rect((  45, 447), (40, 55)),
		flags.Flags.RIGHT_LIGHT_BUTTON : pygame.Rect((1488, 447), (40, 55)),
	},
	"animated": {
		flags.Flags.FAN    	: animated[flags.Flags.FAN    	 ][0].get_rect(topleft=( 783, 303)),
		flags.Flags.LEFT_DOOR : animated[flags.Flags.LEFT_DOOR	 ][0].get_rect(topleft=(  70,  30)),
		flags.Flags.RIGHT_DOOR: animated[flags.Flags.RIGHT_DOOR ][0].get_rect(topleft=(1265,  30)),
	},
	"static": {
		flags.Flags.CAMERA		   : animated[flags.Flags.CAMERA		  ][0].get_rect(topleft=(0,0)),
		flags.Flags.CAMERA_TRANSITION: animated[flags.Flags.CAMERA_TRANSITION][0].get_rect(topleft=(0,0)),
	},
	"rooms_buttons": {
		flags.Flags.SHOW_STAGE 	  : rooms_buttons[flags.Flags.SHOW_STAGE		 ].get_rect(topleft=( 965,  364)),
		flags.Flags.DINING_AREA	  : rooms_buttons[flags.Flags.DINING_AREA	 ].get_rect(topleft=( 920,  400)),
		flags.Flags.PIRATE_COVE	  : rooms_buttons[flags.Flags.PIRATE_COVE	 ].get_rect(topleft=( 895,  475)),
		flags.Flags.WEST_HALL  	  : rooms_buttons[flags.Flags.WEST_HALL		 ].get_rect(topleft=( 950,  620)),
		flags.Flags.WEST_HALL_CORNER: rooms_buttons[flags.Flags.WEST_HALL_CORNER].get_rect(topleft=( 950,  650)),
		flags.Flags.SUPPLY_CLOSET	  : rooms_buttons[flags.Flags.SUPPLY_CLOSET	 ].get_rect(topleft=( 875,  580)),
		flags.Flags.EAST_HALL		  : rooms_buttons[flags.Flags.EAST_HALL		 ].get_rect(topleft=(1055,  620)),
		flags.Flags.EAST_HALL_CORNER: rooms_buttons[flags.Flags.EAST_HALL_CORNER].get_rect(topleft=(1055,  650)),
		flags.Flags.BACKSTAGE		  : rooms_buttons[flags.Flags.BACKSTAGE		 ].get_rect(topleft=( 840,  415)),
		flags.Flags.KITCHEN		  : rooms_buttons[flags.Flags.KITCHEN		 ].get_rect(topleft=(1150,  570)),
		flags.Flags.RESTROOMS		  : rooms_buttons[flags.Flags.RESTROOMS		 ].get_rect(topleft=(1150,  440))
	}
}