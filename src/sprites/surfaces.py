import src.setup_surfaces as setup_surfaces


CURRENT_BACKGROUNDS= {
	"OFFICE"		  : setup_surfaces.ALL_BACKGROUNDS["OFFICE"			  ]["empty"					  ],
	"SHOW_STAGE"	  : setup_surfaces.ALL_BACKGROUNDS["SHOW_STAGE"		  ]["with_freddy_bonnie_chica"],
	"DINING_AREA"	  : setup_surfaces.ALL_BACKGROUNDS["DINING_AREA"	  ]["empty"					  ],
	"PIRATE_COVE"     : setup_surfaces.ALL_BACKGROUNDS["PIRATE_COVE"	  ]["stage_1"  				  ],
	"WEST_HALL"		  : setup_surfaces.ALL_BACKGROUNDS["WEST_HALL"		  ]["empty_1"  				  ],
	"WEST_HALL_CORNER": setup_surfaces.ALL_BACKGROUNDS["WEST_HALL_CORNER" ]["empty"	 				  ],
	"SUPPLY_CLOSET"   : setup_surfaces.ALL_BACKGROUNDS["SUPPLY_CLOSET"	  ]["empty"	 				  ],
	"EAST_HALL"		  : setup_surfaces.ALL_BACKGROUNDS["EAST_HALL"		  ]["empty_1"				  ],
	"EAST_HALL_CORNER": setup_surfaces.ALL_BACKGROUNDS["EAST_HALL_CORNER" ]["empty"	 				  ],
	"BACKSTAGE"		  : setup_surfaces.ALL_BACKGROUNDS["BACKSTAGE"		  ]["empty"	 				  ],
	"RESTROOMS"		  : setup_surfaces.ALL_BACKGROUNDS["RESTROOMS"		  ]["empty"	 				  ],
}

CURRENT_INANIMATED_PROPS = {
	"LEFT_BUTTONS_PANEL" : setup_surfaces.ALL_INANIMATED_PROPS["LEFT_BUTTONS_PANEL" ]["all_off"],
	"RIGHT_BUTTONS_PANEL": setup_surfaces.ALL_INANIMATED_PROPS["RIGHT_BUTTONS_PANEL"]["all_off"],
	"LEFT_DOOR"          : setup_surfaces.ALL_INANIMATED_PROPS["LEFT_DOOR"          ]["opened" ],
	"RIGHT_DOOR"         : setup_surfaces.ALL_INANIMATED_PROPS["RIGHT_DOOR"         ]["closed" ],
}

CURRENT_CAMERA_BUTTONS = {
	"SHOW_STAGE"	  : setup_surfaces.ALL_CAMERA_BUTTONS["SHOW_STAGE"	  	],
	"DINING_AREA"	  : setup_surfaces.ALL_CAMERA_BUTTONS["DINING_AREA"	  	],
	"PIRATE_COVE"	  : setup_surfaces.ALL_CAMERA_BUTTONS["PIRATE_COVE"	  	],
	"WEST_HALL"	   	  : setup_surfaces.ALL_CAMERA_BUTTONS["WEST_HALL"		],
	"WEST_HALL_CORNER": setup_surfaces.ALL_CAMERA_BUTTONS["WEST_HALL_CORNER"],
	"SUPPLY_CLOSET"   : setup_surfaces.ALL_CAMERA_BUTTONS["SUPPLY_CLOSET"	],
	"EAST_HALL"	   	  : setup_surfaces.ALL_CAMERA_BUTTONS["EAST_HALL"		],
	"EAST_HALL_CORNER": setup_surfaces.ALL_CAMERA_BUTTONS["EAST_HALL_CORNER"],
	"BACKSTAGE"	   	  : setup_surfaces.ALL_CAMERA_BUTTONS["BACKSTAGE"		],
	"KITCHEN"		  : setup_surfaces.ALL_CAMERA_BUTTONS["KITCHEN"		  	],
	"RESTROOMS"	   	  : setup_surfaces.ALL_CAMERA_BUTTONS["RESTROOMS"		],
}
