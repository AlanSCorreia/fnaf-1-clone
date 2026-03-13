import os
import dataclasses

import src.components.nights as nights
import src.import_functions as import_functions
import src.entities as entities


@dataclasses.dataclass
class Animatronic:
	current_room_index: int
	current_room_name: str | list[str] | None
	movement_opportunity_delay: int
	difficult_levels: dict[nights.Nights, int]
	routes: dict[int | str, str | list[str]]


def convert_difficult_levels_keys(difficult_levels):

	new_difficult_level_dict = dict()

	for key, value in difficult_levels.items():
		new_difficult_level_dict[nights.Nights[key.upper()]] = value
	
	return new_difficult_level_dict


def generate_animatronic_object(animatronic_information) -> Animatronic:

	animatronic_information["difficult_levels"] = convert_difficult_levels_keys(animatronic_information["difficult_levels"])

	new_animatronic = Animatronic(
		animatronic_information["current_room_index"],
		animatronic_information["current_room_name"],
		animatronic_information["movement_opportunity_delay"],
		animatronic_information["difficult_levels"],
		animatronic_information["routes"]
	)

	return new_animatronic


ANIMATRONICS: dict[int, Animatronic] = dict()
root = "data/animatronics"


for _, _, directories_names in os.walk(root):
	for directory_name in directories_names:

		animatronic_name: str = directory_name.split(".")[0].upper()
		animatronic_information = import_functions.extract_yaml_data(f"{root}/{directory_name}")

		ANIMATRONICS[entities.IDS[animatronic_name]] = generate_animatronic_object(animatronic_information)
