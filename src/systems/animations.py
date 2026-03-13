import src.components as components


def animation_queue():

	# Adicionar todas as animações ativas a uma queue
	# a cada loop será verificado quais animações devem ser atualizadas
	# criar a possíbilidade de uma animação adicionada só ser ativada após
	#	o termino de outra animação
	pass


def update(entity_id: int) -> None:
	
	if components.frames.FRAMES[entity_id].is_looping:
		return
	
	frame_index = components.frames.FRAMES[entity_id].current_frame
	still_running: bool = False

	if components.frames.FRAMES[entity_id].is_reversing:
		still_running = frame_index > 0
	
	else:
		still_running = frame_index < len(components.setup_surfaces.ALL_ANIMATED_PROPS[entity_id]["normal"])-1
	
	components.frames.FRAMES[entity_id].is_animation_playing = still_running


def check_frames_delay(
	frame_id: int,
	current_time: int
) -> bool:

	return current_time-components.frames.FRAMES[frame_id].last_time_frame\
		 > components.frames.FRAMES[frame_id].frames_delay


def update_frame(
	frame_id: int,
	animation_state: str,
	current_time: int
) -> None:

	components.frames.FRAMES[frame_id].last_time_frame: int = current_time
	components.surfaces.CURRENT_ANIMATED_PROPS[frame_id][animation_state] = components.setup_surfaces.ALL_ANIMATED_PROPS[frame_id][animation_state][components.frames.FRAMES[frame_id].current_frame]


def restart_animation(frame_id: int) -> None:
	
	if components.frames.FRAMES[frame_id].is_looping\
	or components.frames.FRAMES[frame_id].restart_needed:

		components.frames.FRAMES[frame_id].current_frame = 1


def increment_frame_index(frame_id):
	
	if components.frames.FRAMES[frame_id].current_frame < len(components.setup_surfaces.ALL_ANIMATED_PROPS[frame_id])-1:
		components.frames.FRAMES[frame_id].current_frame += 1

	else:
		restart_animation(
			frame_id
		)


def decrement_frame_index(frame_id):
	
	if components.frames.FRAMES[frame_id].current_frame > 0:
		components.frames.FRAMES[frame_id].current_frame -= 1
		
	else:
		restart_animation(
			frame_id
		)
