def animation_queue():

	# Adicionar todas as animações ativas a uma queue
	# a cada loop será verificado quais animações devem ser atualizadas
	# criar a possíbilidade de uma animação adicionada só ser ativada após
	#	o termino de outra animação
	pass


def update(entity_id: int,
		   frames: dict,
		   animation_component: dict) -> None:
	
	if frames[entity_id].is_looping:
		return
	
	frame_index = frames[entity_id].current_frame
	still_running: bool = False

	if frames[entity_id].is_reversing:
		still_running = frame_index > 0
	
	else:
		still_running = frame_index < len(animation_component[entity_id])-1
	
	frames[entity_id].is_animation_playing = still_running


def check_frames_delay(frame_id,
					   frames,
					   current_time):
	
	return current_time-frames[frame_id].last_time_frame\
		 > frames[frame_id].frames_delay


def update_frame(frame_id,
				 frames,
				 animation_state,
				 current_animated_props,
				 all_animated_surfaces,
				 current_time):

	frames[frame_id].last_time_frame: int = current_time
	current_animated_props[frame_id][animation_state] = all_animated_surfaces[frame_id][animation_state][frames[frame_id].current_frame]


def restart_animation(frame_id,
					  frames,
					  index) -> None:
	
	if frames[frame_id].is_looping\
	or frames[frame_id].restart_needed:

		frames[frame_id].current_frame = index


def increment_frame_index(frame_id,
						  frames,
						  all_animated_surfaces):
	
	if frames[frame_id].current_frame < len(all_animated_surfaces[frame_id])-1:
		frames[frame_id].current_frame += 1

	else:
		restart_animation(frame_id,
						  frames,
						  1)


def decrement_frame_index(frame_id,
						  frames,
						  all_animated_surfaces):
	
	if frames[frame_id].current_frame > 0:
		frames[frame_id].current_frame -= 1
		
	else:
		restart_animation(frame_id,
						  frames,
						  len(all_animated_surfaces[frame_id])-1)
