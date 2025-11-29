# Todo:
#	3 - existem momento diferentes onde diferentes botões serão necessários ao decorrer do game.
# 		O menu inicial tem seus botões,
# 		o menu de custom night tem seus botões,
#		durante o gameplay no escritório
# 		e quando a câmera está sendo utilizada,
# 		cada situação tem suas entidades, componentes e sistemas. Preciso pensar como organizar tudo isto
# Propostas:

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
				
		if event.type == pygame.MOUSEMOTION:
			sistemas.ativarCamera(entidades.Entidades.CAMERA,
						 		  event,
								  configuracoes.uiEstatico.botaoCameraRectangle,
								  componentes.estados,
								  componentes.quadros)
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1\
			and componentes.estados[entidades.Entidades.MOUSE].estaDisponivel:
				# print(pygame.mouse.get_pos())
				match componentes.globais["momentoEmJogo"]["atual"]:
					case componentes.MomentosEmJogo.SEM_CAMERA:
						painelDeBotoesId = None
						portaId = None
						escritorioSurfaceId = 0
						
						if event.pos[0] < configuracoes.janelaLargura/2:
							painelDeBotoesId = entidades.painelDeBotoesEsquerdo
							portaId = entidades.Entidades.PORTA_ESQUERDA
							escritorioSurfaceId = 1
						else:
							painelDeBotoesId = entidades.painelDeBotoesDireito
							portaId = entidades.Entidades.PORTA_DIREITA
							escritorioSurfaceId = 2

						# O primeiro item de cada Painel de Controle é o próprio Painel
						# Os dois seguintes são os botões do Painel
						for salaId in painelDeBotoesId[1:]:
							if sistemas.atualizarEstadoDoBotao(salaId,
															componentes.rectangles["inanimados"],
															componentes.estados):
								
								sistemas.atualizarSurfaceDoPainelDeBotoes(painelDeBotoesId,
																		componentes.surfaces["inanimados"],
																		componentes.estados,
																		assets.inanimados)
								
								sistemas.atualizarSurfaceDoEscritorio(entidades.Entidades.OFFICE,
																		painelDeBotoesId[2],
																		escritorioSurfaceId,
																		componentes.estados,
																		componentes.surfaces["backgrounds"],
																		assets.backgrounds)
								
								sistemas.atualizarEstadoDaPorta(portaId,
															painelDeBotoesId[1],
															componentes.estados,
															componentes.quadros)

					case componentes.MomentosEmJogo.COM_CAMERA:
						for salaId in entidades.botoesSalas:
							if sistemas.atualizarEstadoDoBotao(salaId,
										  					   componentes.rectangles["botoesSalas"],
															   componentes.estados):
								componentes.quadros[entidades.Entidades.CAMERA_TRANSICAO].animacaoEstaOcorrendo = True
								
								sistemas.atualizarBackgroundCamera(salaId,
										   						   componentes.globais["cameraBackground"])
								
				componentes.globais["estadoMouse"]["ultimoClick"] = pygame.time.get_ticks()
				componentes.globais["estadoMouse"]["estaDisponivel"] = False

	deltaTime = configuracoes.clock.tick(120)/1000
	tempoAtual = pygame.time.get_ticks()
	atualizarPosicaoSemCamera = int(500*deltaTime)
	atualizarPosicaoComCamera = int(150*deltaTime)
	
	sistemas.atualizarDirecaoCamera(entidades.Entidades.CAMERA_MOVIMENTO,
								 	componentes.estados,
								 	componentes.globais["deslocamentoComCamera"],
								 	componentes.globais["limitesDeslocamentoCamera"])
	
	sistemas.atualizarMomentoEmJogo(entidades.Entidades.CAMERA,
									componentes.globais["momentoEmJogo"],
									componentes.MomentosEmJogo,
									componentes.estados)

	for estadoId in entidades.estados:
		sistemas.disponibilizarEstado(estadoId,
									  componentes.estados)

	for salaId in entidades.quadros:
		if componentes.quadros[salaId].animacaoEstaOcorrendo:

			if sistemas.checarIntervaloEntreQuadros(salaId,
													componentes.quadros,
													tempoAtual):
				
				if componentes.quadros[salaId].estaRevertendo:
					sistemas.decrementarQuadro(salaId,
												componentes.quadros,
												assets.animados)
				else:
					sistemas.acrescentarQuadro(salaId,
												componentes.quadros,
												assets.animados)

				surfaces = None

				if salaId in entidades.estaticosSurfaces:
					surfaces = componentes.surfaces["estaticos"]
				else:
					surfaces = componentes.surfaces["animados"]

				sistemas.atualizarQuadro(salaId,
										 surfaces,
										 componentes.quadros,
										 assets.animados,
										 tempoAtual)
				
				sistemas.atualizarEstadoDaAnimacao(salaId,
												   componentes.quadros,
												   assets.animados)

	match componentes.globais["momentoEmJogo"]["atual"]:
		case componentes.MomentosEmJogo.SEM_CAMERA:
			sistemas.atualizarPosicaoDinamica(atualizarPosicaoSemCamera,
									 		  componentes.globais["limitesDeslocamentoCamera"],
											  componentes.globais["deslocamentoSemCamera"])
			
			deslocamentoVertical = componentes.globais["deslocamentoSemCamera"]["vertical"]

			for salaId in entidades.inanimadosRectangles:
				componentes.rectangles["inanimados"][salaId].x += deslocamentoVertical
			
			for salaId in entidades.animadosRectangles:
				componentes.rectangles["animados"][salaId].x += deslocamentoVertical
			
			componentes.rectangles["backgrounds"][entidades.Entidades.OFFICE].x += deslocamentoVertical
			
			configuracoes.displaySurface.blit(componentes.surfaces["backgrounds"][entidades.Entidades.OFFICE],
											  componentes.rectangles["backgrounds"][entidades.Entidades.OFFICE])

			for salaId in entidades.animadosSurfaces:
				configuracoes.displaySurface.blit(componentes.surfaces["animados"][salaId],
												  componentes.rectangles["animados"][salaId])

			for salaId in entidades.inanimadosSurfaces:
				configuracoes.displaySurface.blit(componentes.surfaces["inanimados"][salaId],
												componentes.rectangles["inanimados"][salaId])
		
		case componentes.MomentosEmJogo.COM_CAMERA:
			sistemas.atualizarPosicaoBackgroundCamera(entidades.Entidades.CAMERA_MOVIMENTO,
											 		  componentes.estados,
													  atualizarPosicaoComCamera,
											 		  componentes.globais["deslocamentoComCamera"])
			
			if componentes.estados[entidades.Entidades.CAMERA_MOVIMENTO].estaDisponivel:
				componentes.rectangles["backgrounds"][componentes.globais["cameraBackground"]["atual"]].x += componentes.globais["deslocamentoComCamera"]["vertical"]

			# Draw Background
			configuracoes.displaySurface.blit(componentes.surfaces["backgrounds"][componentes.globais["cameraBackground"]["atual"]],
											  componentes.rectangles["backgrounds"][componentes.globais["cameraBackground"]["atual"]])
			
			for salaId in entidades.camera:
				configuracoes.displaySurface.blit(componentes.surfaces["botoesSalas"][salaId],
									  			  componentes.rectangles["botoesSalas"][salaId])
			
			configuracoes.uiEstaticoComCamera.desenhar()

	for salaId in entidades.estaticosSurfaces:
		if sistemas.possuiComponente(entidades.entidadesMasks[salaId],
							   		 entidades.Bitmasks.QUADRO_APENAS):
			if componentes.quadros[salaId].animacaoEstaOcorrendo:
				configuracoes.displaySurface.blit(componentes.surfaces["estaticos"][salaId],
												  componentes.rectangles["estaticos"][salaId])
	
	configuracoes.uiEstatico.usage = 0 # Nivel de consumo de energia
	configuracoes.uiEstatico.desenhar()

	sistemas.debug(configuracoes.fonte,
					configuracoes.displaySurface,
					entidades.Entidades,
					componentes.rectangles,
					componentes.quadros,
					componentes.estados)

	pygame.display.update()
	# print(componentes.momentoEmJogo)
