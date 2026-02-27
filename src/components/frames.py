from dataclasses import dataclass

import src.import_functions as import_functions
import src.entities as entities


@dataclass
class Frame:

	is_animation_playing: bool
	is_looping			: bool
	is_reversing		: bool
	restart_needed		: bool
	current_frame		: int = 0
	last_time_frame		: int = 0
	frames_delay		: int = 25


FRAMES: dict[int, Frame] = dict()

yaml_file = import_functions.extract_yaml_data("data/components/frames.yaml")


for entity_name, frame_data in yaml_file.items():
	FRAMES[entities.IDS[entity_name]] = Frame(
		frame_data["is_animation_playing"],
		frame_data["is_looping"],
		frame_data["is_reversing"],
		frame_data["restart_needed"],
		frame_data["current_frame"],
		frame_data["last_time_frame"],
		frame_data["frames_delay"]
	)
