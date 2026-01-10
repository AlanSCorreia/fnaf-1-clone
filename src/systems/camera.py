from ..entities import entities_ids, ID


CURRENT_BACKGROUND: ID = entities_ids["SHOW_STAGE"]


def activate(camera_id,
			 event,
			 current_time: int,
			 rectangle,
			 frames,
			 states,
			 update_state) -> None:
	
	# Está fazendo 3 coisas:
		# Checando a colisão do mouse com o botão de ativação da câmera
		# Atualizando o State da câmera para ativa-lá
		# Atualizando o estado da animação de ativação da câmera para executa-lá e
			# definindo que ela não está executando em reverso
	# O nome também não está bom, pois dá a entender que a função
	# apenas ativa a câmera quando, na verdade, ela flipa o estado da câmera
	# ativando E desativando a mesma

	if rectangle.collidepoint(event.pos):
		if states[camera_id].is_available:
			update_state(camera_id,
						 current_time,
						 states)
			frames[camera_id].is_animation_playing = True
			frames[camera_id].is_reversing = not states[camera_id].state


def update_office_objects_position(update_position: int,
								   mouse_x_position: int,
								   object_position_offset: dict[str, int],
								   position_offset_limits: dict[str, int]) -> None:
	""" 
		Aqui foi necessário mover os Rects dos botoes direitos pois eles estavam sendo 
		renderizados fora da resolução da tela
		resolução.x da tela 1280 vesus a coordenada.x dos rects 1515
			isso ocorre porque a resolução.x da surface OFFICE é de 1600
			logo não dava pra clickar pois sempre estava fora do alcance
		a solução foi mover para a esquerda os Rects sempre que a tela estiver se mexendo
		para a direita até que estejam no limite da resolução.
		quando a tela vai para a esquerda os Rects são empurrados de volta para a direita,
		fora da resolução
	"""

	if mouse_x_position > 1100\
	and object_position_offset["base"] >= position_offset_limits["left"]:

		object_position_offset["vertical"] = -(update_position)

	elif mouse_x_position < 200\
	and object_position_offset["base"] <= position_offset_limits["right"]:

		object_position_offset["vertical"] = update_position

	else:

		object_position_offset["vertical"] = 0

	object_position_offset["base"] += object_position_offset["vertical"]


def update_camera_direction(camera_movement_id,
							current_time,
							states,
							update_state,
							background_position_offset: dict[str, int | bool],
							position_offset_limits: dict[str, int]) -> None:

	if states[camera_movement_id].state:
		if background_position_offset["base"] in range(position_offset_limits["left"]-3,
													   position_offset_limits["left"]+3):
			update_state(camera_movement_id,
						 current_time,
						 states,
						 False)

	else:
		if background_position_offset["base"] in range(position_offset_limits["right"]-3,
										  			   position_offset_limits["right"]+3):
			update_state(camera_movement_id,
						 current_time,
		 				 states,
						 True)


def update_background_position(camera_movement_id,
							   states,
							   update_position: int,
							   position_offset) -> None:

	if states[camera_movement_id].state:

		if states[camera_movement_id].is_available:
			position_offset["vertical"] = -(update_position)

		else:
			position_offset["vertical"] = 0

	else:

		if states[camera_movement_id].is_available:
			position_offset["vertical"] = update_position

		else:
			position_offset["vertical"] = 0

	position_offset["base"] += position_offset["vertical"]
	
	# print(deslocamentoComCamera["movimentoDisponivel"])


def update_current_background_position_while_changing_background(next_room_background_id: ID,
																 rectangles) -> None:
	global CURRENT_BACKGROUND
	
	previous_x_position: int = rectangles["backgrounds"][CURRENT_BACKGROUND].x
	CURRENT_BACKGROUND = next_room_background_id
	rectangles["backgrounds"][CURRENT_BACKGROUND].x = previous_x_position


def update_background_surface_based_on_animatronic(animatronic_id,
												   current_room_index,
												   routes,
												   background_surface,
												   surfaces_imports) -> None:
	
	room_id = routes[current_room_index[animatronic_id]]
	background_surface[room_id] = surfaces_imports[room_id][animatronic_id]

