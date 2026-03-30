import src.animations.surfaces as surfaces


ANIMATED_PROPS = {
	"FAN"		: {"normal": surfaces.CURRENT_ANIMATED_PROPS["FAN"		 ]["normal"].get_rect(topleft=( 783, 303))},
	"LEFT_DOOR" : {"normal": surfaces.CURRENT_ANIMATED_PROPS["LEFT_DOOR" ]["normal"].get_rect(topleft=(  70,  30))},
	"RIGHT_DOOR": {"normal": surfaces.CURRENT_ANIMATED_PROPS["RIGHT_DOOR"]["normal"].get_rect(topleft=(1265,  30))},
}

JUMPSCARES: dict[str | int, dict[str, int] | dict[str, dict[str, int]]] = {
	"FREDDY": {
        "normal"  : surfaces.CURRENT_JUMPSCARES["FREDDY"]["normal"  ].get_rect(topleft=(0, 0)),
        "no_power": surfaces.CURRENT_JUMPSCARES["FREDDY"]["no_power"].get_rect(topleft=(0, 0))
    },

    "BONNIE": {
        "normal": surfaces.CURRENT_JUMPSCARES["BONNIE"]["normal"].get_rect(topleft=(0, 0))
    },
    "CHICA" : {
        "normal": surfaces.CURRENT_JUMPSCARES["CHICA" ]["normal"].get_rect(topleft=(0, 0))
    },
    "FOXY"  : {
        "normal": surfaces.CURRENT_JUMPSCARES["FOXY"  ]["normal"].get_rect(topleft=(0, 0))
    },
}