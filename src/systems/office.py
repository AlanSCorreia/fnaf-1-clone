def update_button_panel_surface(left_map_id,
								right_map_id,
								states,
								surfaces,
								surfaces_imports) -> None:

	for map_id in (left_map_id, right_map_id):
		if states[map_id[1]].state:
			
			if states[map_id[2]].state:
				surfaces[map_id[0]] = surfaces_imports[map_id[0]][3]

			else:
				surfaces[map_id[0]] = surfaces_imports[map_id[0]][1]

		elif states[map_id[2]].state:
			surfaces[map_id[0]] = surfaces_imports[map_id[0]][2]

		else:
			surfaces[map_id[0]] = surfaces_imports[map_id[0]][0]


def update_object_positions(update_position: int,
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
		

def deny_multiple_lights_on(left_map_id,
							right_map_id,
							states,
							update_state,
							current_time,
							surfaces,
							surfaces_imports) -> None:
	
	if states[left_map_id[2]].state and not states[left_map_id[2]].is_available:
		if states[right_map_id[2]].state and states[right_map_id[2]].is_available:
			update_state(right_map_id[2],
						 current_time,
						 states)

	elif states[right_map_id[2]].state and not states[right_map_id[2]].is_available:
		if states[left_map_id[2]].state and states[left_map_id[2]].is_available:
			update_state(left_map_id[2],
						 current_time,
						 states)
	
	update_button_panel_surface(left_map_id,
							 	right_map_id,
								states,
								surfaces,
								surfaces_imports)
