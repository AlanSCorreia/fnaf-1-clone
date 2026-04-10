import src.ecs.components as components
import src.ecs.systems as systems

# TODO: Remover tudo o que não seja apenas lógica desta função
# RECOMENDAÇÕES:
	# Criar uma função que recebe o valor devolvido desta para desenhar a surface correta
	# Retornar algo como "{"lado": "esquerdo", "porta": "ativado", "luz": "desativado"}"
def update_button_panel_surface(
	left_map_id: list[int],
	right_map_id: list[int]
) -> None:

	for map_id in (
		left_map_id,
		right_map_id	
	):

		if components.states.STATES[map_id[1]].state:
			
			if components.states.STATES[map_id[2]].state:
				components.surfaces.CURRENT_INANIMATED_PROPS[map_id[0]] = components.setup_surfaces.ALL_INANIMATED_PROPS[map_id[0]]["all_on"]

			else:
				components.surfaces.CURRENT_INANIMATED_PROPS[map_id[0]] = components.setup_surfaces.ALL_INANIMATED_PROPS[map_id[0]]["door_on"]

		elif components.states.STATES[map_id[2]].state:
			components.surfaces.CURRENT_INANIMATED_PROPS[map_id[0]] = components.setup_surfaces.ALL_INANIMATED_PROPS[map_id[0]]["light_on"]

		else:
			components.surfaces.CURRENT_INANIMATED_PROPS[map_id[0]] = components.setup_surfaces.ALL_INANIMATED_PROPS[map_id[0]]["all_off"]


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
		

def deny_multiple_lights_on(
	left_map_id: list[int],
	right_map_id: list[int],
	current_time: int
) -> None:

	for just_turned_on, was_already_on in ((left_map_id[2], right_map_id[2]),
										   (right_map_id[2], left_map_id[2])):
		# Se o botão da luz de um lado acabou de ser ativado:
		if all([
			components.states.STATES[just_turned_on].state,
			not components.states.STATES[just_turned_on].is_available
		]):
			# Se o botão da luz de outra já estava ativado:
			if all([
				components.states.STATES[was_already_on].state,
				components.states.STATES[was_already_on].is_available
			]):
				# Desativar o botão que já estava ativado
				systems.states.update(
					was_already_on,
					current_time
				)
	
	update_button_panel_surface(
		left_map_id,
		right_map_id
	)
