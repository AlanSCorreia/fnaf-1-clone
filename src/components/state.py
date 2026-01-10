<<<<<<< HEAD
from ..entities import flags


class State:
	def __init__(self,
			  	 availability_delay: int,
				 state: bool=False) -> None:

		self.state: bool = state
		self.is_available: bool = True
		self.last_availability_time: int = 0
		self.availability_delay: int = availability_delay


states = {
	flags.Flags.MOUSE				: State(100),
	flags.Flags.SHOW_STAGE			: State(500),
	flags.Flags.DINING_AREA			: State(500),
	flags.Flags.PIRATE_COVE			: State(500),
	flags.Flags.WEST_HALL			: State(500),
	flags.Flags.WEST_HALL_CORNER	: State(500),
	flags.Flags.SUPPLY_CLOSET		: State(500),
	flags.Flags.EAST_HALL			: State(500),
	flags.Flags.EAST_HALL_CORNER	: State(500),
	flags.Flags.BACKSTAGE			: State(500),
	flags.Flags.KITCHEN				: State(500),
	flags.Flags.RESTROOMS			: State(500),
	flags.Flags.LEFT_DOOR			: State(500),
	flags.Flags.RIGHT_DOOR 			: State(500),
	flags.Flags.LEFT_DOOR_BUTTON	: State(500),
	flags.Flags.RIGHT_DOOR_BUTTON  	: State(500),
	flags.Flags.LEFT_LIGHT_BUTTON  	: State(250),
	flags.Flags.RIGHT_LIGHT_BUTTON 	: State(250),
	flags.Flags.CAMERA 	 			: State(500),
	flags.Flags.CAMERA_MOVEMENT		: State(1000, True)
=======
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
>>>>>>> e35898a (commit apenas para deixar eu mudar de branch)
}