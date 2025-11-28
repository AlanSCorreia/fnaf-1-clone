from enum import Enum, auto

import pygame

import entidades
import assets


class MomentosDoJogo(Enum):
	MENU_PRINCIPAL    = auto()
	MENU_CUSTOM_NIGHT = auto()
	EM_JOGO		  	  = auto()


class MomentosEmJogo(Enum):
	SEM_CAMERA		  = auto()
	COM_CAMERA 		  = auto()
	FIM_DE_JOGO		  = auto()


class Noites(Enum):
	PRIMEIRA = auto()
	SEGUNDA  = auto()
	TERCEIRA = auto()
	QUARTA   = auto()
	QUINTA   = auto()
	SEXTA    = auto()


class Estado:
	def __init__(self,
			  	 intervaloDeDisponibilidade: int,
				 estado=False) -> None:

		self.estado = estado
		self.estaDisponivel = True
		self.ultimoTempoDisponivel = 0
		self.intervaloDeDisponibilidade = intervaloDeDisponibilidade


class Quadros:
	def __init__(self,
			  	 animacaoEstaOcorrendo : bool,
				 estaRepetindo		   : bool,
				 estaRevertendo		   : bool,
				 precisaReiniciar	   : bool,
				 quadroAtual		   : int,
				 tempoDoUltimoQuadro   : float,
				 intervaloEntreQuadros : float) -> None:

		self.animacaoEstaOcorrendo = animacaoEstaOcorrendo
		self.estaRepetindo		   = estaRepetindo
		self.estaRevertendo		   = estaRevertendo
		self.precisaReiniciar	   = precisaReiniciar
		self.quadroAtual 		   = quadroAtual
		self.tempoDoUltimoQuadro   = tempoDoUltimoQuadro
		self.intervaloEntreQuadros = intervaloEntreQuadros


class Animatronico:
	def __init__(self,
				 nivelDeDificuldade: int,
				 intervaloOportunidadeDeMovimento: float,
				 rota: dict[int, str | list[str]]) -> None:

		self.nivelDeDificuldade = nivelDeDificuldade
		self.intervaloOportunidadeDeMovimento = intervaloOportunidadeDeMovimento
		self.rota = rota


globais = {	
	"momentoDoJogo": {"atual": MomentosDoJogo.EM_JOGO},

	"momentoEmJogo": {"atual": MomentosEmJogo.SEM_CAMERA},

	"cameraBackground": {"atual": entidades.Entidades.SHOW_STAGE},

	"noiteAtual": {"atual": Noites.PRIMEIRA},

	"estadoMouse": {
		"estaDisponivel": True,
		"ultimoClick": 0,
		"intervaloEntreClicks": 100
	},

	"limitesDeslocamentoCamera": {
		"minimo": -320,
		"maximo": 10
	},

	"deslocamentoSemCamera": {
		"vertical": 0,
		"base": 0
	},

	"deslocamentoComCamera": {
		"vertical": 0,
		"base": 0
	}
}

surfaces = {
	"backgrounds": {
		entidades.Entidades.OFFICE			: assets.backgrounds[entidades.Entidades.OFFICE		 	 ]["vazio"	 ][0],
		entidades.Entidades.SHOW_STAGE		: assets.backgrounds[entidades.Entidades.SHOW_STAGE 	 ]["comTodos"],
		entidades.Entidades.DINING_AREA		: assets.backgrounds[entidades.Entidades.DINING_AREA	 ]["vazio"	 ],
		entidades.Entidades.PIRATE_COVE		: assets.backgrounds[entidades.Entidades.PIRATE_COVE	 ]["estagio1"],
		entidades.Entidades.WEST_HALL		: assets.backgrounds[entidades.Entidades.WEST_HALL  	 ]["vazio"	 ],
		entidades.Entidades.WEST_HALL_CORNER: assets.backgrounds[entidades.Entidades.WEST_HALL_CORNER]["vazio"	 ],
		entidades.Entidades.SUPPLY_CLOSET	: assets.backgrounds[entidades.Entidades.SUPPLY_CLOSET	 ]["vazio"	 ],
		entidades.Entidades.EAST_HALL		: assets.backgrounds[entidades.Entidades.EAST_HALL		 ]["vazio"	 ],
		entidades.Entidades.EAST_HALL_CORNER: assets.backgrounds[entidades.Entidades.EAST_HALL_CORNER]["vazio"	 ],
		entidades.Entidades.BACKSTAGE		: assets.backgrounds[entidades.Entidades.BACKSTAGE	 	 ]["vazio"	 ],
		entidades.Entidades.KITCHEN			: assets.backgrounds[entidades.Entidades.KITCHEN		 ][0],
		entidades.Entidades.RESTROOMS		: assets.backgrounds[entidades.Entidades.RESTROOMS	 	 ]["vazio"	 ]
	},
	"inanimados": {
		entidades.Entidades.PAINEL_BOTOES_ESQUERDOS: assets.inanimados[entidades.Entidades.PAINEL_BOTOES_ESQUERDOS][0],
		entidades.Entidades.PAINEL_BOTOES_DIREITOS : assets.inanimados[entidades.Entidades.PAINEL_BOTOES_DIREITOS ][0],
	},
	"animados": {
		entidades.Entidades.VENTILADOR    : assets.animados[entidades.Entidades.VENTILADOR	  ][0],
		entidades.Entidades.PORTA_ESQUERDA: assets.animados[entidades.Entidades.PORTA_ESQUERDA][0],
		entidades.Entidades.PORTA_DIREITA : assets.animados[entidades.Entidades.PORTA_DIREITA ][0],
	},
	"estaticos": {
		entidades.Entidades.CAMERA		    : assets.animados[entidades.Entidades.CAMERA		  ][0],
		entidades.Entidades.CAMERA_TRANSICAO: assets.animados[entidades.Entidades.CAMERA_TRANSICAO][0]
	},
	"botoesSalas": {
		entidades.Entidades.SHOW_STAGE 		: assets.botoesSalas[entidades.Entidades.SHOW_STAGE		 ],
		entidades.Entidades.DINING_AREA		: assets.botoesSalas[entidades.Entidades.DINING_AREA	 ],
		entidades.Entidades.PIRATE_COVE		: assets.botoesSalas[entidades.Entidades.PIRATE_COVE	 ],
		entidades.Entidades.WEST_HALL  		: assets.botoesSalas[entidades.Entidades.WEST_HALL		 ],
		entidades.Entidades.WEST_HALL_CORNER: assets.botoesSalas[entidades.Entidades.WEST_HALL_CORNER],
		entidades.Entidades.SUPPLY_CLOSET	: assets.botoesSalas[entidades.Entidades.SUPPLY_CLOSET	 ],
		entidades.Entidades.EAST_HALL		: assets.botoesSalas[entidades.Entidades.EAST_HALL		 ],
		entidades.Entidades.EAST_HALL_CORNER: assets.botoesSalas[entidades.Entidades.EAST_HALL_CORNER],
		entidades.Entidades.BACKSTAGE		: assets.botoesSalas[entidades.Entidades.BACKSTAGE		 ],
		entidades.Entidades.KITCHEN			: assets.botoesSalas[entidades.Entidades.KITCHEN		 ],
		entidades.Entidades.RESTROOMS		: assets.botoesSalas[entidades.Entidades.RESTROOMS		 ]
	}
}

rectangles = {
	"backgrounds": {
		entidades.Entidades.OFFICE		  	: assets.backgrounds[entidades.Entidades.OFFICE	 	 	 ]["vazio"	 ][0].get_rect(topleft=(0, 0)),
		entidades.Entidades.SHOW_STAGE	  	: assets.backgrounds[entidades.Entidades.SHOW_STAGE 	 ]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.DINING_AREA	  	: assets.backgrounds[entidades.Entidades.DINING_AREA	 ]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.PIRATE_COVE	  	: assets.backgrounds[entidades.Entidades.PIRATE_COVE	 ]["estagio1"].get_rect(topleft=(0, 0)),
		entidades.Entidades.WEST_HALL	  	: assets.backgrounds[entidades.Entidades.WEST_HALL  	 ]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.WEST_HALL_CORNER: assets.backgrounds[entidades.Entidades.WEST_HALL_CORNER]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.SUPPLY_CLOSET  	: assets.backgrounds[entidades.Entidades.SUPPLY_CLOSET	 ]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.EAST_HALL	  	: assets.backgrounds[entidades.Entidades.EAST_HALL		 ]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.EAST_HALL_CORNER: assets.backgrounds[entidades.Entidades.EAST_HALL_CORNER]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.BACKSTAGE	  	: assets.backgrounds[entidades.Entidades.BACKSTAGE	 	 ]["vazio"	 ].get_rect(topleft=(0, 0)),
		entidades.Entidades.KITCHEN		  	: assets.backgrounds[entidades.Entidades.KITCHEN		 ][0].get_rect(topleft=(0, 0)),
		entidades.Entidades.RESTROOMS	  	: assets.backgrounds[entidades.Entidades.RESTROOMS	 	 ]["vazio"	 ].get_rect(topleft=(0, 0))
	},
	"inanimados": {
		entidades.Entidades.PAINEL_BOTOES_ESQUERDOS: assets.inanimados[entidades.Entidades.PAINEL_BOTOES_ESQUERDOS][0].get_rect(topleft=(  15, 315)),
		entidades.Entidades.PAINEL_BOTOES_DIREITOS : assets.inanimados[entidades.Entidades.PAINEL_BOTOES_DIREITOS ][0].get_rect(topleft=(1465, 315)),
		entidades.Entidades.BOTAO_PORTA_ESQUERDA   : pygame.Rect((  45, 369), (40, 55)),
		entidades.Entidades.BOTAO_PORTA_DIREITA    : pygame.Rect((1488, 369), (40, 55)),
		entidades.Entidades.BOTAO_LUZ_ESQUERDA	   : pygame.Rect((  45, 447), (40, 55)),
		entidades.Entidades.BOTAO_LUZ_DIREITA	   : pygame.Rect((1488, 447), (40, 55)),
	},
	"animados": {
		entidades.Entidades.VENTILADOR    : assets.animados[entidades.Entidades.VENTILADOR    ][0].get_rect(topleft=( 783, 303)),
		entidades.Entidades.PORTA_ESQUERDA: assets.animados[entidades.Entidades.PORTA_ESQUERDA][0].get_rect(topleft=(  70,  30)),
		entidades.Entidades.PORTA_DIREITA : assets.animados[entidades.Entidades.PORTA_DIREITA ][0].get_rect(topleft=(1265,  30)),
	},
	"estaticos": {
		entidades.Entidades.CAMERA		    : assets.animados[entidades.Entidades.CAMERA		  ][0].get_rect(topleft=(0,0)),
		entidades.Entidades.CAMERA_TRANSICAO: assets.animados[entidades.Entidades.CAMERA_TRANSICAO][0].get_rect(topleft=(0,0)),
	},
	"botoesSalas": {
		entidades.Entidades.SHOW_STAGE 		: assets.botoesSalas[entidades.Entidades.SHOW_STAGE		 ].get_rect(topleft=( 965,  364)),
		entidades.Entidades.DINING_AREA		: assets.botoesSalas[entidades.Entidades.DINING_AREA	 ].get_rect(topleft=( 920,  400)),
		entidades.Entidades.PIRATE_COVE		: assets.botoesSalas[entidades.Entidades.PIRATE_COVE	 ].get_rect(topleft=( 895,  475)),
		entidades.Entidades.WEST_HALL  		: assets.botoesSalas[entidades.Entidades.WEST_HALL		 ].get_rect(topleft=( 950,  620)),
		entidades.Entidades.WEST_HALL_CORNER: assets.botoesSalas[entidades.Entidades.WEST_HALL_CORNER].get_rect(topleft=( 950,  650)),
		entidades.Entidades.SUPPLY_CLOSET	: assets.botoesSalas[entidades.Entidades.SUPPLY_CLOSET	 ].get_rect(topleft=( 875,  580)),
		entidades.Entidades.EAST_HALL		: assets.botoesSalas[entidades.Entidades.EAST_HALL		 ].get_rect(topleft=(1055,  620)),
		entidades.Entidades.EAST_HALL_CORNER: assets.botoesSalas[entidades.Entidades.EAST_HALL_CORNER].get_rect(topleft=(1055,  650)),
		entidades.Entidades.BACKSTAGE		: assets.botoesSalas[entidades.Entidades.BACKSTAGE		 ].get_rect(topleft=( 840,  415)),
		entidades.Entidades.KITCHEN			: assets.botoesSalas[entidades.Entidades.KITCHEN		 ].get_rect(topleft=(1150,  570)),
		entidades.Entidades.RESTROOMS		: assets.botoesSalas[entidades.Entidades.RESTROOMS		 ].get_rect(topleft=(1150,  440))
	}
}

estados = {
	entidades.Entidades.SHOW_STAGE			: Estado(500),
	entidades.Entidades.DINING_AREA			: Estado(500),
	entidades.Entidades.PIRATE_COVE			: Estado(500),
	entidades.Entidades.WEST_HALL			: Estado(500),
	entidades.Entidades.WEST_HALL_CORNER	: Estado(500),
	entidades.Entidades.SUPPLY_CLOSET		: Estado(500),
	entidades.Entidades.EAST_HALL			: Estado(500),
	entidades.Entidades.EAST_HALL_CORNER	: Estado(500),
	entidades.Entidades.BACKSTAGE			: Estado(500),
	entidades.Entidades.KITCHEN				: Estado(500),
	entidades.Entidades.RESTROOMS			: Estado(500),
	entidades.Entidades.PORTA_ESQUERDA		: Estado(500),
	entidades.Entidades.PORTA_DIREITA 		: Estado(500),
	entidades.Entidades.BOTAO_PORTA_ESQUERDA: Estado(500),
	entidades.Entidades.BOTAO_PORTA_DIREITA : Estado(500),
	entidades.Entidades.BOTAO_LUZ_ESQUERDA  : Estado(250),
	entidades.Entidades.BOTAO_LUZ_DIREITA   : Estado(250),
	entidades.Entidades.CAMERA 	 		  	: Estado(500),
	entidades.Entidades.CAMERA_MOVIMENTO	: Estado(1000, True)
}

quadros = {
	entidades.Entidades.VENTILADOR      : Quadros( True,  True, False, False, 0, 0, 25),
	entidades.Entidades.PORTA_ESQUERDA  : Quadros(False, False, False, False, 0, 0, 25),
	entidades.Entidades.PORTA_DIREITA   : Quadros(False, False, False, False, 0, 0, 25),
	entidades.Entidades.CAMERA	        : Quadros(False, False, False, False, 0, 0, 25),
	entidades.Entidades.CAMERA_TRANSICAO: Quadros(False, False, False,  True, 0, 0, 25)
}

# animatronicos = {
# 	entidades.Id.Freddy: Animatronico(0, 3.02, {}),
# 	entidades.Id.Bonnie: Animatronico(0, 4.97, {}),
# 	entidades.Id.Chica : Animatronico(0, 4.98, {}),
# 	entidades.Id.Foxy  : Animatronico(0, 5.02, {})
# }

localizacaoDosAnimatronicos = {
	"CAM A1": [],
}