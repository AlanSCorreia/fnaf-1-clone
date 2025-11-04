from enum import Enum, auto


class Id(Enum):
	Escritorio 			   = auto()
	Ventilador 			   = auto()
	
	# Portas
	PortaEsquerda 		   = auto()
	PortaDireita 		   = auto()

	# Painel de Botões
	PainelDeBotoesEsquerdo = auto()
	PainelDeBotoesDireito  = auto()
	
	# Botões Esquerdos
	BotaoDaPortaEsquerda   = auto()
	BotaoDaLuzEsquerda 	   = auto()

	# Botões Direitos
	BotaoDaPortaDireita    = auto()
	BotaoDaLuzDireita 	   = auto()

	# Animatronicos
	# Freddy				   = auto()
	# Bonnie				   = auto()
	# Chica				   = auto()
	# Foxy				   = auto()

	# Salas
	# ShowStage   		   = auto()
	# DiningArea   		   = auto()
	# PirateCove   		   = auto()
	# WestHall   		   	   = auto()
	# WestHallCorner   	   = auto()
	# SupplyCloset   	   	   = auto()
	# EastHall   		   	   = auto()
	# EastHallCorner   	   = auto()
	# Backstage   		   = auto()
	# Kitchen   		   	   = auto()
	# Restrooms   		   = auto()


componentesMask = {
	"surface"  	    : 1 << 0,
	"rectangle"     : 1 << 1,
	"botaoDaPorta"  : 1 << 2,
	"botaoDaLuz"    : 1 << 3,
	"frames"        : 1 << 4,
	# "animatronico"  : 1 << 5
}


entidadesMask = {
	Id.Escritorio			 : componentesMask["surface"  ] | componentesMask["rectangle"    ],
	Id.Ventilador			 : componentesMask["surface"  ] | componentesMask["rectangle"    ] | componentesMask["frames"],
	Id.PortaEsquerda 		 : componentesMask["surface"  ] | componentesMask["rectangle"    ] | componentesMask["frames"],
	Id.PainelDeBotoesEsquerdo: componentesMask["surface"  ] | componentesMask["rectangle"    ],
	Id.BotaoDaPortaEsquerda  : componentesMask["rectangle"] | componentesMask["botaoDaPorta"],
	Id.BotaoDaLuzEsquerda	 : componentesMask["rectangle"] | componentesMask["botaoDaLuz"],
	Id.PortaDireita		     : componentesMask["surface"  ] | componentesMask["rectangle"    ] | componentesMask["frames"],
	Id.PainelDeBotoesDireito : componentesMask["surface"  ] | componentesMask["rectangle"    ],
	Id.BotaoDaPortaDireita	 : componentesMask["rectangle"] | componentesMask["botaoDaPorta"],
	Id.BotaoDaLuzDireita	 : componentesMask["rectangle"] | componentesMask["botaoDaLuz"]
}