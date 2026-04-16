import src.states.components as states_components
import src.states.systems as states_systems

# TODO: Remover tudo o que não seja apenas lógica desta função
# RECOMENDAÇÕES:
	# Criar uma função que recebe o valor devolvido desta para desenhar a surface correta
	# Retornar algo como "{"lado": "esquerdo", "porta": "ativado", "luz": "desativado"}"
def update_button_panel(
	door_button_id: int,
	light_button_id: int,
) -> dict[str, str]:
	"""
		This function returns a dict with the current state of the buttons
		of the button panel to use to update it
	"""
	state = {True: "on", False: "off"}
	return {"door" : state[states_components.STATES[door_button_id].state ],
			"light": state[states_components.STATES[light_button_id].state]}


# Checar em que lado do tela o click foi feito
# para fazer uma checagem ao invés de duas, se possível
def deny_multiple_lights_on(
	left_light_id: int,
	right_light_id: int,
	current_time: int
) -> None:

	for just_turned_on, was_already_on in ((left_light_id, right_light_id),
										   (right_light_id, left_light_id)):
		# Se o botão da luz de um lado acabou de ser ativado:
		if all([
			states_components.STATES[just_turned_on].state,
			not states_components.STATES[just_turned_on].is_available
		]):
			# Se o botão da luz de outra já estava ativado:
			if all([
				states_components.STATES[was_already_on].state,
				states_components.STATES[was_already_on].is_available
			]):
				# Desativar o botão que já estava ativado
				states_systems.update(
					was_already_on,
					current_time
				)

	# Talvez disparar um evento pra avisar que o button painel deveria mudar a sprite?


def update_door(
	door_id: int,
	button_id: int,
	current_time: int
) -> None:
	
	if states_components.STATES[door_id].state ^ states_components.STATES[button_id].state:

		states_systems.update(
			door_id,
			current_time
		)
