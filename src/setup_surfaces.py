import src.import_functions as import_functions


# Descobrir qual é o type desta variavel global
path = "data/assets_paths_normalization"

############ Sprites ###############
BACKGROUNDS      = import_functions.extracted_dicts_from_yaml(f"{path}/backgrounds.yaml")
CAMERA_BUTTONS   = import_functions.extracted_dicts_from_yaml(f"{path}/camera_buttons.yaml")
INANIMATED_PROPS = import_functions.extracted_dicts_from_yaml(f"{path}/inanimated_props.yaml")
############ Sprites ###############

############ Animations ############
ANIMATED_PROPS = import_functions.generate_animations(f"{path}/animations/animated_props.yaml")
JUMPSCARES     = import_functions.generate_animations(f"{path}/animations/jumpscares.yaml")
############ Animations ############
