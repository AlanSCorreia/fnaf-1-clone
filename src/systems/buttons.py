import src.components.states as components_states
import pygame
import src.systems.states as system_states


def mouse_hover(
	mouse_position: tuple[int, int],
	rectangle: pygame.Rect
) -> bool:
	return rectangle.collidepoint(mouse_position)


# Pode ser mais robusto checando quando o botão é apertado e quando ele é solto
# Mas para o escopo desse projeto está bom assim
def has_button_been_clicked(
	button_id: int,
	mouse_position: tuple[int, int],
	rectangle: pygame.Rect,
	current_time: int
) -> bool:

	has_been_clicked = False

	if mouse_hover(mouse_position, rectangle)\
	and components_states.STATES[button_id].is_available:

		system_states.update(
			button_id,
		 	current_time
		)

		has_been_clicked = True

	return has_been_clicked
