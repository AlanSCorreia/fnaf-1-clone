import pygame
import entidades

assets = {
	entidades.Id.Escritorio: {
		"vazio": {
			0: pygame.image.load("assets\\3-THE_OFFICE\\1-OFFICE.png").convert_alpha()
		},
		"nao_vazio": {
			
		}
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
