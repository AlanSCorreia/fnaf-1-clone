from configuracoes import pygame

from sprite_imports import image, botoes_esquerdos_pressionados, botoes_direitos_pressionados


class PainelDeBotoes():
	def __init__(self,
			  	 escritorio_surface,
			  	 posicao: tuple[int, int],
				 inverter: bool = False):

		self.image_dict = botoes_direitos_pressionados if inverter\
						  else botoes_esquerdos_pressionados
		
		self.image = pygame.image.load(self.image_dict["nenhum"]).convert_alpha()
		self.posicao = posicao
		self.escritorio_surface = escritorio_surface

		left =  23 if inverter else 47
		self.botoes = {"porta": [pygame.Rect((self.posicao[0]+left, self.posicao[1]+54), (40, 55)), False], #  Rectangle e estado(Ligado, Desligado)
					   "luz"  : [pygame.Rect((self.posicao[0]+left, self.posicao[1]+132), (40, 55)), False]}

		self.pode_clickar = True
		self.ultimo_click = 0
		self.intervalo_click = 100
	
	def atualizar_intervalo(self):
		if not self.pode_clickar:
			tempo_atual = pygame.time.get_ticks()
			if tempo_atual-self.ultimo_click > self.intervalo_click:
				self.pode_clickar = True
	
	def atualizar_image(self):

		estado = ""
		
		if   self.botoes["porta"] [1]\
		and  self.botoes["luz"  ] [1]: estado = "ambos"
		elif self.botoes["porta"] [1]: estado = "porta"
		elif self.botoes["luz"  ] [1]: estado = "luz"
		else						 : estado = "nenhum"

		self.image = pygame.image.load(self.image_dict[estado]).convert_alpha()
	
	def acionar_botao(self):

		if pygame.mouse.get_pressed()[0] and self.pode_clickar:
			posicao_click = pygame.mouse.get_pos()
			if self.botoes["porta"][0].collidepoint(posicao_click):
				self.botoes["porta"][1] = not self.botoes["porta"][1]
				print("Apertou o botão da porta")
			
			elif self.botoes["luz"][0].collidepoint(posicao_click):
				self.botoes["luz"][1] = not self.botoes["luz"][1]
				print("Apertou o botão da luz")

			self.pode_clickar = False
			self.ultimo_click = pygame.time.get_ticks()
				
			self.atualizar_image()
	
	def atualizar(self):
		self.escritorio_surface.blit(self.image, self.posicao)

		self.acionar_botao()
		self.atualizar_intervalo()


class Ventilador:
	def __init__(self,
			  	 escritorio_surface,
				 posicao) -> None:
		self.image = pygame.image.load(image["ventilador"]).convert_alpha()
		self.rect  = self.image.get_rect(topleft=posicao)

		self.escritorio_surface = escritorio_surface
	
	def desenhar(self):
		self.escritorio_surface.blit(self.image, self.rect)


class Escritorio(pygame.sprite.Sprite):
	def __init__(self,
			  	 groups) -> None:
		
		super().__init__(groups)
		self.image = pygame.image.load(image["escritorio"]).convert_alpha()
		self.rect = self.image.get_rect(topleft=(0, 0))

		self.painel_esquerdo = PainelDeBotoes(self.image, (15, 315))
		self.painel_direito  = PainelDeBotoes(self.image, (1465, 315), inverter=True)

		self.ventilador = Ventilador(self.image, (783, 303))
	
	def mover_visao(self):
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

		camera_speed = 10
		if pygame.mouse.get_pos()[0] > 1100 and self.rect.x >= -320:
			self.rect.x -= camera_speed
			self.painel_direito.botoes["porta"][0].x -= camera_speed
			self.painel_direito.botoes["luz"][0].x -= camera_speed

		elif pygame.mouse.get_pos()[0] < 200 and self.rect.x <= 10:
			self.rect.x += camera_speed
			self.painel_direito.botoes["porta"][0].x += camera_speed
			self.painel_direito.botoes["luz"][0].x += camera_speed
	
	def update(self):

		self.mover_visao()
		
		self.painel_esquerdo.atualizar()
		self.painel_direito.atualizar()
		self.ventilador.desenhar()
