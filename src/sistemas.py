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


def atualizarImageDoPainelDeBotoes(mapsId,
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
							 botoes,
							 mensagem_debug: str) -> bool:

	teveColisao = False

	for entidadeId in entidadesId:
		if rectangles[entidadeId].collidepoint(pygame.mouse.get_pos()):
			botoes[entidadeId].estado = not botoes[entidadeId].estado
			teveColisao = True
			print(mensagem_debug)

	return teveColisao


def atualizarEstadoDasPortas(portasId,
							 botoesId,
							 portas,
							 botoes) -> None:
	
	# TODO: Validar a disponibilidade do botão antes de aperta-ló
	# e atualiza-lá após aperta-ló

	for portaId, botaoId in zip(portasId, botoesId):
		if portas[portaId].aberta:
			if botoes[botaoId].estado: #and botoes[botaoId].estaDisponivel:
				portas[portaId].aberta 	 = False
				portas[portaId].fechando = True
				# botoes[botaoId].estaDisponivel = False
				print(f"Fechando porta -> {portaId}")
		elif portas[portaId].fechada:
			if not botoes[botaoId].estado:
				portas[portaId].fechada = False
				portas[portaId].abrindo = True
				print(f"Abrindo porta -> {portaId}")
		
		print(f"Estado da porta {portaId}:\nFechada: {portas[portaId].fechada}\nFechando: {portas[portaId].fechando}\nAberta: {portas[portaId].aberta}\nAbrindo: {portas[portaId].abrindo}")

def atualizarFramesDasPortas(entidadesId,
							 surfaces,
							 portas,
							 frames,
							 assets) -> None:
	
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


def atualizarFrameDoVentilador(entidadeId,
							   frames,
							   surfaces,
							   assets) -> None:


	# TOOD: Fazer uma função atualizarFrame() para:
	# 	incrementar,
	# 	decrementar,
	# 	manter uma animação em loop
	if pygame.time.get_ticks() - frames[entidadeId].tempoDoUltimoFrame > frames[entidadeId].intervaloEntreFrames:	
		frames[entidadeId].frameAtual = (frames[entidadeId].frameAtual + 1) if frames[entidadeId].frameAtual < len(assets[entidadeId])-1\
										 else 0
		frames[entidadeId].tempoDoUltimoFrame = pygame.time.get_ticks()
		surfaces[entidadeId] = assets[entidadeId][frames[entidadeId].frameAtual]


def possuiComponente(entidadeMask,
					 componente):
    return (entidadeMask & componente) != 0


def filtrarEntidadesPorComponentes(entidadesId: list,
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


def debug(entidadesId,
		  entidadesMask,
		  botoesDasPortas,
		  botoesDasLuzes,) -> None:
	pass
