def animation_queue():

	# Adicionar todas as animações ativas a uma queue
	# a cada loop será verificado quais animações devem ser atualizadas
	# criar a possíbilidade de uma animação adicionada só ser ativada após
	#	o termino de outra animação
	pass


def check_frames_delay(frame_id,
					   frames,
					   current_time):
	
	return current_time-frames[frame_id].last_time_frame\
		 > frames[frame_id].frames_delay


def update_frame(frame_id,
				 surfaces,
				 frames,
				 surface_imports,
				 current_time):

	frames[frame_id].last_time_frame = current_time
	surfaces[frame_id] = surface_imports[frame_id][frames[frame_id].current_frame]


def restart_animation(frame_id,
					  frames,
					  index) -> None:
	
	if frames[frame_id].is_looping\
	or frames[frame_id].restart_needed:

		frames[frame_id].current_frame = index


def increment_frame_index(frame_id,
						  frames,
						  surface_imports):
	
	if frames[frame_id].current_frame < len(surface_imports[frame_id])-1:

		frames[frame_id].current_frame += 1

	else:

		restart_animation(frame_id,
						  frames,
						  0)


def decrement_frame(frame_id,
					frames,
					surface_imports):
	
	if frames[frame_id].current_frame > 0:

		frames[frame_id].current_frame -= 1
		
	else:

		restart_animation(frame_id,
						  frames,
						  len(surface_imports[frame_id])-1)
