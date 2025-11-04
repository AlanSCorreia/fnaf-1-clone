import pygame

import entidades
import assets


class Botao:
	def __init__(self,
			  	 intervaloDeDisponibilidade: int) -> None:

		self.estado = False
		self.estaDisponivel = True
		self.ultimoTempoDisponivel = 0
		self.intervaloDeDisponibilidade = intervaloDeDisponibilidade


class Porta:
	def __init__(self) -> None:
		
		self.fechada  = False
		self.fechando = False
		self.aberta   = True
		self.abrindo  = False


class Frames:
	def __init__(self,
				 frameAtual		 	 : int,
				 tempoDoUltimoFrame	 : float,
				 intervaloEntreFrames: float) -> None:

		self.frameAtual 		  = frameAtual
		self.tempoDoUltimoFrame   = tempoDoUltimoFrame
		self.intervaloEntreFrames = intervaloEntreFrames


class Animatronico:
	def __init__(self,
				 nivelDeDificuldade: int,
				 intervaloEntreOportunidadeDeMovimento: float,
				 rota: dict[int, str | list[str]]) -> None:

		self.nivelDeDificuldade = nivelDeDificuldade
		self.intervaloEntreOportunidadeDeMovimento = intervaloEntreOportunidadeDeMovimento
		self.rota = rota


surfaces = {
	entidades.Id.Escritorio			   : assets.assets[entidades.Id.Escritorio			  ]["vazio"][0],
	entidades.Id.Ventilador			   : assets.assets[entidades.Id.Ventilador			  ][0],
	entidades.Id.PortaEsquerda		   : assets.assets[entidades.Id.PortaEsquerda		  ][0],
	entidades.Id.PainelDeBotoesEsquerdo: assets.assets[entidades.Id.PainelDeBotoesEsquerdo][0],
	entidades.Id.PortaDireita		   : assets.assets[entidades.Id.PortaDireita		  ][0],
	entidades.Id.PainelDeBotoesDireito : assets.assets[entidades.Id.PainelDeBotoesDireito ][0],
}

rectangles = {
	entidades.Id.Escritorio			   : assets.assets[entidades.Id.Escritorio			  ]["vazio"][0].get_rect(topleft=(0, 0)),
	entidades.Id.Ventilador			   : assets.assets[entidades.Id.Ventilador			  ][0].get_rect(topleft=(783, 303)),
	entidades.Id.PortaEsquerda		   : assets.assets[entidades.Id.PortaEsquerda		  ][0].get_rect(topleft=(70, 20)),
	entidades.Id.PainelDeBotoesEsquerdo: assets.assets[entidades.Id.PainelDeBotoesEsquerdo][0].get_rect(topleft=(15, 315)),
	entidades.Id.BotaoDaPortaEsquerda  : pygame.Rect((45, 369), (40, 55)),
	entidades.Id.BotaoDaLuzEsquerda	   : pygame.Rect((45, 447), (40, 55)),
	entidades.Id.PortaDireita		   : assets.assets[entidades.Id.PortaDireita		  ][0].get_rect(topleft=(1270, 20)),
	entidades.Id.PainelDeBotoesDireito : assets.assets[entidades.Id.PainelDeBotoesDireito ][0].get_rect(topleft=(1465, 315)),
	entidades.Id.BotaoDaPortaDireita   : pygame.Rect((1488, 369), (40, 55)),
	entidades.Id.BotaoDaLuzDireita	   : pygame.Rect((1488, 447), (40, 55)),
}

botoesDasPortas = {
	entidades.Id.BotaoDaPortaEsquerda: Botao(500),
	entidades.Id.BotaoDaPortaDireita : Botao(500)
}

botoesDasLuzes = {
	entidades.Id.BotaoDaLuzEsquerda: Botao(250),
	entidades.Id.BotaoDaLuzDireita : Botao(250)
}

# botoesDaCamera = {

# }

portas = {
	entidades.Id.PortaEsquerda: Porta(),
	entidades.Id.PortaDireita : Porta()
}

frames = {
	entidades.Id.Ventilador   : Frames(0, 0, 25),
	entidades.Id.PortaEsquerda: Frames(0, 0, 25),
	entidades.Id.PortaDireita : Frames(0, 0, 25)
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