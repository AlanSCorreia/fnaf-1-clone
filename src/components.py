from enum import Enum, auto
import random

import pygame

import entities
import surfaces_imports


class GameStates(Enum):
	MAIN_MENU    	  = auto()
	MENU_CUSTOM_NIGHT = auto()
	IN_GAME		  	  = auto()


class InGameStates(Enum):
	WITHOUT_CAMERA = auto()
	WITH_CAMERA	   = auto()
	GAME_OVER	   = auto()


class Nights(Enum):
	FIRST  = auto()
	SECOND = auto()
	THIRD  = auto()
	FOURTH = auto()
	FIFTH  = auto()
	SIXTH  = auto()
	CUSTOM = auto()


class _Globals:
	def __init__(self) -> None:
		self.game_state 	   = GameStates.IN_GAME
		self.ingame_state 	   = InGameStates.WITHOUT_CAMERA
		self.camera_background = entities.Entities.SHOW_STAGE
		self.current_night 	   = Nights.FIRST
		
		self.position_offset_limit = {
			"min": -320,
			"max": 10
		}

		self.position_offset = {
			"vertical": 0,
			"base": 0
		}

		self.camera_position_offset = {
			"vertical": 0,
			"base": 0
		}
		

class State:
	def __init__(self,
			  	 availability_delay: int,
				 state: bool=False) -> None:

		self.state: bool = state
		self.is_available: bool = True
		self.last_availability_time: int = 0
		self.availability_delay: int = availability_delay


class Frames:
	def __init__(self,
			  	 is_animation_playing : bool,
				 is_looping		   	  : bool,
				 is_reversing		  : bool,
				 restart_needed	   	  : bool,
				 current_frame		  : int,
				 last_time_frame   	  : float,
				 frames_delay 		  : float) -> None:

		self.is_animation_playing = is_animation_playing
		self.is_looping 		  = is_looping
		self.is_reversing 		  = is_reversing
		self.restart_needed 	  = restart_needed
		self.current_frame 		  = current_frame
		self.last_time_frame 	  = last_time_frame
		self.frames_delay 		  = frames_delay
		

surfaces = {
	"backgrounds": {
		entities.Entities.OFFICE			: surfaces_imports.backgrounds[entities.Entities.OFFICE		 	 ]["empty" ][0],
		entities.Entities.SHOW_STAGE		: surfaces_imports.backgrounds[entities.Entities.SHOW_STAGE 	 ][entities.Entities.BONNIE | entities.Entities.CHICA | entities.Entities.FREDDY][0],
		entities.Entities.DINING_AREA		: surfaces_imports.backgrounds[entities.Entities.DINING_AREA	 ]["empty" ],
		entities.Entities.PIRATE_COVE		: surfaces_imports.backgrounds[entities.Entities.PIRATE_COVE	 ]["stage1"],
		entities.Entities.WEST_HALL			: surfaces_imports.backgrounds[entities.Entities.WEST_HALL  	 ]["empty" ][0],
		entities.Entities.WEST_HALL_CORNER	: surfaces_imports.backgrounds[entities.Entities.WEST_HALL_CORNER]["empty" ],
		entities.Entities.SUPPLY_CLOSET		: surfaces_imports.backgrounds[entities.Entities.SUPPLY_CLOSET	 ]["empty" ],
		entities.Entities.EAST_HALL			: surfaces_imports.backgrounds[entities.Entities.EAST_HALL		 ]["empty" ],
		entities.Entities.EAST_HALL_CORNER	: surfaces_imports.backgrounds[entities.Entities.EAST_HALL_CORNER]["empty" ],
		entities.Entities.BACKSTAGE			: surfaces_imports.backgrounds[entities.Entities.BACKSTAGE	 	 ]["empty" ],
		entities.Entities.KITCHEN			: surfaces_imports.backgrounds[entities.Entities.KITCHEN		 ][0	   ],
		entities.Entities.RESTROOMS			: surfaces_imports.backgrounds[entities.Entities.RESTROOMS	 	 ]["empty" ]
	},
	"inanimate": {
		entities.Entities.LEFT_BUTTONS_PANEL : surfaces_imports.inanimate[entities.Entities.LEFT_BUTTONS_PANEL ][0],
		entities.Entities.RIGHT_BUTTONS_PANEL: surfaces_imports.inanimate[entities.Entities.RIGHT_BUTTONS_PANEL][0],
	},
	"animated": {
		entities.Entities.FAN    	: surfaces_imports.animated[entities.Entities.FAN		 ][0],
		entities.Entities.LEFT_DOOR : surfaces_imports.animated[entities.Entities.LEFT_DOOR  ][0],
		entities.Entities.RIGHT_DOOR: surfaces_imports.animated[entities.Entities.RIGHT_DOOR ][0],
	},
	"static": {
		entities.Entities.CAMERA		   : surfaces_imports.animated[entities.Entities.CAMERA			  ][0],
		entities.Entities.CAMERA_TRANSITION: surfaces_imports.animated[entities.Entities.CAMERA_TRANSITION][0]
	},
	"rooms_buttons": {
		entities.Entities.SHOW_STAGE 	  : surfaces_imports.rooms_buttons[entities.Entities.SHOW_STAGE		 ],
		entities.Entities.DINING_AREA	  : surfaces_imports.rooms_buttons[entities.Entities.DINING_AREA	 ],
		entities.Entities.PIRATE_COVE	  : surfaces_imports.rooms_buttons[entities.Entities.PIRATE_COVE	 ],
		entities.Entities.WEST_HALL  	  : surfaces_imports.rooms_buttons[entities.Entities.WEST_HALL		 ],
		entities.Entities.WEST_HALL_CORNER: surfaces_imports.rooms_buttons[entities.Entities.WEST_HALL_CORNER],
		entities.Entities.SUPPLY_CLOSET	  : surfaces_imports.rooms_buttons[entities.Entities.SUPPLY_CLOSET	 ],
		entities.Entities.EAST_HALL		  : surfaces_imports.rooms_buttons[entities.Entities.EAST_HALL	 	 ],
		entities.Entities.EAST_HALL_CORNER: surfaces_imports.rooms_buttons[entities.Entities.EAST_HALL_CORNER],
		entities.Entities.BACKSTAGE		  : surfaces_imports.rooms_buttons[entities.Entities.BACKSTAGE		 ],
		entities.Entities.KITCHEN		  : surfaces_imports.rooms_buttons[entities.Entities.KITCHEN		 ],
		entities.Entities.RESTROOMS		  : surfaces_imports.rooms_buttons[entities.Entities.RESTROOMS		 ]
	}
}

rectangles = {
	"backgrounds": {
		entities.Entities.OFFICE		  : surfaces_imports.backgrounds[entities.Entities.OFFICE	 	   ]["empty" ][0].get_rect(topleft=(0, 0)),
		entities.Entities.SHOW_STAGE	  : surfaces_imports.backgrounds[entities.Entities.SHOW_STAGE 	   ]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.DINING_AREA	  : surfaces_imports.backgrounds[entities.Entities.DINING_AREA	   ]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.PIRATE_COVE	  : surfaces_imports.backgrounds[entities.Entities.PIRATE_COVE	   ]["stage1"].get_rect(topleft=(0, 0)),
		entities.Entities.WEST_HALL	  	  : surfaces_imports.backgrounds[entities.Entities.WEST_HALL  	   ]["empty" ][0].get_rect(topleft=(0, 0)),
		entities.Entities.WEST_HALL_CORNER: surfaces_imports.backgrounds[entities.Entities.WEST_HALL_CORNER]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.SUPPLY_CLOSET   : surfaces_imports.backgrounds[entities.Entities.SUPPLY_CLOSET   ]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.EAST_HALL	  	  : surfaces_imports.backgrounds[entities.Entities.EAST_HALL	   ]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.EAST_HALL_CORNER: surfaces_imports.backgrounds[entities.Entities.EAST_HALL_CORNER]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.BACKSTAGE	  	  : surfaces_imports.backgrounds[entities.Entities.BACKSTAGE	   ]["empty" ].get_rect(topleft=(0, 0)),
		entities.Entities.KITCHEN		  : surfaces_imports.backgrounds[entities.Entities.KITCHEN		   ][0		 ].get_rect(topleft=(0, 0)),
		entities.Entities.RESTROOMS	  	  : surfaces_imports.backgrounds[entities.Entities.RESTROOMS	   ]["empty" ].get_rect(topleft=(0, 0))
	},
	"inanimate": {
		entities.Entities.LEFT_BUTTONS_PANEL : surfaces_imports.inanimate[entities.Entities.LEFT_BUTTONS_PANEL ][0].get_rect(topleft=(  15, 315)),
		entities.Entities.RIGHT_BUTTONS_PANEL: surfaces_imports.inanimate[entities.Entities.RIGHT_BUTTONS_PANEL][0].get_rect(topleft=(1465, 315)),
		entities.Entities.LEFT_DOOR_BUTTON   : pygame.Rect((  45, 369), (40, 55)),
		entities.Entities.RIGHT_DOOR_BUTTON  : pygame.Rect((1488, 369), (40, 55)),
		entities.Entities.LEFT_LIGHT_BUTTON	 : pygame.Rect((  45, 447), (40, 55)),
		entities.Entities.RIGHT_LIGHT_BUTTON : pygame.Rect((1488, 447), (40, 55)),
	},
	"animated": {
		entities.Entities.FAN    	: surfaces_imports.animated[entities.Entities.FAN    	 ][0].get_rect(topleft=( 783, 303)),
		entities.Entities.LEFT_DOOR : surfaces_imports.animated[entities.Entities.LEFT_DOOR	 ][0].get_rect(topleft=(  70,  30)),
		entities.Entities.RIGHT_DOOR: surfaces_imports.animated[entities.Entities.RIGHT_DOOR ][0].get_rect(topleft=(1265,  30)),
	},
	"static": {
		entities.Entities.CAMERA		   : surfaces_imports.animated[entities.Entities.CAMERA		  ][0].get_rect(topleft=(0,0)),
		entities.Entities.CAMERA_TRANSITION: surfaces_imports.animated[entities.Entities.CAMERA_TRANSITION][0].get_rect(topleft=(0,0)),
	},
	"rooms_buttons": {
		entities.Entities.SHOW_STAGE 	  : surfaces_imports.rooms_buttons[entities.Entities.SHOW_STAGE		 ].get_rect(topleft=( 965,  364)),
		entities.Entities.DINING_AREA	  : surfaces_imports.rooms_buttons[entities.Entities.DINING_AREA	 ].get_rect(topleft=( 920,  400)),
		entities.Entities.PIRATE_COVE	  : surfaces_imports.rooms_buttons[entities.Entities.PIRATE_COVE	 ].get_rect(topleft=( 895,  475)),
		entities.Entities.WEST_HALL  	  : surfaces_imports.rooms_buttons[entities.Entities.WEST_HALL		 ].get_rect(topleft=( 950,  620)),
		entities.Entities.WEST_HALL_CORNER: surfaces_imports.rooms_buttons[entities.Entities.WEST_HALL_CORNER].get_rect(topleft=( 950,  650)),
		entities.Entities.SUPPLY_CLOSET	  : surfaces_imports.rooms_buttons[entities.Entities.SUPPLY_CLOSET	 ].get_rect(topleft=( 875,  580)),
		entities.Entities.EAST_HALL		  : surfaces_imports.rooms_buttons[entities.Entities.EAST_HALL		 ].get_rect(topleft=(1055,  620)),
		entities.Entities.EAST_HALL_CORNER: surfaces_imports.rooms_buttons[entities.Entities.EAST_HALL_CORNER].get_rect(topleft=(1055,  650)),
		entities.Entities.BACKSTAGE		  : surfaces_imports.rooms_buttons[entities.Entities.BACKSTAGE		 ].get_rect(topleft=( 840,  415)),
		entities.Entities.KITCHEN		  : surfaces_imports.rooms_buttons[entities.Entities.KITCHEN		 ].get_rect(topleft=(1150,  570)),
		entities.Entities.RESTROOMS		  : surfaces_imports.rooms_buttons[entities.Entities.RESTROOMS		 ].get_rect(topleft=(1150,  440))
	}
}

states = {
	entities.Entities.MOUSE				: State(100),
	entities.Entities.SHOW_STAGE		: State(500),
	entities.Entities.DINING_AREA		: State(500),
	entities.Entities.PIRATE_COVE		: State(500),
	entities.Entities.WEST_HALL			: State(500),
	entities.Entities.WEST_HALL_CORNER	: State(500),
	entities.Entities.SUPPLY_CLOSET		: State(500),
	entities.Entities.EAST_HALL			: State(500),
	entities.Entities.EAST_HALL_CORNER	: State(500),
	entities.Entities.BACKSTAGE			: State(500),
	entities.Entities.KITCHEN			: State(500),
	entities.Entities.RESTROOMS			: State(500),
	entities.Entities.LEFT_DOOR			: State(500),
	entities.Entities.RIGHT_DOOR 		: State(500),
	entities.Entities.LEFT_DOOR_BUTTON	: State(500),
	entities.Entities.RIGHT_DOOR_BUTTON : State(500),
	entities.Entities.LEFT_LIGHT_BUTTON : State(250),
	entities.Entities.RIGHT_LIGHT_BUTTON: State(250),
	entities.Entities.CAMERA 	 		: State(500),
	entities.Entities.CAMERA_MOVEMENT	: State(1000, True)
}

frames = {
	entities.Entities.FAN      		   : Frames( True,  True, False, False, 0, 0, 25),
	entities.Entities.LEFT_DOOR  	   : Frames(False, False, False, False, 0, 0, 25),
	entities.Entities.RIGHT_DOOR   	   : Frames(False, False, False, False, 0, 0, 25),
	entities.Entities.CAMERA	       : Frames(False, False, False, False, 0, 0, 25),
	entities.Entities.CAMERA_TRANSITION: Frames(False, False, False,  True, 0, 0, 25)
}

difficult_levels = {
	Nights.FIRST : {
		entities.Entities.FREDDY: 0,
		entities.Entities.BONNIE: 0,
		entities.Entities.CHICA : 0,
		entities.Entities.FOXY  : 0
	},
	Nights.SECOND: {
		entities.Entities.FREDDY: 0,
		entities.Entities.BONNIE: 3,
		entities.Entities.CHICA : 1,
		entities.Entities.FOXY  : 1
	},
	Nights.THIRD : {
		entities.Entities.FREDDY: 1,
		entities.Entities.BONNIE: 0,
		entities.Entities.CHICA : 5,
		entities.Entities.FOXY  : 2
	},
	Nights.FOURTH: {
		entities.Entities.FREDDY: random.randint(1, 2),
		entities.Entities.BONNIE: 2,
		entities.Entities.CHICA : 4,
		entities.Entities.FOXY  : 6
	},
	Nights.FIFTH : {
		entities.Entities.FREDDY: 3,
		entities.Entities.BONNIE: 5,
		entities.Entities.CHICA : 7,
		entities.Entities.FOXY  : 5
	},
	Nights.SIXTH : {
		entities.Entities.FREDDY: 4,
		entities.Entities.BONNIE: 10,
		entities.Entities.CHICA : 12,
		entities.Entities.FOXY  : 6
	},
	Nights.CUSTOM: {
		entities.Entities.FREDDY: 0,
		entities.Entities.BONNIE: 0,
		entities.Entities.CHICA : 0,
		entities.Entities.FOXY  : 0
	},
}

movement_opportunity_delay = {
	entities.Entities.FREDDY: 3.02,
	entities.Entities.BONNIE: 4.97,
	entities.Entities.CHICA : 4.98,
	entities.Entities.FOXY  : 5.01
}

routes = {
	entities.Entities.FREDDY: {
		1: entities.Entities.SHOW_STAGE,
		2: entities.Entities.DINING_AREA,
		3: entities.Entities.RESTROOMS,
		4: entities.Entities.KITCHEN,
		5: entities.Entities.EAST_HALL,
		6: entities.Entities.EAST_HALL_CORNER,
		7: entities.Entities.RIGHT_DOOR
	},
	entities.Entities.BONNIE: {
		1: entities.Entities.SHOW_STAGE,
		2: [entities.Entities.BACKSTAGE,
	  		entities.Entities.DINING_AREA],
		3: entities.Entities.WEST_HALL,
		4: [entities.Entities.SUPPLY_CLOSET,
	  		entities.Entities.WEST_HALL_CORNER],
		5: entities.Entities.LEFT_DOOR
	},
	entities.Entities.CHICA : {
		1: entities.Entities.SHOW_STAGE,
		2: entities.Entities.DINING_AREA,
		3: [entities.Entities.RESTROOMS,
			entities.Entities.KITCHEN],
		4: [entities.Entities.EAST_HALL],
		5: [entities.Entities.DINING_AREA,
			entities.Entities.EAST_HALL_CORNER],
		6: [entities.Entities.EAST_HALL,
			entities.Entities.RIGHT_DOOR]
	},
	entities.Entities.FOXY  : {
		1: entities.Entities.PIRATE_COVE,
		2: "stage1",
		3: "stage2",
		4: "stage3",
		5: ["stage4_a", "stage4_b"],
		6: entities.Entities.EAST_HALL,
		7: entities.Entities.LEFT_DOOR
	}
}

current_room = {
	entities.Entities.FREDDY: routes[entities.Entities.FREDDY][1],
	entities.Entities.BONNIE: routes[entities.Entities.BONNIE][5],
	entities.Entities.CHICA : routes[entities.Entities.CHICA ][6][1],
	entities.Entities.FOXY  : routes[entities.Entities.FOXY  ][1]
}
