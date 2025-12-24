from ..entities import flags
from ..surfaces_imports import backgrounds, inanimate, animated, rooms_buttons


surfaces = {
	"backgrounds": {
		flags.Flags.OFFICE			: backgrounds[flags.Flags.OFFICE		 	 ]["empty" ][0],
		flags.Flags.SHOW_STAGE		: backgrounds[flags.Flags.SHOW_STAGE 	 ][flags.Flags.FREDDY | flags.Flags.BONNIE | flags.Flags.CHICA][0],
		flags.Flags.DINING_AREA		: backgrounds[flags.Flags.DINING_AREA	 ]["empty" ],
		flags.Flags.PIRATE_COVE		: backgrounds[flags.Flags.PIRATE_COVE	 ]["stage1"],
		flags.Flags.WEST_HALL			: backgrounds[flags.Flags.WEST_HALL  	 ]["empty" ][0],
		flags.Flags.WEST_HALL_CORNER	: backgrounds[flags.Flags.WEST_HALL_CORNER]["empty" ],
		flags.Flags.SUPPLY_CLOSET		: backgrounds[flags.Flags.SUPPLY_CLOSET	 ]["empty" ],
		flags.Flags.EAST_HALL			: backgrounds[flags.Flags.EAST_HALL		 ]["empty" ],
		flags.Flags.EAST_HALL_CORNER	: backgrounds[flags.Flags.EAST_HALL_CORNER]["empty" ],
		flags.Flags.BACKSTAGE			: backgrounds[flags.Flags.BACKSTAGE	 	 ]["empty" ],
		flags.Flags.KITCHEN			: backgrounds[flags.Flags.KITCHEN		 ][0	   ],
		flags.Flags.RESTROOMS			: backgrounds[flags.Flags.RESTROOMS	 	 ]["empty" ]
	},
	"inanimate": {
		flags.Flags.LEFT_BUTTONS_PANEL : inanimate[flags.Flags.LEFT_BUTTONS_PANEL ][0],
		flags.Flags.RIGHT_BUTTONS_PANEL: inanimate[flags.Flags.RIGHT_BUTTONS_PANEL][0],
	},
	"animated": {
		flags.Flags.FAN    	: animated[flags.Flags.FAN		 ][0],
		flags.Flags.LEFT_DOOR : animated[flags.Flags.LEFT_DOOR  ][0],
		flags.Flags.RIGHT_DOOR: animated[flags.Flags.RIGHT_DOOR ][0],
	},
	"static": {
		flags.Flags.CAMERA		   : animated[flags.Flags.CAMERA			  ][0],
		flags.Flags.CAMERA_TRANSITION: animated[flags.Flags.CAMERA_TRANSITION][0]
	},
	"rooms_buttons": {
		flags.Flags.SHOW_STAGE 	  : rooms_buttons[flags.Flags.SHOW_STAGE		 ],
		flags.Flags.DINING_AREA	  : rooms_buttons[flags.Flags.DINING_AREA	 ],
		flags.Flags.PIRATE_COVE	  : rooms_buttons[flags.Flags.PIRATE_COVE	 ],
		flags.Flags.WEST_HALL  	  : rooms_buttons[flags.Flags.WEST_HALL		 ],
		flags.Flags.WEST_HALL_CORNER: rooms_buttons[flags.Flags.WEST_HALL_CORNER],
		flags.Flags.SUPPLY_CLOSET	  : rooms_buttons[flags.Flags.SUPPLY_CLOSET	 ],
		flags.Flags.EAST_HALL		  : rooms_buttons[flags.Flags.EAST_HALL	 	 ],
		flags.Flags.EAST_HALL_CORNER: rooms_buttons[flags.Flags.EAST_HALL_CORNER],
		flags.Flags.BACKSTAGE		  : rooms_buttons[flags.Flags.BACKSTAGE		 ],
		flags.Flags.KITCHEN		  : rooms_buttons[flags.Flags.KITCHEN		 ],
		flags.Flags.RESTROOMS		  : rooms_buttons[flags.Flags.RESTROOMS		 ]
	}
}