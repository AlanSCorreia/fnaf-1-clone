from ..entities import flags


class Frame:
	def __init__(self,
			  	 is_animation_playing : bool,
				 is_looping		   	  : bool,
				 is_reversing		  : bool,
				 restart_needed	   	  : bool,
				 current_frame		  : int,
				 last_time_frame   	  : float,
				 frames_delay 		  : float) -> None:

		self.is_animation_playing = is_animation_playing
		self.is_looping 		  = is_looping
		self.is_reversing 		  = is_reversing
		self.restart_needed 	  = restart_needed
		self.current_frame 		  = current_frame
		self.last_time_frame 	  = last_time_frame
		self.frames_delay 		  = frames_delay


frames = {
	flags.Flags.FAN      		  : Frame( True,  True, False, False, 0, 0, 25),
	flags.Flags.LEFT_DOOR  	  	  : Frame(False, False, False, False, 0, 0, 25),
	flags.Flags.RIGHT_DOOR   	  : Frame(False, False, False, False, 0, 0, 25),
	flags.Flags.CAMERA	       	  : Frame(False, False, False, False, 0, 0, 25),
	flags.Flags.CAMERA_TRANSITION : Frame(False, False, False,  True, 0, 0, 25)
}