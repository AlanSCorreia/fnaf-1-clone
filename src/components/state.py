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
	flags.Flags.DINING_AREA		: State(500),
	flags.Flags.PIRATE_COVE		: State(500),
	flags.Flags.WEST_HALL			: State(500),
	flags.Flags.WEST_HALL_CORNER	: State(500),
	flags.Flags.SUPPLY_CLOSET		: State(500),
	flags.Flags.EAST_HALL			: State(500),
	flags.Flags.EAST_HALL_CORNER	: State(500),
	flags.Flags.BACKSTAGE			: State(500),
	flags.Flags.KITCHEN			: State(500),
	flags.Flags.RESTROOMS			: State(500),
	flags.Flags.LEFT_DOOR			: State(500),
	flags.Flags.RIGHT_DOOR 		: State(500),
	flags.Flags.LEFT_DOOR_BUTTON	: State(500),
	flags.Flags.RIGHT_DOOR_BUTTON  : State(500),
	flags.Flags.LEFT_LIGHT_BUTTON  : State(250),
	flags.Flags.RIGHT_LIGHT_BUTTON : State(250),
	flags.Flags.CAMERA 	 		: State(500),
	flags.Flags.CAMERA_MOVEMENT	: State(1000, True)
}