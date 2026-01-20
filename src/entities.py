from enum import IntFlag, auto

from custom_types import str_ID, int_ID


	##################### DECLARATION #####################
class Bitmasks(IntFlag):
	ANIMATRONIC  	 = auto()
	BACKGROUND	  	 = auto()
	BUTTON 		  	 = auto()
	CAMERA 		   	 = auto()
	ENERGY_USAGE	 = auto()
	FRAME 		  	 = auto()
	RECTANGLE	  	 = auto()
	STATE 		  	 = auto()
	STATIC	  	  	 = auto()
	SURFACE		  	 = auto()
	TRANSITION_FRAME = auto()


next_entity_id: int_ID = 0
entities_ids: dict[str_ID, int_ID] = dict()
components_masks: dict[int_ID, Bitmasks] = {}
filtered_entities_ids: dict[str, list[int_ID]] = {}


def create_entity(name: str) -> None:
	global next_entity_id, entities_ids

	entities_ids[name] = next_entity_id
	next_entity_id += 1


def has_component(entity_masks,
				  component_mask) -> bool:
	
    return (entity_masks & component_mask) == component_mask


def has_all_components(entities_masks,
					   components_masks) -> bool:
	
	return all(has_component(entities_masks, component_mask)
			   for component_mask in components_masks)


def has_any_components(entities_masks,
					   components_masks) -> bool:
	
    return any(has_component(entities_masks, component_mask)
			   for component_mask in components_masks)


def filter_entities_by_components(entities_ids: dict[str, int_ID],
								  components_masks: dict[int_ID, Bitmasks],
								  accepted_bitmasks: list[Bitmasks],
								  rejected_bitmasks: list[Bitmasks] | None) -> list[int_ID]:
	
	result: list[int_ID] = []

	for entity_id in entities_ids.values():
		if accepted_bitmasks:
			if rejected_bitmasks:
				if has_all_components(components_masks[entity_id], accepted_bitmasks)\
				and not has_any_components(components_masks[entity_id], rejected_bitmasks):
					result.append(entity_id)

			else:
				if has_all_components(components_masks[entity_id], accepted_bitmasks):
					result.append(entity_id)
	
	return result


##################### DECLARATION #####################

##################### IMPLEMENTATION #####################

##################### IMPLEMENTATION #####################

#
	# MOUSE -> 128
	# OFFICE -> 578
	# SHOW_STAGE -> 718
	# DINING_AREA -> 718
	# PIRATE_COVE -> 718
	# WEST_HALL -> 718
	# WEST_HALL_CORNER -> 718
	# SUPPLY_CLOSET -> 718
	# EAST_HALL -> 718
	# EAST_HALL_CORNER -> 718
	# BACKSTAGE -> 718
	# KITCHEN -> 718
	# RESTROOMS -> 718
	# FAN -> 608
	# LEFT_DOOR -> 736
	# RIGHT_DOOR -> 736
	# LEFT_BUTTONS_PANEL -> 576
	# RIGHT_BUTTONS_PANEL -> 576
	# LEFT_DOOR_BUTTON -> 212
	# RIGHT_DOOR_BUTTON -> 212
	# LEFT_LIGHT_BUTTON -> 212
	# RIGHT_LIGHT_BUTTON -> 212
	# FREDDY -> 2032
	# BONNIE -> 1888
	# CHICA -> 128
	# FOXY -> 1
	# CAMERA -> 1
	# CAMERA_WHITE_BARS_TRANSITION -> 1
	# CAMERA_BACKGROUND_MOVEMENT -> 1
