import src.import_functions as import_functions


# Descobrir qual é o type desta variavel global
ALL_BACKGROUNDS:		  dict = dict()
ALL_CAMERA_BUTTONS:		  dict = dict()
ALL_INANIMATED_PROPS:	  dict = dict()
ALL_ANIMATED_PROPS:		  dict = dict()
ALL_JUMPSCARES:			  dict = dict()


path = "data/assets_paths_normalization"

ALL_BACKGROUNDS = import_functions.extracted_dicts_from_yaml(f"{path}/backgrounds.yaml")
ALL_CAMERA_BUTTONS = import_functions.extracted_dicts_from_yaml(f"{path}/camera_buttons.yaml")
ALL_INANIMATED_PROPS = import_functions.extracted_dicts_from_yaml(f"{path}/inanimated_props.yaml")

ALL_ANIMATED_PROPS = import_functions.generate_animations(f"{path}/animations/animated_props.yaml")
ALL_JUMPSCARES = import_functions.generate_animations(f"{path}/animations/jumpscares.yaml")
