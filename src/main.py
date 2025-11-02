import sys

import pygame
from configuracoes import displaySurface, clock, surfacesAndRectanglesIds

import assets
import entidades
import componentes
from sistemas import podeClickar, atualizarEstadoDosBotoes, atualizarEstadoDasPortas,\
					 atualizarFrameDoVentilador, atualizarFramesDasPortas,\
					 desenharSurfaces, atualizarImageDoPainelDeBotoes,\
					 atualizarPosicoes, atualizarIntervaloDeClick, impossibilitarClick

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0] and podeClickar:
				print(pygame.mouse.get_pos())

				if atualizarEstadoDosBotoes((entidades.Id.BotaoDaPortaEsquerda,
								 			 entidades.Id.BotaoDaPortaDireita),
											 componentes.rectangles,
											 componentes.botoesDaPorta,
											 "O botão da porta foi apertado!")\
				or atualizarEstadoDosBotoes((entidades.Id.BotaoDaLuzEsquerda,
								 			 entidades.Id.BotaoDaLuzDireita),
											 componentes.rectangles,
											 componentes.botoesDaLuz,
											 "O botão da luz foi apertado!"):
					atualizarImageDoPainelDeBotoes(
						((entidades.Id.PainelDeBotoesEsquerdo, entidades.Id.BotaoDaPortaEsquerda, entidades.Id.BotaoDaLuzEsquerda),
						(entidades.Id.PainelDeBotoesDireito, entidades.Id.BotaoDaPortaDireita, entidades.Id.BotaoDaLuzDireita)),
						componentes.surfaces,
						componentes.botoesDaPorta,
						componentes.botoesDaLuz,
						assets.assets)
					atualizarEstadoDasPortas((entidades.Id.PortaEsquerda,
											  entidades.Id.PortaDireita),
											 (entidades.Id.BotaoDaPortaEsquerda,
											  entidades.Id.BotaoDaPortaDireita),
											  componentes.portas,
											  componentes.botoesDaPorta)

				impossibilitarClick()
		
	delta_time = clock.tick(60)/1000

	
	atualizarFrameDoVentilador(entidades.Id.Ventilador,
							   componentes.frames,
							   componentes.surfaces,
							   assets.assets)
	atualizarFramesDasPortas((entidades.Id.PortaEsquerda,
							  entidades.Id.PortaDireita),
							  componentes.surfaces,
							  componentes.portas,
							  componentes.frames,
							  assets.assets)

	atualizarPosicoes(entidades.Id,
				   	  componentes.rectangles)
	desenharSurfaces(displaySurface,
					 surfacesAndRectanglesIds,
					 componentes.surfaces,
					 componentes.rectangles)
	atualizarIntervaloDeClick()

	pygame.display.update()
