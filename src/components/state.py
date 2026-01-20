from dataclasses import dataclass

from ..entities import entities_ids, ID


@dataclass
class State:

	state: bool = False
	is_available: bool = True
	last_availability_time: int = 0
	availability_delay: int


states: dict[ID, State] = {
	entities_ids["MOUSE"	 		 ]: State(availability_delay=100),
	entities_ids["SHOW_STAGE"		 ]: State(availability_delay=500),
	entities_ids["DINING_AREA"		 ]: State(availability_delay=500),
	entities_ids["PIRATE_COVE"		 ]: State(availability_delay=500),
	entities_ids["WEST_HALL"		 ]: State(availability_delay=500),
	entities_ids["WEST_HALL_CORNER"	 ]: State(availability_delay=500),
	entities_ids["SUPPLY_CLOSET"	 ]: State(availability_delay=500),
	entities_ids["EAST_HALL"		 ]: State(availability_delay=500),
	entities_ids["EAST_HALL_CORNER"	 ]: State(availability_delay=500),
	entities_ids["BACKSTAGE"		 ]: State(availability_delay=500),
	entities_ids["KITCHEN"			 ]: State(availability_delay=500),
	entities_ids["RESTROOMS"		 ]: State(availability_delay=500),
	entities_ids["LEFT_DOOR"		 ]: State(availability_delay=500),
	entities_ids["RIGHT_DOOR"		 ]: State(availability_delay=500),
	entities_ids["LEFT_DOOR_BUTTON"	 ]: State(availability_delay=500),
	entities_ids["RIGHT_DOOR_BUTTON" ]: State(availability_delay=500),
	entities_ids["LEFT_LIGHT_BUTTON" ]: State(availability_delay=250),
	entities_ids["RIGHT_LIGHT_BUTTON"]: State(availability_delay=250),
	entities_ids["CAMERA"			 ]: State(availability_delay=500),
	entities_ids["CAMERA_MOVEMENT"	 ]: State(availability_delay=1000, state=True)
}