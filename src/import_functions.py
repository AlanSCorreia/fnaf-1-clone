import dataclasses

import yaml
import pygame


@dataclasses.dataclass
class Animation:
	entity_name: str
	state: str
	path: str
	frame_count: int


def extract_yaml_data(path: str) -> dict:
	
	with open(path) as stream:
		file = yaml.safe_load(stream)

	return file


def generate_animation_dict(entity_name: str,
							animation_state: str,
							animation_information: dict) -> dict:

	animation_object = Animation(
		entity_name,
		animation_state,
		animation_information["path"],
		animation_information["frame_count"]
	)

	new_animation_dict = dict()

	for frame in range(1, animation_object.frame_count+1):

		new_animation_dict[frame] = pygame.image.load(
			animation_object.path.format(frame=frame)
		).convert_alpha()

	return new_animation_dict


def generate_animations(file_path) -> dict:

	import src.entities as entities

	animations_dicts = extract_yaml_data(file_path)
	new_dict: dict = dict()

	for entity_name_state, animation_information in animations_dicts.items():
		entity_name, animation_state = entity_name_state.split(" ")

		if entities.IDS[entity_name] not in new_dict:
			new_dict[entities.IDS[entity_name]] = dict()

		new_dict[entities.IDS[entity_name]][animation_state] = generate_animation_dict(
			entity_name,
			animation_state,
			animation_information
		)
		# print(f"{inner_id_str} -> {nested_frames[entities.IDS[id_str]][inner_id_str]}")

	return new_dict


def generate_surfaces_from_nested_dict(surfaces_dictionary: dict) -> dict:
	
	temporary_dict = dict()
	
	for key, value in surfaces_dictionary.items():
		temporary_dict[key] = pygame.image.load(value).convert_alpha()
	
	return temporary_dict


def converted_yaml_dicts(data) -> dict:
	import src.entities as entities

	new_dict = dict()

	for entity_name, value in data.items():
		
		if isinstance(value, dict):
			new_dict[entities.IDS[entity_name]] = generate_surfaces_from_nested_dict(value)

		else:
			new_dict[entities.IDS[entity_name]] = pygame.image.load(value).convert_alpha()
	
	return new_dict


def extracted_dicts_from_yaml(directory_path):
	extracted_data = extract_yaml_data(directory_path)

	return converted_yaml_dicts(extracted_data)
