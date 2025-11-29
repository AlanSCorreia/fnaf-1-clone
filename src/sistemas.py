from random import randint

import pygame


def desenharSurfaces(displaySurface,
					 entidadesId,
					 surfaces: dict,
					 rectangles: dict) -> None:
	
	for entidadeId in entidadesId:
		displaySurface.blit(surfaces[entidadeId], rectangles[entidadeId])


def atualizarMomentoEmJogo(cameraId,
						   momentoEmJogo,
						   momentosEmJogo,
						   estados):
	
	if not estados[cameraId].estado:
		momentoEmJogo["atual"] = momentosEmJogo.SEM_CAMERA
	else:
		if estados[cameraId].estaDisponivel:
			momentoEmJogo["atual"] = momentosEmJogo.COM_CAMERA


def ativarCamera(cameraId,
				#  momentoEmJogo,
				 event,
				 rectangle,
				 estados,
				 quadros):

	if rectangle.collidepoint(event.pos):
		if estados[cameraId].estaDisponivel:
			atualizarEstado(cameraId,
				   			estados)
			quadros[cameraId].animacaoEstaOcorrendo = True
			quadros[cameraId].estaRevertendo = not estados[cameraId].estado


def atualizarPosicaoDinamica(atualizarPosicao: int,
							 limitesDeslocamentoCamera: dict[str, int],
							 deslocamentoSemCamera: dict[str, int]) -> None:
	""" 
	Aqui foi necessário mover os Rects dos botoes direitos pois eles estavam sendo 
	renderizados fora da resolução da tela.
	resolução.x da tela 1280 vesus a coordenada.x dos rects 1515
		isso ocorre porque a resolução.x da surface OFFICE é de 1600
		logo não dava pra clickar pois sempre estava fora do alcance
	a solução foi mover para a esquerda os Rects sempre que a tela estiver se mexendo
	para a direita até que estejam no limite da resolução.
	quando a tela vai para a esquerda os Rects são empurrados de volta para a direita,
	fora da resolução
	"""

	if pygame.mouse.get_pos()[0] > 1100\
	and deslocamentoSemCamera["base"] >= limitesDeslocamentoCamera["minimo"]:
		deslocamentoSemCamera["vertical"] = -(atualizarPosicao)

	elif pygame.mouse.get_pos()[0] < 200\
	and deslocamentoSemCamera["base"] <= limitesDeslocamentoCamera["maximo"]:
		deslocamentoSemCamera["vertical"] = atualizarPosicao

	else:
		deslocamentoSemCamera["vertical"] = 0

	deslocamentoSemCamera["base"] += deslocamentoSemCamera["vertical"]


def atualizarDirecaoCamera(cameraMovimentoId,
						   estados,
						   deslocamentoComCamera: dict[str, int | bool],
						   limitesDeslocamentoCamera: dict[str, int]):

		if estados[cameraMovimentoId].estado:
			if deslocamentoComCamera["base"] in range(limitesDeslocamentoCamera["minimo"]-3,
													  limitesDeslocamentoCamera["minimo"]+3):
				atualizarEstado(cameraMovimentoId,
								estados,
								False)

		else:
			if deslocamentoComCamera["base"] in range(limitesDeslocamentoCamera["maximo"]-3,
													  limitesDeslocamentoCamera["maximo"]+3):
				atualizarEstado(cameraMovimentoId,
								estados,
								True)


def atualizarPosicaoBackgroundCamera(cameraMovimentoId,
									 estados,
									 atualizarPosicao: int,
									 deslocamentoComCamera: dict[str, int | bool]):

	if estados[cameraMovimentoId].estado:
		if estados[cameraMovimentoId].estaDisponivel:
			deslocamentoComCamera["vertical"] = -(atualizarPosicao)

	else:
		if estados[cameraMovimentoId].estaDisponivel:
			deslocamentoComCamera["vertical"] = atualizarPosicao

	deslocamentoComCamera["base"] += deslocamentoComCamera["vertical"]
	
	# print(deslocamentoComCamera["movimentoDisponivel"])


def atualizarBackgroundCamera(salaId,
							  cameraBackground):
	
	cameraBackground["atual"] = salaId
	print(salaId)


def atualizarSurfaceDoPainelDeBotoes(mapId,
									 surfaces,
									 estados,
									 assets) -> None:

	painelId 	   = mapId[0]
	botaoDaPortaId = mapId[1]
	botaoDaLuzId   = mapId[2]

	if estados[botaoDaPortaId].estado:
		if estados[botaoDaLuzId].estado:
			surfaces[painelId] = assets[painelId][3]
		else:
			surfaces[painelId] = assets[painelId][1]
	elif estados[botaoDaLuzId].estado:
		surfaces[painelId] = assets[painelId][2]
	else:
		surfaces[painelId] = assets[painelId][0]


def atualizarEstadoDoBotao(botaoId,
						   rectangles,
						   estados) -> bool:
	
	teveColisao = False
		
	if rectangles[botaoId].collidepoint(pygame.mouse.get_pos())\
	and estados[botaoId].estaDisponivel:
		atualizarEstado(botaoId,
				  		estados)
		teveColisao = True

	return teveColisao


def disponibilizarEstado(estadoId,
						 estados):
	
	# Ideia de otimização: Fazer checagens com base na posição do mouse
	# por exemplo, não tem porque considerar os botões das luzes se a posição Y
	# estiver abaixo da posição em que esses botões se encontram (não esqueça, quanto
	# mais baixo na tela, maior o valor de Y)
	if not estados[estadoId].estaDisponivel:
		if pygame.time.get_ticks() - estados[estadoId].ultimoTempoDisponivel > estados[estadoId].intervaloDeDisponibilidade:
			estados[estadoId].estaDisponivel = True


def atualizarEstadoDaPorta(portaId,
						   botaoId,
						   estados,
						   quadros) -> None:
	
	# Ideia anterior
		# Ideia de otimização: Fazer checagens com base na posição do mouse
		# por exemplo, não tem porque considerar a porta direita se a posição x
		# estiver abaixo da posição em que esta porta se encontra
	# Ideia nova
		# A ideia anterior é boa, mas esta função não precisa saber da posição da tela
		# Ao inves, ela deveria se preocupar com uma porta por vez
		# com as informações do evento que ativa esta função
		# os parametros irão receber os dados necessários

		# Como as portas não estão sendo disponibilizadas, sempre da True
		# por isso ela abre/fecha mesmo quando aperta o botão da luz
	
	if estados[portaId].estado ^ estados[botaoId].estado:
		atualizarEstado(portaId,
						estados)
		quadros[portaId].animacaoEstaOcorrendo = True
		quadros[portaId].estaRevertendo = not estados[portaId].estado


def atualizarEstado(entidadeId,
					componente,
					estado=None) -> None:

	if estado is None:
		componente[entidadeId].estado = not componente[entidadeId].estado
	else:
		componente[entidadeId].estado = estado

	componente[entidadeId].ultimoTempoDisponivel = pygame.time.get_ticks()
	componente[entidadeId].estaDisponivel = False


def atualizarSurfaceDoEscritorio(escritorioId,
								 botaoId,
								 vazioId,
								 estados,
								 surfaces,
								 assets) -> None:

	# botaoId e vazioId deveriam vir atraves de parametros
	# botaoId, vazioId = (botoesId[0], 1) if pygame.mouse.get_pos()[0] < configuracoes.janelaLargura/2\
	# 			  else (botoesId[1], 2)

	if estados[botaoId].estado:
		surfaces[escritorioId] = assets[escritorioId]["vazio"][vazioId]
	# Checar se a Bonnie e/ou chica estão na porta
	else:
		surfaces[escritorioId] = assets[escritorioId]["vazio"][0]


def checarIntervaloEntreQuadros(entidadeId,
								quadros,
								tempoAtual):
	return tempoAtual-quadros[entidadeId].tempoDoUltimoQuadro\
		> quadros[entidadeId].intervaloEntreQuadros


def atualizarQuadro(entidadeId,
					surfaces,
					quadros,
					assets,
					tempoAtual):

	quadros[entidadeId].tempoDoUltimoQuadro = tempoAtual
	surfaces[entidadeId] = assets[entidadeId][quadros[entidadeId].quadroAtual]


def atualizarEstadoDaAnimacao(entidadeId,
							  quadros,
							  assets):
	
	if quadros[entidadeId].estaRepetindo:
		return
	
	quadroIndice = quadros[entidadeId].quadroAtual
	aindaEstaOcorrendo = quadroIndice > 0 if quadros[entidadeId].estaRevertendo\
					else quadroIndice < len(assets[entidadeId])-1
	
	quadros[entidadeId].animacaoEstaOcorrendo = aindaEstaOcorrendo


def acrescentarQuadro(entidadeId,
					  quadros,
					  assets):
	
	if quadros[entidadeId].quadroAtual < len(assets[entidadeId])-1:
		quadros[entidadeId].quadroAtual += 1
	else:
		if quadros[entidadeId].estaRepetindo\
		or quadros[entidadeId].precisaReiniciar:
			quadros[entidadeId].quadroAtual = 0


def decrementarQuadro(entidadeId,
					  quadros,
					  assets):
	
	if quadros[entidadeId].quadroAtual > 0:
		quadros[entidadeId].quadroAtual -= 1
	else:
		if quadros[entidadeId].estaEmLoop\
		or quadros[entidadeId].precisaReiniciar:
			quadros[entidadeId].quadroAtual = len(assets[entidadeId])-1


def possuiComponente(entidadeMask,
					 componente):
    return (entidadeMask & componente) != 0


def possuiTodosComponentes(entidadesMask, bitMasks):
        return all(possuiComponente(entidadesMask, bitMask)
				   for bitMask in bitMasks)


def possuiQualquerComponentes(entidadesMask, bitMasks):
        return any(possuiComponente(entidadesMask, bitMask)
				   for bitMask in bitMasks)


def filtrarEntidadesPorComponentes(entidadesId,
								   bitMasksAceitos,#: list[str],
								   bitMasksRejeitados,# : list[str] | None,
								   entidadesMask):# : dict
	
	resultado = []

	for entidadeId in entidadesId:
		if bitMasksAceitos:
			if bitMasksRejeitados:
				if possuiTodosComponentes(entidadesMask[entidadeId], bitMasksAceitos)\
				and not possuiQualquerComponentes(entidadesMask[entidadeId], bitMasksRejeitados):
					resultado.append(entidadeId)
			else:
				if possuiTodosComponentes(entidadesMask[entidadeId], bitMasksAceitos):
					resultado.append(entidadeId)
	
	return resultado


def debug(fonte: pygame.font.Font,
		  displaySurface,
		  entidadesId,
		  rectangles,
		  quadros,
		  estados):

	texto = ''

	texto += f"{entidadesId.OFFICE}\n"
	texto += f"Eixo X: {rectangles["backgrounds"][entidadesId.OFFICE].x} Eixo Y: {rectangles["backgrounds"][entidadesId.OFFICE].y}\n"

	texto += f"ativado: {estados[entidadesId.PORTA_ESQUERDA].estado} esta disponível: {estados[entidadesId.PORTA_ESQUERDA].estaDisponivel}\n"
	
	texto += f"\n{entidadesId.PAINEL_BOTOES_ESQUERDOS}\n"
	texto += f"Eixo X : {rectangles["inanimados"][entidadesId.PAINEL_BOTOES_ESQUERDOS].x} Eixo Y: {rectangles["inanimados"][entidadesId.PAINEL_BOTOES_ESQUERDOS].y}\n"
	texto += f"Botão da Porta: {estados[entidadesId.BOTAO_PORTA_ESQUERDA].estado} esta disponível: {estados[entidadesId.BOTAO_PORTA_ESQUERDA].estaDisponivel}\n"
	texto += f"Botão da Luz: {estados[entidadesId.BOTAO_LUZ_ESQUERDA].estado} esta disponível: {estados[entidadesId.BOTAO_LUZ_ESQUERDA].estaDisponivel}\n"
	
	texto += f"ativado: {estados[entidadesId.PORTA_DIREITA].estado} esta disponível: {estados[entidadesId.PORTA_DIREITA].estaDisponivel}\n"
	
	texto += f"\n{entidadesId.PAINEL_BOTOES_DIREITOS}\n"
	texto += f"Eixo X: {rectangles["inanimados"][entidadesId.PAINEL_BOTOES_DIREITOS].x} Eixo Y: {rectangles["inanimados"][entidadesId.PAINEL_BOTOES_DIREITOS].y}\n"
	texto += f"Botão da Porta: {estados[entidadesId.BOTAO_PORTA_DIREITA].estado} esta disponível: {estados[entidadesId.BOTAO_PORTA_DIREITA].estaDisponivel}\n"
	texto += f"Botão da Luz: {estados[entidadesId.BOTAO_LUZ_DIREITA].estado} esta disponível: {estados[entidadesId.BOTAO_LUZ_DIREITA].estaDisponivel}\n"

	texto += "\nCamera\n"
	texto += f"esta Disponivel: {estados[entidadesId.CAMERA].estaDisponivel}"
	texto += f"\nAnimação está ocorrendo: {quadros[entidadesId.CAMERA].animacaoEstaOcorrendo}"
	texto += f"\nQuadro atual: {quadros[entidadesId.CAMERA].quadroAtual}"

	texto += "\nAnimação de transição/ativação da camera"
	texto += f"\nAnimação está ocorrendo: {quadros[entidadesId.CAMERA_TRANSICAO].animacaoEstaOcorrendo}"
	texto += f"\nQuadro atual: {quadros[entidadesId.CAMERA_TRANSICAO].quadroAtual}"

	fonteSurface = fonte.render(texto, True, pygame.color.Color("white"))
	fonteRect = fonteSurface.get_rect(topleft=(0, 0))

	displaySurface.blit(fonteSurface, fonteRect)


def oportunidadeDeMovimento(animatronico) -> bool:
	return randint(0, 20) <= animatronico.nivelDeDificuldade
