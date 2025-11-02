from enum import Enum, auto


class Id(Enum):
	Escritorio 			   = auto()
	Ventilador 			   = auto()
	PortaEsquerda 		   = auto()
	PainelDeBotoesEsquerdo = auto()
	BotaoDaPortaEsquerda   = auto()
	BotaoDaLuzEsquerda 	   = auto()
	PortaDireita 		   = auto()
	PainelDeBotoesDireito  = auto()
	BotaoDaPortaDireita    = auto()
	BotaoDaLuzDireita 	   = auto()


componentesMask = {
	"surface"  	    : 1 << 0,
	"rectangle"     : 1 << 1,
	"botoesDaPorta" : 1 << 2,
	"botoesDaLuz"   : 1 << 3,
	"frames"        : 1 << 4
}


entidadesMask = {
	Id.Escritorio			 : componentesMask["surface"  ] | componentesMask["rectangle"    ],
	Id.Ventilador			 : componentesMask["surface"  ] | componentesMask["rectangle"    ] | componentesMask["frames"],
	Id.PortaEsquerda 		 : componentesMask["surface"  ] | componentesMask["rectangle"    ] | componentesMask["frames"],
	Id.PainelDeBotoesEsquerdo: componentesMask["surface"  ] | componentesMask["rectangle"    ],
	Id.BotaoDaPortaEsquerda  : componentesMask["rectangle"] | componentesMask["botoesDaPorta"],
	Id.BotaoDaLuzEsquerda	 : componentesMask["rectangle"] | componentesMask["botoesDaPorta"],
	Id.PortaDireita		     : componentesMask["surface"  ] | componentesMask["rectangle"    ] | componentesMask["frames"],
	Id.PainelDeBotoesDireito : componentesMask["surface"  ] | componentesMask["rectangle"    ],
	Id.BotaoDaPortaDireita	 : componentesMask["rectangle"] | componentesMask["botoesDaPorta"],
	Id.BotaoDaLuzDireita	 : componentesMask["rectangle"] | componentesMask["botoesDaPorta"]
}