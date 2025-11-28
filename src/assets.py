import pygame
import entidades


backgrounds = {
	entidades.Entidades.OFFICE: {
		"vazio": {
			0: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE.png").convert_alpha(),
			1: pygame.image.load("assets\\3-THE_OFFICE\\LEFT_LIGHT.png").convert_alpha(),
			2: pygame.image.load("assets\\3-THE_OFFICE\\RIGHT_LIGHT.png").convert_alpha()
		},
		"comAnimatronicos": {
			0: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE_BONNIE.png").convert_alpha(),
			1: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE_CHICA.png").convert_alpha()
		},
		"semEnergia"   : pygame.image.load("assets\\3-THE_OFFICE\\LIGHTS_OUT\\304.png").convert_alpha(),
		"freddysJingle": pygame.image.load("assets\\3-THE_OFFICE\\LIGHTS_OUT\\305.png").convert_alpha() 
	},

	entidades.Entidades.SHOW_STAGE: {
		"vazio"			 : pygame.image.load("assets\\6-CAMERAS\\1-STAGE_ALL.png").convert_alpha(),
		"comTodos"		 : pygame.image.load("assets\\6-CAMERAS\\1-STAGE.png").convert_alpha(),
		"comTodosOlhando": pygame.image.load("assets\\6-CAMERAS\\1-STAGE_LOOKING.png").convert_alpha(),
		"freddyOlhando"  : pygame.image.load("assets\\6-CAMERAS\\1-STAGE_FREDDY_LOOKING.png").convert_alpha(),
		"semBonnie"		 : pygame.image.load("assets\\6-CAMERAS\\1-STAGE_BONNIE.png").convert_alpha(),
		"semChica"		 : pygame.image.load("assets\\6-CAMERAS\\1-STAGE_CHICA.png").convert_alpha(),
		"semBonnieChica" : pygame.image.load("assets\\6-CAMERAS\\1-STAGE_BONNIE_CHICA.png").convert_alpha()
	},

	entidades.Entidades.DINING_AREA: {
		"vazio"			: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA.png").convert_alpha(),
		"bonnie"		: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_BONNIE.png").convert_alpha(),
		"bonnieNoEscuro": pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_BONNIE_2.0.png").convert_alpha(),
		"chica"			: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_CHICA.png").convert_alpha(),
		"chicaNoEscuro" : pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_CHICA2.png").convert_alpha(),
		"freddy"		: pygame.image.load("assets\\6-CAMERAS\\2-DINING_AREA_FREDDY.png").convert_alpha(),
	},

	entidades.Entidades.PIRATE_COVE: {
		"estagio1"  : pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE.png").convert_alpha(),
		"estagio2"  : pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_FOXY.png").convert_alpha(),
		"estagio3"  : pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_FOXY2.png").convert_alpha(),
		"estagio4_1": pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_FOXY3.png").convert_alpha(),
		"estagio4_2": pygame.image.load("assets\\6-CAMERAS\\3-PIRATE_COVE_IT'S_ME.png").convert_alpha(),
	},

	entidades.Entidades.WEST_HALL: {
		"vazio"		: pygame.image.load("assets\\6-CAMERAS\\6-WEST_HALL_CORNER_2.png").convert_alpha(),
		"luzApagada": pygame.image.load("assets\\6-CAMERAS\\6-WEST_HALL_CORNER.png").convert_alpha(),
		"bonnie"	: pygame.image.load("assets\\6-CAMERAS\\6-WEST_HALL_CORNER_BONNIE.png").convert_alpha(),
	},

	entidades.Entidades.WEST_HALL_CORNER: {
		"vazio"				: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL.png").convert_alpha(),
		"bonnie1"			: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_BONNIE.png").convert_alpha(),
		"bonnie2"			: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_BONNIE2.png").convert_alpha(),
		"bonnie3"			: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_BONNIE3.png").convert_alpha(),
		"goldenFreddyPoster": pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_GOLDEN_FREDDY.png").convert_alpha(),
		"freddyPoster"		: pygame.image.load("assets\\6-CAMERAS\\9-WEST_HALL_POSTER_GLITCH.png").convert_alpha()
	},

	entidades.Entidades.SUPPLY_CLOSET: {
		"vazio" : pygame.image.load("assets\\6-CAMERAS\\8-SUPPLY_ROOM.png").convert_alpha(),
		"bonnie": pygame.image.load("assets\\6-CAMERAS\\8-SUPPLY_ROOM_BONNIE.png").convert_alpha()
	},

	entidades.Entidades.EAST_HALL: {
		"vazio"  : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER.png").convert_alpha(),
		"chica1" : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_CHICA.png").convert_alpha(),
		"chica2" : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_CHICA2.png").convert_alpha(),
		"freddy" : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_FREDDY.png").convert_alpha(),
		"crianca": pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_CHILDREN.png").convert_alpha(),
		"souEu"  : pygame.image.load("assets\\6-CAMERAS\\7-EAST_HALL_CORNER_IT'S_ME.png").convert_alpha()
	},

	entidades.Entidades.EAST_HALL_CORNER: {
		"vazio"    : pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL.png").convert_alpha(),
		"chica1"   : pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_CHICA.png").convert_alpha(),
		"chica2"   : pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_CHICA2.png").convert_alpha(),
		"freddy"   : pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_FREDDY.png").convert_alpha(),
		"noticias1": pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS.png").convert_alpha(),
		"noticias2": pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS2.png").convert_alpha(),
		"noticias3": pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS3.png").convert_alpha(),
		"noticias4": pygame.image.load("assets\\6-CAMERAS\\10-EAST_HALL_NEWS4.png").convert_alpha()
	},

	entidades.Entidades.BACKSTAGE: {
		"vazio"		  : pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE.png").convert_alpha(),
		"bonnie1"	  : pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE_BONNIE.png").convert_alpha(),
		"bonnie2"	  : pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE_BONNIE_2.0.png").convert_alpha(),
		"bonnieCabeca": pygame.image.load("assets\\6-CAMERAS\\5-BACKSTAGE_LOOKING.png").convert_alpha()
	},

	entidades.Entidades.KITCHEN: {
		quadro: pygame.image.load(f"assets\\0-STATIC\\{quadro+1}.png").convert_alpha()
		for quadro in range(8)
	},

	entidades.Entidades.RESTROOMS: {
		"vazio" : pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS.png").convert_alpha(),
		"chica1": pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS_CHICA.png").convert_alpha(),
		"chica2": pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS_CHICA2.png").convert_alpha(),
		"freddy": pygame.image.load("assets\\6-CAMERAS\\4-RESTROOMS_FREDDY.png").convert_alpha(),
	}
}

botoesSalas = {
	entidades.Entidades.SHOW_STAGE		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\1-CAM 1A.png").convert_alpha(),
	entidades.Entidades.DINING_AREA		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\1-CAM 1B.png").convert_alpha(),
	entidades.Entidades.PIRATE_COVE		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\1-CAM 1C.png").convert_alpha(),
	entidades.Entidades.WEST_HALL		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\2-CAM 2A.png").convert_alpha(),
	entidades.Entidades.WEST_HALL_CORNER: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\2-CAM 2B.png").convert_alpha(),
	entidades.Entidades.SUPPLY_CLOSET	: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\3-CAM 3.png" ).convert_alpha(),
	entidades.Entidades.EAST_HALL		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\4-CAM 4A.png").convert_alpha(),
	entidades.Entidades.EAST_HALL_CORNER: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\4-CAM 4B.png").convert_alpha(),
	entidades.Entidades.BACKSTAGE		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\5-CAM 5.png" ).convert_alpha(),
	entidades.Entidades.KITCHEN			: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\6-CAM 6.png" ).convert_alpha(),
	entidades.Entidades.RESTROOMS		: pygame.image.load("assets\\6-CAMERAS\\CAM_BUTTONS\\7-CAM 7.png" ).convert_alpha()
}


inanimados = {
	entidades.Entidades.PAINEL_BOTOES_ESQUERDOS: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\1-STOPPED.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\2-DOOR.png").convert_alpha(),
		2: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\3-LIGHT.png").convert_alpha(),
		3: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\4-BOTH.png").convert_alpha()
	},

	entidades.Entidades.PAINEL_BOTOES_DIREITOS: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\1-STOPPED.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\2-DOOR.png").convert_alpha(),
		2: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\3-LIGHT.png").convert_alpha(),
		3: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\4-BOTH.png").convert_alpha()
	},

	entidades.Entidades.PORTA_ESQUERDA: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\STOPPED\\103.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\LEFT\\14.png").convert_alpha()
	},

	entidades.Entidades.PORTA_DIREITA: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\RIGHT\\1.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\RIGHT\\14.png").convert_alpha()
	}
}

animados = {
	entidades.Entidades.OFFICE: {
		"bonnie": {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\2-BONNIE\\{frame+1}.png").convert_alpha()
			for frame in range(11)
		},
		"chica" : {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\3-CHICA\\{frame+1}.png").convert_alpha()
			for frame in range(16)
		},
		"freddy": {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\1-FREDDY\\{frame+1}.png").convert_alpha()
			for frame in range(29)
		},
		"freddy_sem_energia": {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\1-FREDDY\\{frame+1}.png").convert_alpha()
			for frame in range(20)
		},
		"foxy"  : {
			frame: pygame.image.load(f"assets\\3-THE_OFFICE\\FOXY\\{frame+1}.png").convert_alpha()
			for frame in range(20)
		},
	},

	entidades.Entidades.VENTILADOR: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\FAN\\{frame+1}.png").convert_alpha()\
		for frame in range(3)
	},

	entidades.Entidades.PORTA_ESQUERDA: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\DOORS\\LEFT\\{frame+1}.png").convert_alpha()
		for frame in range(14)
	},

	entidades.Entidades.PORTA_DIREITA: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\DOORS\\RIGHT\\{frame+1}.png").convert_alpha()
		for frame in range(14)
	},

	entidades.Entidades.CAMERA: {
		frame: pygame.image.load(f"assets\\6-CAMERAS\\MONITOR_ANIMATION\\{frame+1}.png").convert_alpha()
		for frame in range(11)
	},

	entidades.Entidades.CAMERA_TRANSICAO: {
		frame: pygame.image.load(f"assets\\6-CAMERAS\\WHITE_BARS\\{frame+1}.png").convert_alpha()
		for frame in range(7)
	},
}
