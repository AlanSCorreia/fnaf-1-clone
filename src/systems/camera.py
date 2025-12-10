def activate(camera_id,
			 event,
			 current_time: int,
			 rectangle,
			 frames,
			 states,
			 update_state) -> None:

	if rectangle.collidepoint(event.pos):
		if states[camera_id].is_available:
			update_state(camera_id,
						 current_time,
						 states)
			frames[camera_id].is_animation_playing = True
			frames[camera_id].is_reversing = not states[camera_id].state


def update_dinamic_objects_position(update_position: int,
									mouse_x_position: int,
									position_offset: dict[str, int],
									position_offset_limit: dict[str, int]) -> None:
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

	if mouse_x_position > 1100\
	and position_offset["base"] >= position_offset_limit["min"]:
		position_offset["vertical"] = -(update_position)

	elif mouse_x_position < 200\
	and position_offset["base"] <= position_offset_limit["max"]:
		position_offset["vertical"] = update_position

	else:
		position_offset["vertical"] = 0

	position_offset["base"] += position_offset["vertical"]


def update_direction(camera_movement_id,
					 current_time,
					 states,
					 update_state,
					 position_offset: dict[str, int | bool],
					 position_offset_limit: dict[str, int]) -> None:

	if states[camera_movement_id].state:
		if position_offset["base"] in range(position_offset_limit["min"]-3,
											position_offset_limit["min"]+3):
			update_state(camera_movement_id,
						 current_time,
						 states,
						 False)

	else:
		if position_offset["base"] in range(position_offset_limit["max"]-3,
										  	position_offset_limit["max"]+3):
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


def update_background(room_id,
					  rectangles,
					  globals) -> None:
	
	x_position = rectangles["backgrounds"][globals.camera_background].x
	globals.camera_background = room_id
	rectangles["backgrounds"][globals.camera_background].x = x_position
