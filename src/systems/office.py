def update_button_panel_surface(map_id,
								states,
								surfaces,
								surfaces_imports) -> None:

	panel_id 	    = map_id[0]
	door_button_id  = map_id[1]
	light_button_id = map_id[2]

	if states[door_button_id].state:
		if states[light_button_id].state:
			surfaces[panel_id] = surfaces_imports[panel_id][3]
		else:
			surfaces[panel_id] = surfaces_imports[panel_id][1]
	elif states[light_button_id].state:
		surfaces[panel_id] = surfaces_imports[panel_id][2]
	else:
		surfaces[panel_id] = surfaces_imports[panel_id][0]


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


def deny_multiple_lights_on(left_light_id,
							right_light_id,
							map_id,
							states,
							update_state,
							current_time,
							surfaces,
							surfaces_imports) -> None:
	
	if states[left_light_id].state and not states[left_light_id].is_available:
		if states[right_light_id].state and states[right_light_id].is_available:
			update_state(right_light_id,
						 current_time,
						 states)

	elif states[right_light_id].state and not states[right_light_id].is_available:
		if states[left_light_id].state and states[left_light_id].is_available:
			update_state(left_light_id,
						 current_time,
						 states)
	
	update_button_panel_surface(map_id,
								states,
								surfaces,
								surfaces_imports)
