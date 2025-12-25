import pygame
from .entities import flags


backgrounds = {
	flags.Flags.OFFICE: {
		"empty": {
			0: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE.png").convert_alpha(),
			1: pygame.image.load("assets\\3-THE_OFFICE\\LEFT_LIGHT.png").convert_alpha(),
			2: pygame.image.load("assets\\3-THE_OFFICE\\RIGHT_LIGHT.png").convert_alpha()
		},
		flags.Flags.BONNIE: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE_BONNIE.png").convert_alpha(),
		flags.Flags.CHICA : pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE_CHICA.png").convert_alpha(),
		"no_power"   : pygame.image.load("assets\\3-THE_OFFICE\\LIGHTS_OUT\\304.png").convert_alpha(),
		"freddys_jingle": pygame.image.load("assets\\3-THE_OFFICE\\LIGHTS_OUT\\305.png").convert_alpha() 
	},

	flags.Flags.SHOW_STAGE: {
		"empty": pygame.image.load("assets\\6-CAMERAS\\1-STAGE_ALL.png").convert_alpha(),
		flags.Flags.FREDDY | flags.Flags.BONNIE | flags.Flags.CHICA: {
			0: pygame.image.load("assets\\6-CAMERAS\\1-STAGE.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\1-STAGE_LOOKING.png").convert_alpha(),
		},
		flags.Flags.FREDDY | flags.Flags.CHICA: pygame.image.load("assets\\6-CAMERAS\\1-STAGE_BONNIE.png").convert_alpha(),
		flags.Flags.FREDDY | flags.Flags.BONNIE: pygame.image.load("assets\\6-CAMERAS\\1-STAGE_CHICA.png").convert_alpha(),
		flags.Flags.FREDDY: pygame.image.load("assets\\6-CAMERAS\\1-STAGE_FREDDY_LOOKING.png").convert_alpha(),
		flags.Flags.FREDDY: pygame.image.load("assets\\6-CAMERAS\\1-STAGE_BONNIE_CHICA.png").convert_alpha()
	},

	flags.Flags.DINING_AREA: {
		"empty": pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA.png").convert_alpha(),
		flags.Flags.BONNIE: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_BONNIE.png").convert_alpha(),
		flags.Flags.CHICA : pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_CHICA.png").convert_alpha(),
		flags.Flags.FREDDY: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_FREDDY.png").convert_alpha(),
		"in_the_dark": {
			flags.Flags.BONNIE: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_BONNIE_2.0.png").convert_alpha(),
			flags.Flags.CHICA : pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_CHICA2.png").convert_alpha(),
		},
	},

	flags.Flags.PIRATE_COVE: {
		"stage1"  : pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE.png").convert_alpha(),
		"stage2"  : pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_FOXY.png").convert_alpha(),
		"stage3"  : pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_FOXY2.png").convert_alpha(),
		"stage4_a": pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_FOXY3.png").convert_alpha(),
		"stage4_b": pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_IT'S_ME.png").convert_alpha(),
	},

	flags.Flags.WEST_HALL: {
		"empty": {
			0: pygame.image.load("assets\\6-CAMERAS\\6-WEST_HALL_CORNER.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\6-WEST_HALL_CORNER_2.png").convert_alpha()
		},
		flags.Flags.BONNIE: pygame.image.load("assets\\6-CAMERAS\\6-WEST_HALL_CORNER_BONNIE.png").convert_alpha(),
	},

	flags.Flags.WEST_HALL_CORNER: {
		"empty"					  : pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL.png").convert_alpha(),
		flags.Flags.BONNIE: {
			0: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_BONNIE.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_BONNIE2.png").convert_alpha(),
			2: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_BONNIE3.png").convert_alpha(),
		},
		flags.Flags.FREDDY: {
			0: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_POSTER_GLITCH.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_GOLDEN_FREDDY.png").convert_alpha()
		},
	},

	flags.Flags.SUPPLY_CLOSET: {
		"empty": pygame.image.load("assets\\6-CAMERAS\\8-SUPPLY_ROOM.png").convert_alpha(),
		flags.Flags.BONNIE: pygame.image.load("assets\\6-CAMERAS\\8-SUPPLY_ROOM_BONNIE.png").convert_alpha()
	},

	flags.Flags.EAST_HALL: {
		"empty": pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER.png").convert_alpha(),
		flags.Flags.CHICA: {
			0: pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_CHICA.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_CHICA2.png").convert_alpha(),
		},
		flags.Flags.FREDDY : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_FREDDY.png").convert_alpha(),
		"children": pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_CHILDREN.png").convert_alpha(),
		"its_me"  : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_IT'S_ME.png").convert_alpha()
	},

	flags.Flags.EAST_HALL_CORNER: {
		"empty"   : pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL.png").convert_alpha(),
		flags.Flags.CHICA: {
			0: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_CHICA.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_CHICA2.png").convert_alpha()
		},
		flags.Flags.FREDDY: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_FREDDY.png").convert_alpha(),
		"news": {
			0: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS2.png").convert_alpha(),
			2: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS3.png").convert_alpha(),
			3: pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS4.png").convert_alpha()
		}, 
	},

	flags.Flags.BACKSTAGE: {
		"empty": pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE.png").convert_alpha(),
		flags.Flags.BONNIE: {
			0: pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE_BONNIE.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE_BONNIE_2.0.png").convert_alpha(),
			2: pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE_LOOKING.png").convert_alpha()
		}
	},

	flags.Flags.KITCHEN: {
		quadro: pygame.image.load(f"assets\\0-STATIC\\{quadro+1}.png").convert_alpha()
		for quadro in range(8)
	},

	flags.Flags.RESTROOMS: {
		"empty": pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS.png").convert_alpha(),
		flags.Flags.CHICA: {
			0: pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS_CHICA.png").convert_alpha(),
			1: pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS_CHICA2.png").convert_alpha(),
		},
		flags.Flags.FREDDY:
			pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS_FREDDY.png").convert_alpha(),
	}
}

rooms_buttons = {
	flags.Flags.SHOW_STAGE	  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\1-CAM 1A.png").convert_alpha(),
	flags.Flags.DINING_AREA	  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\1-CAM 1B.png").convert_alpha(),
	flags.Flags.PIRATE_COVE	  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\1-CAM 1C.png").convert_alpha(),
	flags.Flags.WEST_HALL		  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\2-CAM 2A.png").convert_alpha(),
	flags.Flags.WEST_HALL_CORNER: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\2-CAM 2B.png").convert_alpha(),
	flags.Flags.SUPPLY_CLOSET	  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\3-CAM 3.png" ).convert_alpha(),
	flags.Flags.EAST_HALL		  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\4-CAM 4A.png").convert_alpha(),
	flags.Flags.EAST_HALL_CORNER: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\4-CAM 4B.png").convert_alpha(),
	flags.Flags.BACKSTAGE		  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\5-CAM 5.png" ).convert_alpha(),
	flags.Flags.KITCHEN		  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\6-CAM 6.png" ).convert_alpha(),
	flags.Flags.RESTROOMS		  : pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\7-CAM 7.png" ).convert_alpha()
}

inanimate = {
	flags.Flags.LEFT_BUTTONS_PANEL: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\1-STOPPED.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\2-DOOR.png").convert_alpha(),
		2: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\3-LIGHT.png").convert_alpha(),
		3: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\4-BOTH.png").convert_alpha()
	},

	flags.Flags.RIGHT_BUTTONS_PANEL: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\1-STOPPED.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\2-DOOR.png").convert_alpha(),
		2: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\3-LIGHT.png").convert_alpha(),
		3: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\4-BOTH.png").convert_alpha()
	},

	flags.Flags.LEFT_DOOR: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\STOPPED\\103.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\LEFT\\14.png").convert_alpha()
	},

	flags.Flags.RIGHT_DOOR: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\RIGHT\\1.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\RIGHT\\14.png").convert_alpha()
	}
}

animated = {
	flags.Flags.OFFICE: {
		flags.Flags.BONNIE: {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\2-BONNIE\\{frame+1}.png").convert_alpha()
			for frame in range(11)
		},
		flags.Flags.CHICA : {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\3-CHICA\\{frame+1}.png").convert_alpha()
			for frame in range(16)
		},
		flags.Flags.FREDDY: {
			"normal": {
				frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\1-FREDDY\\{frame+1}.png").convert_alpha()
				for frame in range(29)
			},
			"no_power": {
				frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\1-FREDDY\\{frame+1}.png").convert_alpha()
				for frame in range(20)
			}
		},
		flags.Flags.FOXY  : {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\FOXY\\{frame+1}.png").convert_alpha()
			for frame in range(20)
		},
	},

	flags.Flags.FAN: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\FAN\\{frame+1}.png").convert_alpha()\
		for frame in range(3)
	},

	flags.Flags.LEFT_DOOR: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\DOORS\\LEFT\\{frame+1}.png").convert_alpha()
		for frame in range(14)
	},

	flags.Flags.RIGHT_DOOR: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\DOORS\\RIGHT\\{frame+1}.png").convert_alpha()
		for frame in range(14)
	},

	flags.Flags.CAMERA: {
		frame: pygame.image.load(f"assets\\6-CAMERAS\\MONITOR_ANIMATION\\{frame+1}.png").convert_alpha()
		for frame in range(11)
	},

	flags.Flags.CAMERA_TRANSITION: {
		frame: pygame.image.load(f"assets\\6-CAMERAS\\WHITE_BARS\\{frame+1}.png").convert_alpha()
		for frame in range(7)
	},
}
