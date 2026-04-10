from dataclasses import dataclass

import src.import_functions as import_functions


@dataclass
class AnimationData:
	is_linked_to		: bool
	is_animation_playing: bool
	is_looping			: bool
	is_reversing		: bool
	restart_needed		: bool
	current_frame		: int = 0
	last_frame_time		: int = 0
	frames_delay		: int = 25


ANIMATIONS: dict[str, AnimationData] = dict()


for entity_name, animation_data in import_functions\
										.extract_yaml_data("data/components/frames.yaml")\
										.items():
	# ANIMATIONS[entity_name] = AnimationData(
	# 	animation_data[""],
	# 	animation_data["is_animation_playing"],
	# 	animation_data["is_looping"],
	# 	animation_data["is_reversing"],
	# 	animation_data["restart_needed"],
	# 	animation_data["current_frame"],
	# 	animation_data["last_time_frame"],
	# 	animation_data["frames_delay"]
	# )
	ANIMATIONS[entity_name] = AnimationData(
		**animation_data
	)
