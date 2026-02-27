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
