from random import randint

import pygame


podeClickar = True
ultimoClick = 0
intervaloEntreClicks = 100


def impossibilitarClick():
	global ultimoClick, podeClickar

	ultimoClick = pygame.time.get_ticks()
	podeClickar = False


def atualizarIntervaloDeClick():
	global podeClickar

	if not podeClickar:
		tempoAtual = pygame.time.get_ticks()
		if tempoAtual-ultimoClick > intervaloEntreClicks:
			podeClickar = True


def desenharSurfaces(displaySurface,
					 entidadesId,
					 surfaces: dict,
					 rectangles: dict) -> None:
	
	for entidadeId in entidadesId:
		displaySurface.blit(surfaces[entidadeId], rectangles[entidadeId])


def atualizarPosicoes(entidadesId,
					  rectangles: dict) -> None:
	""" 
	Aqui foi necessário mover os Rects dos botoes direitos pois eles estavam sendo 
	renderizados fora da resolução da tela.
	resolução.x da tela 1280 vesus a coordenada.x dos rects 1515
		isso ocorre porque a resolução.x da surface escritorio é de 1600
		logo não dava pra clickar pois sempre estava fora do alcance
	a solução foi mover para a esquerda os Rects sempre que a tela estiver se mexendo
	para a direita até que estejam dentro da resolução.
	quando a tela vai para a esquerda os Rects são empurrados de volta para a direita,
	fora da resolução
	"""

	atualizarPosicao = 10
	if pygame.mouse.get_pos()[0] > 1100 and rectangles[entidadesId.Escritorio].x >= -320:
		for entidadeId in entidadesId:
			rectangles[entidadeId].x -= atualizarPosicao

	elif pygame.mouse.get_pos()[0] < 200 and rectangles[entidadesId.Escritorio].x <= 10:
		for entidadeId in entidadesId:
			rectangles[entidadeId].x += atualizarPosicao


def atualizarSurfaceDoPainelDeBotoes(mapsId,
								   surfaces,
								   botoesDaPorta,
								   botoesDaLuz,
								   assets) -> None:

	for mapId in mapsId:
		painelId 	   = mapId[0]
		botaoDaPortaId = mapId[1]
		botaoDaLuzId   = mapId[2]

		if botoesDaPorta[botaoDaPortaId].estado:
			if botoesDaLuz[botaoDaLuzId].estado:
				surfaces[painelId] = assets[painelId][3]
			else:
				surfaces[painelId] = assets[painelId][1]
		elif botoesDaLuz[botaoDaLuzId].estado:
			surfaces[painelId] = assets[painelId][2]
		else:
			surfaces[painelId] = assets[painelId][0]

	
def oportunidadeDeMovimento(animatronico) -> bool:
	return randint(0, 20) <= animatronico.nivelDeDificuldade


def atualizarEstadoDosBotoes(entidadesId,
							 rectangles,
							 botoesDasPortas,
							 botoesDasLuzes,
							 entidadesMask,
							 componentesMask,
							 mensagem_debug: str) -> bool:
	
	# Ideia de otimização: Fazer checagens com base na posição do mouse
	# por exemplo, não tem porque considerar os botões das luzes se a posição Y
	# estiver abaixo da posição em que esses botões se encontram (não esqueça, quanto
	# mais baixo na tela, maior o valor de Y)
	teveColisao = False

	for entidadeId in entidadesId:
		botao = botoesDasPortas if possuiComponente(entidadesMask[entidadeId], componentesMask["botaoDaPorta"])\
								else botoesDasLuzes
		
		if rectangles[entidadeId].collidepoint(pygame.mouse.get_pos()) and botao[entidadeId].estaDisponivel:
			botao[entidadeId].estado = not botao[entidadeId].estado
			teveColisao = True

			botao[entidadeId].ultimoTempoDisponivel = pygame.time.get_ticks()
			botao[entidadeId].estaDisponivel = False
			print(mensagem_debug)

	return teveColisao


def atualizarDisponibilidadeDosBotoes(botoesId,
									  botoesDasPortas,
									  botoesDasLuzes,
									  entidadesMask,
									  componentesMask):
	
	# Ideia de otimização: Fazer checagens com base na posição do mouse
	# por exemplo, não tem porque considerar os botões das luzes se a posição Y
	# estiver abaixo da posição em que esses botões se encontram (não esqueça, quanto
	# mais baixo na tela, maior o valor de Y)
	for botaoId in botoesId:
		botao = botoesDasPortas if possuiComponente(entidadesMask[botaoId], componentesMask["botaoDaPorta"])\
							  else botoesDasLuzes
		
		if not botao[botaoId].estaDisponivel:
			if pygame.time.get_ticks() - botao[botaoId].ultimoTempoDisponivel > botao[botaoId].intervaloDeDisponibilidade:
				botao[botaoId].estaDisponivel = True


def atualizarEstadoDasPortas(portasId,
							 botoesId,
							 portas,
							 botoes) -> None:
	
	# Ideia de otimização: Fazer checagens com base na posição do mouse
	# por exemplo, não tem porque considerar a porta direita se a posição x
	# estiver abaixo da posição em que esta porta se encontra

	for portaId, botaoId in zip(portasId, botoesId):
		if portas[portaId].aberta:
			if botoes[botaoId].estado:
				portas[portaId].aberta 	 = False
				portas[portaId].fechando = True

				botoes[botaoId].estaDisponivel = False
				print(f"Fechando porta -> {portaId}")
		elif portas[portaId].fechada:
			if not botoes[botaoId].estado:
				portas[portaId].fechada = False
				portas[portaId].abrindo = True

				botoes[botaoId].estaDisponivel = False
				print(f"Abrindo porta -> {portaId}")
		
		# print(f"Estado da porta {portaId}:\nFechada: {portas[portaId].fechada}\nFechando: {portas[portaId].fechando}\nAberta: {portas[portaId].aberta}\nAbrindo: {portas[portaId].abrindo}")


def atualizarSurfaceDoEscritorio(entidadeId,
								 botoesId,
								 botoesDasLuzes,
								 surfaces,
								 assets) -> None:
	
	# Usei numero mágico pra não ter que importar o displaySurface so pra pegar metade da tela 
	botaoId, vazioId = (botoesId[0], 1) if pygame.mouse.get_pos()[0] < 500\
					    else (botoesId[1], 2)
	
	if botoesDasLuzes[botaoId].estado:
		surfaces[entidadeId] = assets[entidadeId]["vazio"][vazioId]
	# Checar se a Bonnie e/ou chica estão na porta
	else:
		surfaces[entidadeId] = assets[entidadeId]["vazio"][0]


def atualizarFrames():

	# TOOD: Fazer uma função atualizarFrame() para:
	# 	incrementar,
	# 	decrementar,
	# 	manter uma animação em loop
	pass


def atualizarFramesDosJumpscares():

	pass


def atualizarFramesDasPortas(entidadesId,
							 surfaces,
							 portas,
							 frames,
							 assets) -> None:
	
	# Ideia de otimização: Criar função que faz o processo de mudar as váriaveis referentes
	# aos 4 estados das portas
	
	for entidadeId in entidadesId:
		animacaoOcorrendo = 0
		frameIndice = frames[entidadeId].frameAtual

		if portas[entidadeId].fechando:
			animacaoOcorrendo = frames[entidadeId].frameAtual < len(assets[entidadeId])-1
			frameIndice += 1
		elif portas[entidadeId].abrindo:
			animacaoOcorrendo = frames[entidadeId].frameAtual > 0
			frameIndice -= 1
		
		if portas[entidadeId].fechando or portas[entidadeId].abrindo:
			if animacaoOcorrendo:
				if pygame.time.get_ticks() - frames[entidadeId].tempoDoUltimoFrame > frames[entidadeId].intervaloEntreFrames:
					frames[entidadeId].frameAtual = frameIndice							

					frames[entidadeId].tempoDoUltimoFrame = pygame.time.get_ticks()
					surfaces[entidadeId] = assets[entidadeId][frames[entidadeId].frameAtual]
			else:
				if portas[entidadeId].fechando:
					frames[entidadeId].frameAtual = len(assets[entidadeId])-1
					portas[entidadeId].fechando   = False
					portas[entidadeId].fechada    = True
				else:
					frames[entidadeId].frameAtual = 0
					portas[entidadeId].abrindo	  = False
					portas[entidadeId].aberta	  = True


def atualizarFramesDoVentilador(entidadeId,
							    frames,
							    surfaces,
							    assets) -> None:

	if pygame.time.get_ticks() - frames[entidadeId].tempoDoUltimoFrame > frames[entidadeId].intervaloEntreFrames:	
		frames[entidadeId].frameAtual = (frames[entidadeId].frameAtual + 1) if frames[entidadeId].frameAtual < len(assets[entidadeId])-1\
										 else 0
		frames[entidadeId].tempoDoUltimoFrame = pygame.time.get_ticks()
		surfaces[entidadeId] = assets[entidadeId][frames[entidadeId].frameAtual]


def possuiComponente(entidadeMask,
					 componente):
    return (entidadeMask & componente) != 0


def filtrarEntidadesPorComponentes(entidadesId,
								   componentes: list[str],
								   entidadeMask: dict,
								   componenteMask: dict):
	
    def possuiTodosComponentes(entidade_mask, componentes, componenteMask):
        return all(possuiComponente(entidade_mask, componenteMask[componente]) for componente in componentes)

    return [entidadeId 
			for entidadeId in entidadesId
			if possuiTodosComponentes(entidadeMask[entidadeId],
							 		  componentes,
									  componenteMask)]


def debug(fonte: pygame.font.Font,
		  displaySurface,
		  entidadesId,
		  rectangles,
		#   entidadesMask,
		  botoesDasPortas,
		  botoesDasLuzes,
		  portas
		  ):

	texto = ''

	texto += f"{entidadesId.Escritorio}\n"
	texto += f"Eixo X: {rectangles[entidadesId.Escritorio].x} Eixo Y: {rectangles[entidadesId.Escritorio].y}\n"
	texto += f"\n{entidadesId.PainelDeBotoesEsquerdo}\n"
	texto += f"Eixo X : {rectangles[entidadesId.PainelDeBotoesEsquerdo].x} Eixo Y: {rectangles[entidadesId.PainelDeBotoesEsquerdo].y}\n"
	texto += f"fechada: {portas[entidadesId.PortaEsquerda].fechada} fechando: {portas[entidadesId.PortaEsquerda].fechando} aberta: {portas[entidadesId.PortaEsquerda].aberta} abrindo: {portas[entidadesId.PortaEsquerda].abrindo}\n"
	texto += f"Botão da Porta: {botoesDasPortas[entidadesId.BotaoDaPortaEsquerda].estado} esta disponível: {botoesDasPortas[entidadesId.BotaoDaPortaEsquerda].estaDisponivel}\n"
	texto += f"Botão da Luz: {botoesDasLuzes[entidadesId.BotaoDaLuzEsquerda].estado} esta disponível: {botoesDasLuzes[entidadesId.BotaoDaLuzEsquerda].estaDisponivel}\n"
	texto += f"\n{entidadesId.PainelDeBotoesDireito}\n"
	texto += f"Eixo X: {rectangles[entidadesId.PainelDeBotoesDireito].x} Eixo Y: {rectangles[entidadesId.PainelDeBotoesDireito].y}\n"
	texto += f"fechada: {portas[entidadesId.PortaDireita].fechada} fechando: {portas[entidadesId.PortaDireita].fechando} aberta: {portas[entidadesId.PortaDireita].aberta} abrindo: {portas[entidadesId.PortaDireita].abrindo}\n"
	texto += f"Botão da Porta: {botoesDasPortas[entidadesId.BotaoDaPortaDireita].estado} esta disponível: {botoesDasPortas[entidadesId.BotaoDaPortaDireita].estaDisponivel}\n"
	texto += f"Botão da Luz: {botoesDasLuzes[entidadesId.BotaoDaLuzDireita].estado} esta disponível: {botoesDasLuzes[entidadesId.BotaoDaLuzDireita].estaDisponivel}\n"

	fonteSurface = fonte.render(texto, True, pygame.color.Color("white"))
	fonteRect = fonteSurface.get_rect(topleft=(0, 0))

	displaySurface.blit(fonteSurface, fonteRect)
