from enum import IntFlag, auto


	##################### DECLARATION #####################
type ID = int
next_entity_id: ID = 0
entities_ids: dict[str, ID] = dict()


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


def create_entity(name: str) -> None:
	global next_entity_id, entities_ids

	entities_ids[name] = next_entity_id
	next_entity_id += 1


def has_component(entity_mask,
				  components) -> bool:
	
    return (entity_mask & components) == components


def has_all_components(entities_mask,
					   bit_masks) -> bool:
	
	return all(has_component(entities_mask, bit_mask)
			   for bit_mask in bit_masks)


def has_any_components(entities_mask,
					   bit_masks) -> bool:
	
    return any(has_component(entities_mask, bit_mask)
			   for bit_mask in bit_masks)


def filter_entities_by_components(entities_ids: dict[str, ID],
								  accepted_bitmasks: list[Bitmasks],
								  rejected_bitmasks: list[Bitmasks] | None,
								  components_masks: dict[ID, Bitmasks]) -> list[ID]:
	
	result: list[ID] = []

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

for entity in ("MOUSE", "OFFICE", "SHOW_STAGE",
			   "DINING_AREA", "PIRATE_COVE", "WEST_HALL",
			   "WEST_HALL_CORNER", "SUPPLY_CLOSET", "EAST_HALL",
			   "EAST_HALL_CORNER", "BACKSTAGE", "KITCHEN",
			   "RESTROOMS", "FAN", "LEFT_DOOR",
			   "RIGHT_DOOR", "LEFT_BUTTONS_PANEL", "RIGHT_BUTTONS_PANEL",
			   "LEFT_DOOR_BUTTON", "RIGHT_DOOR_BUTTON", "LEFT_LIGHT_BUTTON",
			   "RIGHT_LIGHT_BUTTON", "FREDDY", "BONNIE",
			   "CHICA", "FOXY", "CAMERA",
			   "CAMERA_STATIC_TRANSITION", "CAMERA_BACKGROUND_MOVEMENT"):

	create_entity(entity)


components_masks: dict[ID, Bitmasks] = {
	entities_ids["MOUSE"			  ]: Bitmasks.STATE,
	entities_ids["OFFICE"			  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.BACKGROUND,
	entities_ids["SHOW_STAGE"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["DINING_AREA"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["PIRATE_COVE"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["WEST_HALL"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["WEST_HALL_CORNER"	  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["SUPPLY_CLOSET"	  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["EAST_HALL"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["EAST_HALL_CORNER"	  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["BACKSTAGE"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["KITCHEN"			  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["RESTROOMS"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	entities_ids["FAN"				  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.FRAME,
	entities_ids["LEFT_DOOR"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.FRAME,
	entities_ids["RIGHT_DOOR"		  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.FRAME,
	entities_ids["LEFT_BUTTONS_PANEL" ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE,
	entities_ids["RIGHT_BUTTONS_PANEL"]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE,
	entities_ids["LEFT_DOOR_BUTTON"	  ]: Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON | Bitmasks.ENERGY_USAGE,
	entities_ids["RIGHT_DOOR_BUTTON"  ]: Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON | Bitmasks.ENERGY_USAGE,
	entities_ids["LEFT_LIGHT_BUTTON"  ]: Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON | Bitmasks.ENERGY_USAGE,
	entities_ids["RIGHT_LIGHT_BUTTON" ]: Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON | Bitmasks.ENERGY_USAGE,
	entities_ids["CAMERA"			  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE  | Bitmasks.FRAME 		   | Bitmasks.TRANSITION_FRAME | Bitmasks.STATIC | Bitmasks.ENERGY_USAGE,
	entities_ids["CAMERA_TRANSITION"  ]: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.FRAME  | Bitmasks.TRANSITION_FRAME | Bitmasks.STATIC,
	entities_ids["CAMERA_MOVEMENT"	  ]: Bitmasks.STATE,
	entities_ids["FREDDY"			  ]: Bitmasks.ANIMATRONIC,
	entities_ids["BONNIE"			  ]: Bitmasks.ANIMATRONIC,
	entities_ids["CHICA"			  ]: Bitmasks.ANIMATRONIC,
	entities_ids["FOXY"				  ]: Bitmasks.ANIMATRONIC
}


ids: dict[str, list[ID]] = {

	"static_surfaces": filter_entities_by_components(entities_ids,
												[Bitmasks.SURFACE,
												Bitmasks.STATIC],
												[Bitmasks.CAMERA],
												components_masks),

	"inanimate_surfaces": filter_entities_by_components(entities_ids,
													[Bitmasks.SURFACE],
													[Bitmasks.FRAME,
													Bitmasks.STATIC,
													Bitmasks.BACKGROUND],
													components_masks),

	"inanimate_rectangles": filter_entities_by_components(entities_ids,
													[Bitmasks.RECTANGLE],
													[Bitmasks.FRAME,
													Bitmasks.STATIC,
													Bitmasks.BACKGROUND],
													components_masks),

	"animated_surfaces": filter_entities_by_components(entities_ids,
												[Bitmasks.FRAME],
												[Bitmasks.STATIC],
												components_masks),

	"animated_rectangles": filter_entities_by_components(entities_ids,
													[Bitmasks.FRAME],
													[Bitmasks.STATIC],
													components_masks),

	"states": filter_entities_by_components(entities_ids,
										[Bitmasks.STATE],
										None,
										components_masks),

	"left_button_panel": [entities_ids["LEFT_BUTTONS_PANEL"],
						  entities_ids["LEFT_DOOR_BUTTON"  ],
						  entities_ids["LEFT_LIGHT_BUTTON" ]],

	"right_button_panel": [entities_ids["RIGHT_BUTTONS_PANEL"],
						   entities_ids["RIGHT_DOOR_BUTTON"  ],
						   entities_ids["RIGHT_LIGHT_BUTTON" ]],

	"panel_buttons": filter_entities_by_components(entities_ids,
											[Bitmasks.BUTTON],
											[Bitmasks.CAMERA],
											components_masks),

	"have_frames": filter_entities_by_components(entities_ids,
										[Bitmasks.FRAME],
										None,
										components_masks),

	"cameras": filter_entities_by_components(entities_ids,
										[Bitmasks.CAMERA],
										None,
										components_masks),

	"rooms_buttons": filter_entities_by_components(entities_ids,
											[Bitmasks.BUTTON,
												Bitmasks.CAMERA],
											None,
											components_masks),

	"animatronics": filter_entities_by_components(entities_ids,
											[Bitmasks.ANIMATRONIC],
											None,
											components_masks),

	"energy_usage": filter_entities_by_components(entities_ids,
											[Bitmasks.ENERGY_USAGE],
											None,
											components_masks)
}

##################### IMPLEMENTATION #####################
