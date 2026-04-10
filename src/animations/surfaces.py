import src.setup_surfaces as setup_surfaces


CURRENT_ANIMATED_PROPS = {
	"FAN"		: {"normal": setup_surfaces.ALL_ANIMATED_PROPS["FAN"	   ]["normal"][1]},
	"LEFT_DOOR" : {"normal": setup_surfaces.ALL_ANIMATED_PROPS["LEFT_DOOR" ]["normal"][1]},
	"RIGHT_DOOR": {"normal": setup_surfaces.ALL_ANIMATED_PROPS["RIGHT_DOOR"]["normal"][1]},
}

CURRENT_JUMPSCARES = {
	"FREDDY": {
		"normal"  : setup_surfaces.ALL_JUMPSCARES["FREDDY"]["normal"  ][1],
		"no_power": setup_surfaces.ALL_JUMPSCARES["FREDDY"]["no_power"][1]
	},

	"BONNIE": {
		"normal": setup_surfaces.ALL_JUMPSCARES["BONNIE"]["normal"][1]
	},
	"CHICA" : {
		"normal": setup_surfaces.ALL_JUMPSCARES["CHICA" ]["normal"][1]
	},
	"FOXY"  : {
		"normal": setup_surfaces.ALL_JUMPSCARES["FOXY"  ]["normal"][1]
	},
}