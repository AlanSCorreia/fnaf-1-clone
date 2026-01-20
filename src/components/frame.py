from dataclasses import dataclass

from ..entities import entities_ids, ID


@dataclass
class Frame:

	is_animation_playing: bool
	is_looping			: bool
	is_reversing		: bool
	restart_needed		: bool
	current_frame		: int = 0
	last_time_frame		: int = 0
	frames_delay		: int = 25


frames: dict[ID, Frame] = {
	entities_ids["FAN"				]: Frame( True,  True, False, False),
	entities_ids["LEFT_DOOR"		]: Frame(False, False, False, False),
	entities_ids["RIGHT_DOOR"		]: Frame(False, False, False, False),
	entities_ids["CAMERA"			]: Frame(False, False, False, False),
	entities_ids["CAMERA_TRANSITION"]: Frame(False, False, False,  True)
}