import pygame


def draw(display_surface,
		 entities_id,
		 surfaces: dict,
		 rectangles: dict) -> None:
	
	for entityId in entities_id:
		display_surface.blit(surfaces[entityId], rectangles[entityId])


def define_energy_usage(energy_usage_id,
						states) -> int:
	
	energy_consumption = 1
	for id in energy_usage_id:
		if states[id].state:
			energy_consumption += 1
	
	return energy_consumption


def debug(font: pygame.font.Font,
		  ingame_state,
		  ingame_states,
		  globals,
		  display_surface,
		  entities_id,
		  rectangles,
		  frames,
		  states):

	text = ''

	match ingame_state:
		case ingame_states.WITHOUT_CAMERA:
			text += f"{entities_id.OFFICE}\n"
			text += f"Eixo X: {rectangles["backgrounds"][entities_id.OFFICE].x} Eixo Y: {rectangles["backgrounds"][entities_id.OFFICE].y}\n"

			text += f"{states[entities_id.LEFT_DOOR].state}\n"
			text += f"ativado: {states[entities_id.LEFT_DOOR].state} esta disponível: {states[entities_id.LEFT_DOOR].is_available}\n"
			
			text += f"\n{entities_id.LEFT_BUTTONS_PANEL}\n"
			text += f"Eixo X : {rectangles["inanimate"][entities_id.LEFT_BUTTONS_PANEL].x} Eixo Y: {rectangles["inanimate"][entities_id.LEFT_BUTTONS_PANEL].y}\n"
			text += f"Botão da Porta: {states[entities_id.LEFT_DOOR_BUTTON].state} esta disponível: {states[entities_id.LEFT_DOOR_BUTTON].is_available}\n"
			text += f"Botão da Luz: {states[entities_id.LEFT_LIGHT_BUTTON].state} esta disponível: {states[entities_id.LEFT_LIGHT_BUTTON].is_available}\n"
			
			text += f"{states[entities_id.RIGHT_DOOR].state}\n"
			text += f"ativado: {states[entities_id.RIGHT_DOOR].state} esta disponível: {states[entities_id.RIGHT_DOOR].is_available}\n"
			
			text += f"\n{entities_id.RIGHT_BUTTONS_PANEL}\n"
			text += f"Eixo X: {rectangles["inanimate"][entities_id.RIGHT_BUTTONS_PANEL].x} Eixo Y: {rectangles["inanimate"][entities_id.RIGHT_BUTTONS_PANEL].y}\n"
			text += f"Botão da Porta: {states[entities_id.RIGHT_DOOR_BUTTON].state} esta disponível: {states[entities_id.RIGHT_DOOR_BUTTON].is_available}\n"
			text += f"Botão da Luz: {states[entities_id.RIGHT_LIGHT_BUTTON].state} esta disponível: {states[entities_id.RIGHT_LIGHT_BUTTON].is_available}\n"

			text += "\nCamera\n"
			text += f"esta Disponivel: {states[entities_id.CAMERA].is_available}"
			text += f"\nAnimação está ocorrendo: {frames[entities_id.CAMERA].is_animation_playing}"
			text += f"\nQuadro atual: {frames[entities_id.CAMERA].current_frame}"

			text += "\nAnimação de transição/ativação da camera"
			text += f"\nAnimação está ocorrendo: {frames[entities_id.CAMERA_TRANSITION].is_animation_playing}"
			text += f"\nQuadro atual: {frames[entities_id.CAMERA_TRANSITION].current_frame}"
		
		case ingame_state.WITH_CAMERA:
			text += f"Sala atual: {globals.camera_background}\n"
			text += f"Eixo X: {rectangles["backgrounds"][globals.camera_background].x} Eixo Y: {rectangles["backgrounds"][globals.camera_background].y}\n"
			text += f"\nPosition offset: {globals.camera_position_offset}\n"


	font_surface = font.render(text, True, pygame.color.Color("white"))
	font_rectangle = font_surface.get_rect(topleft=(0, 0))

	display_surface.blit(font_surface, font_rectangle)
