import src.ecs.entities as entities
import src.states.components as components
import src.states.systems as systems


def update(
	entity_id: int,
	current_time: int,
	static_state: bool | None=None
) -> None:

	components.STATES[entity_id].state = static_state\
											if static_state is not None\
											else not components.STATES[entity_id].state

	components.STATES[entity_id].last_availability_time = current_time
	components.STATES[entity_id].is_available = False
	

def update_availabilities(
	current_time: int
) -> None:

	for state_name in entities.IDS_FILTERED["STATES"]:

		if not components.STATES[entities.IDS[state_name]].is_available:

			if current_time-components.STATES[entities.IDS[state_name]].last_availability_time\
			> components.STATES[entities.IDS[state_name]].availability_delay:
				components.STATES[entities.IDS[state_name]].is_available = True
