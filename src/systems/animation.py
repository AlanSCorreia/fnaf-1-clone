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


def increment_frame(frame_id,
					frames,
					surface_imports):
	
	if frames[frame_id].current_frame < len(surface_imports[frame_id])-1:
		frames[frame_id].current_frame += 1

	else:
		if frames[frame_id].is_looping\
		or frames[frame_id].restart_needed:
			frames[frame_id].current_frame = 0


def decrement_frame(frame_id,
					frames,
					surface_imports):
	
	if frames[frame_id].current_frame > 0:
		frames[frame_id].current_frame -= 1
		
	else:
		if frames[frame_id].is_looping\
		or frames[frame_id].restart_needed:
			frames[frame_id].current_frame = len(surface_imports[frame_id])-1
