import src.states.systems as states_systems
import src.states.components as states_components


def update(
	camera_id: int,
	current_time: int
) -> None:

	if states_components.STATES[camera_id].is_available:

		states_systems.update(
			camera_id,
			current_time
		)
