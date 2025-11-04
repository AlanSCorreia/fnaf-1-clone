import sys

import pygame
import configuracoes

import assets
import entidades
import componentes
import sistemas


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
			if pygame.mouse.get_pressed()[0] and sistemas.podeClickar:
				# print(pygame.mouse.get_pos())

				if sistemas.atualizarEstadoDosBotoes((entidades.Id.BotaoDaPortaEsquerda,
										  			  entidades.Id.BotaoDaPortaDireita,
													  entidades.Id.BotaoDaLuzEsquerda,
													  entidades.Id.BotaoDaLuzDireita),
													  componentes.rectangles,
													  componentes.botoesDasPortas,
													  componentes.botoesDasLuzes,
													  entidades.entidadesMask,
													  entidades.componentesMask,
													  "O botão da porta foi apertado!"):
					sistemas.atualizarSurfaceDoPainelDeBotoes(((entidades.Id.PainelDeBotoesEsquerdo,
											   				  entidades.Id.BotaoDaPortaEsquerda,
															  entidades.Id.BotaoDaLuzEsquerda),
															 (entidades.Id.PainelDeBotoesDireito,
				 											  entidades.Id.BotaoDaPortaDireita,
															  entidades.Id.BotaoDaLuzDireita)),
															 componentes.surfaces,
															 componentes.botoesDasPortas,
															 componentes.botoesDasLuzes,
															 assets.assets)
					sistemas.atualizarSurfaceDoEscritorio(entidades.Id.Escritorio,
										   				  (entidades.Id.BotaoDaLuzEsquerda,
														   entidades.Id.BotaoDaLuzDireita),
														  componentes.botoesDasLuzes,
														  componentes.surfaces,
														  assets.assets)
					sistemas.atualizarEstadoDasPortas((entidades.Id.PortaEsquerda,
													   entidades.Id.PortaDireita),
													  (entidades.Id.BotaoDaPortaEsquerda,
													   entidades.Id.BotaoDaPortaDireita),
													   componentes.portas,
													   componentes.botoesDasPortas)

				sistemas.impossibilitarClick()
		
	delta_time = configuracoes.clock.tick(60)/1000

	sistemas.atualizarDisponibilidadeDosBotoes((entidades.Id.BotaoDaPortaEsquerda,
											 	entidades.Id.BotaoDaLuzEsquerda,
											 	entidades.Id.BotaoDaPortaDireita,
												entidades.Id.BotaoDaLuzDireita),
												componentes.botoesDasPortas,
												componentes.botoesDasLuzes,
												entidades.entidadesMask,
												entidades.componentesMask)

	sistemas.atualizarFramesDoVentilador(entidades.Id.Ventilador,
									    componentes.frames,
										componentes.surfaces,
										assets.assets)
	sistemas.atualizarFramesDasPortas((entidades.Id.PortaEsquerda,
									   entidades.Id.PortaDireita),
									   componentes.surfaces,
									   componentes.portas,
									   componentes.frames,
									   assets.assets)
	
	sistemas.atualizarPosicoes(entidades.Id,
							   componentes.rectangles)
	sistemas.desenharSurfaces(configuracoes.displaySurface,
						      configuracoes.surfacesAndRectanglesIds,
							  componentes.surfaces,
							  componentes.rectangles)
	sistemas.debug(configuracoes.fonte,
				   configuracoes.displaySurface,
				   entidades.Id,
				   componentes.rectangles,
				   componentes.botoesDasPortas,
				   componentes.botoesDasLuzes,
				   componentes.portas)
	
	sistemas.atualizarIntervaloDeClick()

	pygame.display.update()
