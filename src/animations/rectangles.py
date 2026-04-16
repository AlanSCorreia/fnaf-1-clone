import src.setup_surfaces as setup_surfaces


ANIMATED_PROPS = {
	"FAN"		: {"normal": setup_surfaces.ANIMATED_PROPS["FAN"	   ]["normal"][0].get_rect(topleft=( 783, 303))},
	"LEFT_DOOR" : {"normal": setup_surfaces.ANIMATED_PROPS["LEFT_DOOR" ]["normal"][0].get_rect(topleft=(  70,  30))},
	"RIGHT_DOOR": {"normal": setup_surfaces.ANIMATED_PROPS["RIGHT_DOOR"]["normal"][0].get_rect(topleft=(1265,  30))},
}

JUMPSCARES: dict[str | int, dict[str, int] | dict[str, dict[str, int]]] = {
	"FREDDY": {
        "normal"  : setup_surfaces.JUMPSCARES["FREDDY"]["normal"  ][0].get_rect(topleft=(0, 0)),
        "no_power": setup_surfaces.JUMPSCARES["FREDDY"]["no_power"][0].get_rect(topleft=(0, 0))
    },

    "BONNIE": {
        "normal": setup_surfaces.JUMPSCARES["BONNIE"]["normal"][0].get_rect(topleft=(0, 0))
    },
    "CHICA" : {
        "normal": setup_surfaces.JUMPSCARES["CHICA" ]["normal"][0].get_rect(topleft=(0, 0))
    },
    "FOXY"  : {
        "normal": setup_surfaces.JUMPSCARES["FOXY"  ]["normal"][0].get_rect(topleft=(0, 0))
    },
}