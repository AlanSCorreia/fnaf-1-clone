# import src.custom_types as custom_types
import src.entities as entities
import src.components.setup_surfaces as setup_surfaces


CURRENT_BACKGROUNDS= {
    entities.IDS["OFFICE"			]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["OFFICE"			  ]]["empty"	],
    entities.IDS["SHOW_STAGE"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["SHOW_STAGE"		  ]]["with_freddy_bonnie_chica"],
    entities.IDS["DINING_AREA"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["DINING_AREA"	  ]]["empty"	],
    entities.IDS["PIRATE_COVE"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["PIRATE_COVE"	  ]]["stage_1"  ],
    entities.IDS["WEST_HALL"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["WEST_HALL"		  ]]["empty_1"  ],
    entities.IDS["WEST_HALL_CORNER" ]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["WEST_HALL_CORNER" ]]["empty"	],
    entities.IDS["SUPPLY_CLOSET"    ]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["SUPPLY_CLOSET"	  ]]["empty"	],
    entities.IDS["EAST_HALL"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["EAST_HALL"		  ]]["empty_1"  ],
    entities.IDS["EAST_HALL_CORNER" ]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["EAST_HALL_CORNER" ]]["empty"	],
    entities.IDS["BACKSTAGE"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["BACKSTAGE"		  ]]["empty"	],
    entities.IDS["RESTROOMS"		]: setup_surfaces.ALL_BACKGROUNDS[entities.IDS["RESTROOMS"		  ]]["empty"	],
}

CURRENT_INANIMATED_PROPS = {
    entities.IDS["LEFT_BUTTONS_PANEL" ]: setup_surfaces.ALL_INANIMATED_PROPS[entities.IDS["LEFT_BUTTONS_PANEL" ]]["all_off"],
    entities.IDS["RIGHT_BUTTONS_PANEL"]: setup_surfaces.ALL_INANIMATED_PROPS[entities.IDS["RIGHT_BUTTONS_PANEL"]]["all_off"],
    entities.IDS["LEFT_DOOR"          ]: setup_surfaces.ALL_INANIMATED_PROPS[entities.IDS["LEFT_DOOR"          ]]["opened" ],
    entities.IDS["RIGHT_DOOR"         ]: setup_surfaces.ALL_INANIMATED_PROPS[entities.IDS["RIGHT_DOOR"         ]]["closed" ],
}

CURRENT_ANIMATED_PROPS = {
    entities.IDS["FAN"		 ]: {"normal": setup_surfaces.ALL_ANIMATED_PROPS[entities.IDS["FAN"	      ]]["normal"][1]},
    entities.IDS["LEFT_DOOR" ]: {"normal": setup_surfaces.ALL_ANIMATED_PROPS[entities.IDS["LEFT_DOOR" ]]["normal"][1]},
    entities.IDS["RIGHT_DOOR"]: {"normal": setup_surfaces.ALL_ANIMATED_PROPS[entities.IDS["RIGHT_DOOR"]]["normal"][1]},
}

CURRENT_CAMERA_BUTTONS = {
    entities.IDS["SHOW_STAGE"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["SHOW_STAGE"	  ]],
    entities.IDS["DINING_AREA"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["DINING_AREA"	  ]],
    entities.IDS["PIRATE_COVE"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["PIRATE_COVE"	  ]],
    entities.IDS["WEST_HALL"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["WEST_HALL"		  ]],
    entities.IDS["WEST_HALL_CORNER"]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["WEST_HALL_CORNER"]],
    entities.IDS["SUPPLY_CLOSET"   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["SUPPLY_CLOSET"	  ]],
    entities.IDS["EAST_HALL"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["EAST_HALL"		  ]],
    entities.IDS["EAST_HALL_CORNER"]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["EAST_HALL_CORNER"]],
    entities.IDS["BACKSTAGE"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["BACKSTAGE"		  ]],
    entities.IDS["KITCHEN"		   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["KITCHEN"		  ]],
    entities.IDS["RESTROOMS"	   ]: setup_surfaces.ALL_CAMERA_BUTTONS[entities.IDS["RESTROOMS"		  ]],
}

CURRENT_JUMPSCARES = {
    entities.IDS["FREDDY"]: {
        "normal"  : setup_surfaces.ALL_JUMPSCARES[entities.IDS["FREDDY"]]["normal"  ][1],
        "no_power": setup_surfaces.ALL_JUMPSCARES[entities.IDS["FREDDY"]]["no_power"][1]
    },

    entities.IDS["BONNIE"]: {
        "normal": setup_surfaces.ALL_JUMPSCARES[entities.IDS["BONNIE"]]["normal"][1]
    },
    entities.IDS["CHICA" ]: {
        "normal": setup_surfaces.ALL_JUMPSCARES[entities.IDS["CHICA" ]]["normal"][1]
    },
    entities.IDS["FOXY"  ]: {
        "normal": setup_surfaces.ALL_JUMPSCARES[entities.IDS["FOXY"  ]]["normal"][1]
    },
}
