import src.entities as entities
import src.components as components
import src.systems as systems


def update(
	entity_id: int,
	current_time: int,
	static_state: bool | None=None
) -> None:

	if static_state is None:
		components.states.STATES[entity_id].state = not components.states.STATES[entity_id].state
	else:
		components.states.STATES[entity_id].state = static_state

	components.states.STATES[entity_id].last_availability_time = current_time
	components.states.STATES[entity_id].is_available = False
	

def update_availabilities(current_time: int) -> None:
	for state_name in entities.IDS_FILTERED["STATES"]:

		if not components.states.STATES[entities.IDS[state_name]].is_available:

			if current_time - components.states.STATES[entities.IDS[state_name]].last_availability_time\
			> components.states.STATES[entities.IDS[state_name]].availability_delay:
				components.states.STATES[entities.IDS[state_name]].is_available = True


def update_door(
	door_id,
	button_id,
	current_time
) -> None:
	
	if components.states.STATES[door_id].state ^ components.states.STATES[button_id].state:

		systems.states.update(
			door_id,
			current_time
		)

		components.frames.FRAMES[door_id].is_animation_playing = True
		components.frames.FRAMES[door_id].is_reversing = not components.states.STATES[door_id].state
