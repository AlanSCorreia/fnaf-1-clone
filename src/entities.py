import enum

import src.import_functions as import_functions


##################### DECLARATION #####################

class Bitmasks(enum.IntFlag):
	ANIMATION		 = enum.auto()
	ANIMATRONIC  	 = enum.auto()
	BACKGROUND	  	 = enum.auto()
	BUTTON 		  	 = enum.auto()
	CAMERA 		   	 = enum.auto()
	DOOR 			 = enum.auto()
	ENERGY_USAGE	 = enum.auto()
	STATE 		  	 = enum.auto()
	SPRITE		  	 = enum.auto()


ID_NEXT			: int				   = 0
IDS				: dict[str, 	  int] = dict()
IDS_FILTERED	: dict[str, list[str]] = dict()
MASKS_COMPONENTS: dict[int,  Bitmasks] = dict()


def create_entity(entity_name: str) -> None:
	global ID_NEXT, IDS

	IDS[entity_name] = ID_NEXT
	ID_NEXT += 1


def has_component(masks_entity: int,
				  mask_component: Bitmasks) -> bool:
	
    return (masks_entity & mask_component) == mask_component


def has_all_components(masks_entity: int,
					   masks_components_strings: list[str] | None=None) -> bool:

	if masks_components_strings is None:
		return False

	return all(has_component(masks_entity, Bitmasks[mask_component])
			   for mask_component in masks_components_strings)


def has_any_components(masks_entity: int,
					   masks_components_strings: list[str] | None=None) -> bool:

	if masks_components_strings is None:
		return False

	return any(has_component(masks_entity, Bitmasks[mask_component])
			   for mask_component in masks_components_strings)


def is_entity_valid_component_archtype(entity_name,
									   bitmasks_accepted: list[str],
									   bitmasks_rejected: list[str] | None) -> bool:

	return has_all_components(MASKS_COMPONENTS[IDS[entity_name]],
								bitmasks_accepted)\
																			\
	and not has_any_components(MASKS_COMPONENTS[IDS[entity_name]],
								bitmasks_rejected)


def get_components_archtypes(bitmasks_accepted: list[str],
							 bitmasks_rejected: list[str] | None) -> list[str]:
	
	return list(entity_name for entity_name in IDS.keys()
				if is_entity_valid_component_archtype(entity_name,
													  bitmasks_accepted,
													  bitmasks_rejected))


def add_components_masks(entity_name: str,
						 masks_components_string: str) -> None:

	for index, mask_component in enumerate(masks_components_string.split(" | ")):

		if index > 0:
			MASKS_COMPONENTS[IDS[entity_name]] |= Bitmasks[mask_component]
			continue

		MASKS_COMPONENTS[IDS[entity_name]] = Bitmasks[mask_component]


def add_filtered_id(entity_name: str,
					components_accepted: list[str],
					components_rejected: list[str] | list) -> None:

	IDS_FILTERED[entity_name] = get_components_archtypes(components_accepted,
												    	 components_rejected)


##################### DECLARATION #####################

##################### IMPLEMENTATION #####################


roots = ("data/entities.yaml", "data/id_filters.yaml")

for entity_name, masks_components_string in import_functions.extract_yaml_data(roots[0]).items():

	create_entity(entity_name)

	add_components_masks(
		entity_name,
		masks_components_string
	)


for entity_name, masks_components_dict in import_functions.extract_yaml_data(roots[1]).items():
	add_filtered_id(
		entity_name.upper(),
		masks_components_dict["components_accepted"],
		masks_components_dict["components_rejected"]
	)

##################### IMPLEMENTATION #####################
