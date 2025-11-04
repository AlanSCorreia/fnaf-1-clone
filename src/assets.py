import pygame
import entidades

assets = {
	entidades.Id.Escritorio: {
		"vazio": {
			0: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE.png").convert_alpha(),
			1: pygame.image.load("assets\\3-THE_OFFICE\\LEFT_LIGHT.png").convert_alpha(),
			2: pygame.image.load("assets\\3-THE_OFFICE\\RIGHT_LIGHT.png").convert_alpha()
		},
		"com_animatronicos": {
			0: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE_BONNIE.png").convert_alpha(),
			1: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE_CHICA.png").convert_alpha()
		},
		"jumpscares": {
			"bonnie": {
				frame-1: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\2-BONNIE\\{frame}.png").convert_alpha()
				for frame in range(1, 12)
			},
			"chica" : {
				frame-1: pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\3-CHICA\\{frame}.png").convert_alpha()
				for frame in range(1, 17)
			},
			"freddy": {
				frame-1 : pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\1-FREDDY\\{frame}.png").convert_alpha()
				for frame in range(1, 30)
			},
			"freddy_sem_energia": {
				frame-1 : pygame.image.load(f"assets\\3-THE_OFFICE\\JUMPSCARES\\1-FREDDY\\{frame}.png").convert_alpha()
				for frame in range(1, 21)
			},
			"foxy"  : {
				frame-1 : pygame.image.load(f"assets\\3-THE_OFFICE\\FOXY\\{frame}.png").convert_alpha()
				for frame in range(1, 21)
			}
		},
		"sem_energia": pygame.image.load("assets\\3-THE_OFFICE\\LIGHTS_OUT\\304.png").convert_alpha(),
		"freddy_jingle": pygame.image.load("assets\\3-THE_OFFICE\\LIGHTS_OUT\\305.png").convert_alpha()
	},

	entidades.Id.Ventilador: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\FAN\\{frame+1}.png").convert_alpha()\
			for frame in range(3)
	},

	entidades.Id.PortaEsquerda: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\DOORS\\LEFT\\{frame}.png").convert_alpha() for frame in range(1, 15)
	},

	entidades.Id.PainelDeBotoesEsquerdo: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\1-STOPPED.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\2-DOOR.png").convert_alpha(),
		2: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\3-LIGHT.png").convert_alpha(),
		3: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\LEFT\\4-BOTH.png").convert_alpha()
	},

	entidades.Id.PortaDireita: {
		frame: pygame.image.load(f"assets\\3-THE_OFFICE\\DOORS\\RIGHT\\{frame}.png").convert_alpha() for frame in range(1, 15)
	},

	entidades.Id.PainelDeBotoesDireito: {
		0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\1-STOPPED.png").convert_alpha(),
		1: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\2-DOOR.png").convert_alpha(),
		2: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\3-LIGHT.png").convert_alpha(),
		3: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\BUTTONS\\RIGHT\\4-BOTH.png").convert_alpha()
	}
}

portaEsquerdaUpdate = {0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\STOPPED\\103.png").convert_alpha()}
assets[entidades.Id.PortaEsquerda] = {**portaEsquerdaUpdate, **assets[entidades.Id.PortaEsquerda]}

portaDireitaUpdate = {0: pygame.image.load("assets\\3-THE_OFFICE\\DOORS\\STOPPED\\104.png").convert_alpha()}
assets[entidades.Id.PortaDireita] = {**portaDireitaUpdate, **assets[entidades.Id.PortaDireita]}
