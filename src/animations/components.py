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
										.extract_yaml_data("data/components/animations.yaml")\
										.items():

	ANIMATIONS[entity_name] = AnimationData(
		**animation_data
	)
