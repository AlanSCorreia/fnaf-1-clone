import pygame

import src.entities as entities
import src.components.surfaces as surfaces


CURRENT_ROOM_ON_CAMERA: int = entities.IDS["SHOW_STAGE"]

BACKGROUNDS = {
	entities.IDS["OFFICE"]: surfaces.CURRENT_BACKGROUNDS[entities.IDS["OFFICE"	  ]].get_rect(topleft=(0, 0)),
	entities.IDS["CAMERA"]: surfaces.CURRENT_BACKGROUNDS[entities.IDS["SHOW_STAGE"]].get_rect(topleft=(0, 0)),
}

INANIMATED_PROPS = {
	entities.IDS["LEFT_BUTTONS_PANEL" ]: surfaces.CURRENT_INANIMATED_PROPS[entities.IDS["LEFT_BUTTONS_PANEL" ]].get_rect(topleft=(  15, 315)),
	entities.IDS["RIGHT_BUTTONS_PANEL"]: surfaces.CURRENT_INANIMATED_PROPS[entities.IDS["RIGHT_BUTTONS_PANEL"]].get_rect(topleft=(1465, 315)),
	entities.IDS["LEFT_DOOR"		  ]: surfaces.CURRENT_INANIMATED_PROPS[entities.IDS["LEFT_DOOR"			 ]].get_rect(topleft=(	 0,   0)),
	entities.IDS["RIGHT_DOOR"		  ]: surfaces.CURRENT_INANIMATED_PROPS[entities.IDS["RIGHT_DOOR"		 ]].get_rect(topleft=(	 0,   0)),
	entities.IDS["LEFT_DOOR_BUTTON"	  ]: pygame.Rect((  45, 369), (40, 55)),
	entities.IDS["RIGHT_DOOR_BUTTON"  ]: pygame.Rect((1488, 369), (40, 55)),
	entities.IDS["LEFT_LIGHT_BUTTON"  ]: pygame.Rect((  45, 447), (40, 55)),
	entities.IDS["RIGHT_LIGHT_BUTTON" ]: pygame.Rect((1488, 447), (40, 55)),
}

ANIMATED_PROPS = {
	entities.IDS["FAN"		 ]: {"normal": surfaces.CURRENT_ANIMATED_PROPS[entities.IDS["FAN"		]]["normal"].get_rect(topleft=( 783, 303))},
	entities.IDS["LEFT_DOOR" ]: {"normal": surfaces.CURRENT_ANIMATED_PROPS[entities.IDS["LEFT_DOOR" ]]["normal"].get_rect(topleft=(  70,  30))},
	entities.IDS["RIGHT_DOOR"]: {"normal": surfaces.CURRENT_ANIMATED_PROPS[entities.IDS["RIGHT_DOOR"]]["normal"].get_rect(topleft=(1265,  30))},
}

PANELS_BUTTONS = {
	entities.IDS["LEFT_DOOR_BUTTON"  ]: pygame.Rect(),
	entities.IDS["LEFT_LIGHT_BUTTON" ]: pygame.Rect(),
	entities.IDS["RIGHT_DOOR_BUTTON" ]: pygame.Rect(),
	entities.IDS["RIGHT_LIGHT_BUTTON"]: pygame.Rect(),
}

CAMERA_BUTTONS = {
	entities.IDS["SHOW_STAGE"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["SHOW_STAGE"		 ]].get_rect(topleft=( 965,  364)),
	entities.IDS["DINING_AREA"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["DINING_AREA"	 ]].get_rect(topleft=( 920,  400)),
	entities.IDS["PIRATE_COVE"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["PIRATE_COVE"	 ]].get_rect(topleft=( 895,  475)),
	entities.IDS["WEST_HALL"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["WEST_HALL"		 ]].get_rect(topleft=( 950,  620)),
	entities.IDS["WEST_HALL_CORNER"]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["WEST_HALL_CORNER"]].get_rect(topleft=( 950,  650)),
	entities.IDS["SUPPLY_CLOSET"   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["SUPPLY_CLOSET"   ]].get_rect(topleft=( 875,  580)),
	entities.IDS["EAST_HALL"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["EAST_HALL"		 ]].get_rect(topleft=(1055,  620)),
	entities.IDS["EAST_HALL_CORNER"]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["EAST_HALL_CORNER"]].get_rect(topleft=(1055,  650)),
	entities.IDS["BACKSTAGE"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["BACKSTAGE"		 ]].get_rect(topleft=( 840,  415)),
	entities.IDS["KITCHEN"		   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["KITCHEN"		 ]].get_rect(topleft=(1150,  570)),
	entities.IDS["RESTROOMS"	   ]: surfaces.CURRENT_CAMERA_BUTTONS[entities.IDS["RESTROOMS"		 ]].get_rect(topleft=(1150,  440))
}

JUMPSCARES: dict[str | int, dict[str, int] | dict[str, dict[str, int]]] = {
	entities.IDS["FREDDY"]: {
        "normal"  : surfaces.CURRENT_JUMPSCARES[entities.IDS["FREDDY"]]["normal"  ].get_rect(topleft=(0, 0)),
        "no_power": surfaces.CURRENT_JUMPSCARES[entities.IDS["FREDDY"]]["no_power"].get_rect(topleft=(0, 0))
    },

    entities.IDS["BONNIE"]: {
        "normal": surfaces.CURRENT_JUMPSCARES[entities.IDS["BONNIE"]]["normal"].get_rect(topleft=(0, 0))
    },
    entities.IDS["CHICA" ]: {
        "normal": surfaces.CURRENT_JUMPSCARES[entities.IDS["CHICA" ]]["normal"].get_rect(topleft=(0, 0))
    },
    entities.IDS["FOXY"  ]: {
        "normal": surfaces.CURRENT_JUMPSCARES[entities.IDS["FOXY"  ]]["normal"].get_rect(topleft=(0, 0))
    },
}
