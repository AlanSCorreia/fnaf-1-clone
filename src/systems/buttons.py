import pygame
import src.systems.states as system_states


def mouse_hover(mouse_position,
				rect: pygame.Rect) -> bool:
	return rect.collidepoint(mouse_position)


def has_button_been_clicked(
	button_id,
	rectangle,
	states,
	current_time,
	mouse_position: tuple[int, int]
) -> bool:
	
	had_collision = False
		
	if mouse_hover(mouse_position, rectangle)\
	and states[button_id].is_available:
		
		system_states.update(
			button_id,
		 	current_time,
		 	states
		)
			   
		had_collision = True

	return had_collision
