import src.states.components as states_components
import src.states.systems 	 as states_systems


def update_object_positions(
	update_position: int,
	mouse_x_position: int,
	object_position_offset: dict[str, int],
	position_offset_limits: dict[str, int]
) -> None:
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


def set_camera_direction(
	camera_movement_id: int,
	current_time: int,
	position_offset_background,
	position_offset_background_limits
) -> None:

	direction: str = "left" if states_components.STATES[camera_movement_id].state\
				else "right"

	if position_offset_background["base"] in range(position_offset_background_limits[direction]-3,
													position_offset_background_limits[direction]+3):
		states_systems.update(
			camera_movement_id,
			current_time,
			direction.startswith("right")
		)
