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


def update_surface(office_id,
				   animatronic_id,
				   button_id,
				   surface_id,
				   states,
				   surfaces,
				   surfaces_imports,
				   current_room,
				   final_destination) -> None:

	if states[button_id].state:
		if current_room[animatronic_id] == final_destination:
			surfaces[office_id] = surfaces_imports[office_id][animatronic_id]

		else:
			surfaces[office_id] = surfaces_imports[office_id]["empty"][surface_id]

	else:
		surfaces[office_id] = surfaces_imports[office_id]["empty"][0]


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
