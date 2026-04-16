import src.setup_surfaces 		 as setup_surfaces
import src.animations.components as components
import src.animations.surfaces 	 as surfaces

import src.states.components as states_components
import src.states.systems	 as states_systems


class AnimationsQueue:
	def __init__(
		self
	) -> None:

		self.queue: list[str] = list()

	def add_animation(
		self,
		animation_name: str
	) -> None:

		self.queue.append(animation_name)
		components.ANIMATIONS[animation_name].is_animation_playing = True

	def update(
		self
	) -> None:
	
		# Adicionar todas as animações ativas a uma queue
		# a cada loop será verificado quais animações devem ser atualizadas
		# criar a possíbilidade de uma animação adicionada só ser ativada após
		#	o termino de outra animação
		if not components.ANIMATIONS[self.queue[-1]].is_animation_playing:
			self.queue.pop()

			if len(self.queue)\
			> 0:
				components.ANIMATIONS[self.queue[-1]].is_animation_playing = True


def update(
	animatino_name: str
) -> None:
	
	if components.ANIMATIONS[animatino_name].is_looping:
		return
	
	frame_index = components.ANIMATIONS[animatino_name].current_frame
	components.ANIMATIONS[animatino_name].is_animation_playing = is_animation_still_playing(
		animatino_name,
		frame_index
	)


def is_animation_still_playing(
	animation_name: str,
	frame_index: int
) -> bool:

	return (frame_index > 0) if components.ANIMATIONS[animation_name].is_reversing\
	  else (frame_index < len(setup_surfaces.ANIMATED_PROPS[animation_name]["normal"])-1)


def check_frames_delay(
	animation_name: str,
	current_time: int
) -> bool:

	return current_time-components.ANIMATIONS[animation_name].last_frame_time\
		 > components.ANIMATIONS[animation_name].frames_delay


#TODO: Arrumar
def update_frame(
	animation_name: str,
	animation_state: str,
	current_time: int
) -> None:

	components.ANIMATIONS[animation_name].last_frame_time: int = current_time
	pass


def restart_animation(
	animation_name: str
) -> None:
	
	if components.ANIMATIONS[animation_name].is_looping\
	or components.ANIMATIONS[animation_name].restart_needed:

		components.ANIMATIONS[animation_name].current_frame = 1


def increment_frame_index(
	animation_name: str
) -> None:
	
	if components.ANIMATIONS[animation_name].current_frame\
	< len(setup_surfaces.ANIMATED_PROPS[animation_name])-1:
		components.ANIMATIONS[animation_name].current_frame += 1

	else:
		restart_animation(
			animation_name
		)


def decrement_frame_index(
	animation_name: str
) -> None:
	
	if components.ANIMATIONS[animation_name].current_frame\
	> 1:
		components.ANIMATIONS[animation_name].current_frame -= 1
		
	else:
		restart_animation(
			animation_name
		)
