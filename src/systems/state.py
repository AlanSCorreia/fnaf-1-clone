def update(entity_id,
		   current_time,
		   states,
		   state=None) -> None:

	if state is None:
		states[entity_id].state = not states[entity_id].state
	else:
		states[entity_id].state = state

	states[entity_id].last_availability_time = current_time
	states[entity_id].is_available = False


def update_availability(state_id,
						states,
						current_time):

	if not states[state_id].is_available:
		if current_time - states[state_id].last_availability_time > states[state_id].availability_delay:
			states[state_id].is_available = True


def update_ingame(camera_id,
				  globals,
				  ingame_states,
				  states):
	
	if not states[camera_id].state:
		globals.ingame_state = ingame_states.WITHOUT_CAMERA
	else:
		if states[camera_id].is_available:
			globals.ingame_state = ingame_states.WITH_CAMERA


def update_button(button_id,
				  rectangles,
				  states,
				  current_time,
				  mouse_position: tuple[int, int]) -> bool:
	
	had_collision = False
		
	if rectangles[button_id].collidepoint(mouse_position)\
	and states[button_id].is_available:
		update(button_id,
		 	   current_time,
		 	   states)
		had_collision = True

	return had_collision


def update_animation(entity_id,
					 frames,
					 surface_imports):
	
	if frames[entity_id].is_looping:
		return
	
	frame_index = frames[entity_id].current_frame
	still_running = frame_index > 0 if frames[entity_id].is_reversing\
					else frame_index < len(surface_imports[entity_id])-1
	
	frames[entity_id].is_animation_playing = still_running


def update_door(door_id,
				button_id,
				current_time,
				update_state,
				states,
				frames) -> None:
	
	if states[door_id].state ^ states[button_id].state:
		update_state(door_id,
			   		 current_time,
			   		 states)
		frames[door_id].is_animation_playing = True
		frames[door_id].is_reversing = not states[door_id].state
