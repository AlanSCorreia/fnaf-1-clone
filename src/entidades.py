from enum import Enum, IntFlag, auto

import sistemas


class Entidades(Enum):
	MOUSE 				   = auto()
	OFFICE	   		   	   = auto()
	SHOW_STAGE 	   		   = auto()
	DINING_AREA 	   	   = auto()
	PIRATE_COVE 	   	   = auto()
	WEST_HALL 	   		   = auto()
	WEST_HALL_CORNER	   = auto()
	SUPPLY_CLOSET		   = auto()
	EAST_HALL 	   		   = auto()
	EAST_HALL_CORNER	   = auto()
	BACKSTAGE 	   		   = auto()
	KITCHEN 	   		   = auto()
	RESTROOMS 	   		   = auto()

	VENTILADOR 			   = auto()
	
	# Portas
	PORTA_ESQUERDA 		   = auto()
	PORTA_DIREITA 		   = auto()

	# Painel de Botões
	PAINEL_BOTOES_ESQUERDOS = auto()
	PAINEL_BOTOES_DIREITOS  = auto()
	
	# Botões das Portas
	BOTAO_PORTA_ESQUERDA   = auto()
	BOTAO_PORTA_DIREITA    = auto()

	# Botões das Luzes
	BOTAO_LUZ_ESQUERDA 	   = auto()
	BOTAO_LUZ_DIREITA 	   = auto()

	# Animatronicos
	# Freddy				   = auto()
	# Bonnie				   = auto()
	# Chica				   = auto()
	# Foxy				   = auto()

	CAMERA			   	   = auto()
	CAMERA_TRANSICAO	   = auto()
	CAMERA_MOVIMENTO	   = auto()


class Bitmasks(IntFlag):
	SURFACE		  = auto()
	RECTANGLE	  = auto()
	BACKGROUND	  = auto()
	ESTATICO	  = auto()
	ESTADO 		  = auto()
	BOTAO 		  = auto()
	QUADRO 		  = auto()
	CAMERA 		  = auto()
	QUADRO_APENAS = auto()


# componentesMask = {
# 	"background"	: 1 << 0,
# 	"surface"  	    : 1 << 1,
# 	"rectangle"     : 1 << 2,
# 	"estatico"		: 1 << 3,
# 	"estado"     	: 1 << 4,
# 	"botao"			: 1 << 5,
# 	"quadro"        : 1 << 6,
# 	# "animatronico"  : 1 << 7,
# 	"camera"		: 1 << 8,
# 	"quadroApenas"  : 1 << 9
# }

entidadesMasks = {
	Entidades.MOUSE					 : Bitmasks.ESTADO,
	Entidades.OFFICE				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.BACKGROUND,
	Entidades.SHOW_STAGE			 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.DINING_AREA			 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.PIRATE_COVE			 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.WEST_HALL				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.WEST_HALL_CORNER		 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.SUPPLY_CLOSET			 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.EAST_HALL				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.EAST_HALL_CORNER		 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.BACKSTAGE				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.KITCHEN				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.RESTROOMS				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.BOTAO  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entidades.VENTILADOR			 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.QUADRO,
	Entidades.PORTA_ESQUERDA 		 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.QUADRO,
	Entidades.PORTA_DIREITA		     : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.QUADRO,
	Entidades.PAINEL_BOTOES_ESQUERDOS: Bitmasks.SURFACE   | Bitmasks.RECTANGLE,
	Entidades.PAINEL_BOTOES_DIREITOS : Bitmasks.SURFACE   | Bitmasks.RECTANGLE,
	Entidades.BOTAO_PORTA_ESQUERDA   : Bitmasks.RECTANGLE | Bitmasks.ESTADO    | Bitmasks.BOTAO,
	Entidades.BOTAO_PORTA_DIREITA	 : Bitmasks.RECTANGLE | Bitmasks.ESTADO    | Bitmasks.BOTAO,
	Entidades.BOTAO_LUZ_ESQUERDA	 : Bitmasks.RECTANGLE | Bitmasks.ESTADO    | Bitmasks.BOTAO,
	Entidades.BOTAO_LUZ_DIREITA	 	 : Bitmasks.RECTANGLE | Bitmasks.ESTADO    | Bitmasks.BOTAO,
	Entidades.CAMERA				 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.ESTADO | Bitmasks.QUADRO 		| Bitmasks.QUADRO_APENAS | Bitmasks.ESTATICO,
	Entidades.CAMERA_TRANSICAO		 : Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.QUADRO | Bitmasks.QUADRO_APENAS | Bitmasks.ESTATICO,
	Entidades.CAMERA_MOVIMENTO		 : Bitmasks.ESTADO
}

estaticosSurfaces = sistemas.filtrarEntidadesPorComponentes(Entidades,
															[Bitmasks.SURFACE, Bitmasks.ESTATICO],
															[Bitmasks.CAMERA],
															entidadesMasks)

inanimadosSurfaces = sistemas.filtrarEntidadesPorComponentes(Entidades,
															 [Bitmasks.SURFACE],
															 [Bitmasks.QUADRO, Bitmasks.ESTATICO, Bitmasks.BACKGROUND],
															 entidadesMasks)

inanimadosRectangles = sistemas.filtrarEntidadesPorComponentes(Entidades,
															   [Bitmasks.RECTANGLE],
															   [Bitmasks.QUADRO, Bitmasks.ESTATICO, Bitmasks.BACKGROUND],
															   entidadesMasks)

animadosSurfaces = sistemas.filtrarEntidadesPorComponentes(Entidades,
														   [Bitmasks.QUADRO],
														   [Bitmasks.ESTATICO],
														   entidadesMasks)

animadosRectangles = sistemas.filtrarEntidadesPorComponentes(Entidades,
															 [Bitmasks.QUADRO],
															 [Bitmasks.ESTATICO],
															 entidadesMasks)

estados = sistemas.filtrarEntidadesPorComponentes(Entidades,
												  [Bitmasks.ESTADO],
												  None,
												  entidadesMasks)

painelDeBotoesEsquerdo = [Entidades.PAINEL_BOTOES_ESQUERDOS,
						  Entidades.BOTAO_PORTA_ESQUERDA,
						  Entidades.BOTAO_LUZ_ESQUERDA]

painelDeBotoesDireito = [Entidades.PAINEL_BOTOES_DIREITOS,
						 Entidades.BOTAO_PORTA_DIREITA,
						 Entidades.BOTAO_LUZ_DIREITA]

quadros = sistemas.filtrarEntidadesPorComponentes(Entidades,
												  [Bitmasks.QUADRO],
												  None,
												  entidadesMasks)

camera = sistemas.filtrarEntidadesPorComponentes(Entidades,
												 [Bitmasks.CAMERA],
												 None,
												 entidadesMasks)

botoesSalas = sistemas.filtrarEntidadesPorComponentes(Entidades,
													  [Bitmasks.BOTAO, Bitmasks.CAMERA],
													  None,
													  entidadesMasks)