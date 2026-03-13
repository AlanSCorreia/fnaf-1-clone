import pygame

from src import components, systems


def update(
	camera_id: int,
	mouse_position: tuple[int, int],
	current_time: int,
	rectangle: pygame.Rect
) -> None:

	if rectangle.collidepoint(mouse_position):
		if components.states.STATES[camera_id].is_available:
			
			systems.states.update(
				camera_id,
				current_time
			)

			components.frames.FRAMES[camera_id].is_animation_playing = True
			components.frames.FRAMES[camera_id].is_reversing = not components.states.STATES[camera_id].state


def set_direction(
	camera_movement_id,
	current_time,
	position_offset_background,
	position_offset_background_limits
) -> None:
		
	def _setting_direction(
		direction: str,
		boolean: bool=False
	):
		if position_offset_background["base"] in range(position_offset_background_limits[direction]-3,
													   position_offset_background_limits[direction]+3):
			systems.states.update(
				camera_movement_id,
				current_time,
				boolean
			)

	if components.states.STATES[camera_movement_id].state:
		_setting_direction("left")

	else:
		_setting_direction("right", True)


def update_background_based_on_animatronic(
	animatronic_id,
	index_current_room,
	routes,
	surface_background,
	surfaces_imports
) -> None:
	
	room_id = routes[index_current_room[animatronic_id]]
	surface_background[room_id] = surfaces_imports[room_id][animatronic_id]


# Provavelmente inutilizado
def get_last_background_position(
	previous_background_id: int,
	background_rectangles
) -> int:
	"""
	Get the previous background X value and returns it
	"""

	previous_x_position: int = background_rectangles[previous_background_id].x
	return previous_x_position


def update_background_surface(
	background_id,
	rooms,
	surfaces,
	all_surfaces
) -> None:
	"""
	Change the background surface
	"""
	surfaces[rooms] = all_surfaces[rooms][background_id]


def update_background_movement(
	camera_movement_id,
	states,
	update_position: int,
	position_offset
) -> None:

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
