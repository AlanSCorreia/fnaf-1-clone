from enum import Flag, auto


class Flags(Flag):
	MOUSE 				   = auto()
	OFFICE	   		   	   = auto()
	SHOW_STAGE 	   		   = auto()
	DINING_AREA 	   	   = auto()
	PIRATE_COVE 	   	   = auto()
	WEST_HALL 	   		   = auto()
	WEST_HALL_CORNER	   = auto()
	SUPPLY_CLOSET		   = auto()
	EAST_HALL 	   		   = auto()
	EAST_HALL_CORNER	   = auto()
	BACKSTAGE 	   		   = auto()
	KITCHEN 	   		   = auto()
	RESTROOMS 	   		   = auto()

	FAN 			   	   = auto()
	
	# Portas
	LEFT_DOOR 		   	   = auto()
	RIGHT_DOOR 		       = auto()

	# Painel de Botões
	LEFT_BUTTONS_PANEL 	   = auto()
	RIGHT_BUTTONS_PANEL    = auto()
	
	# Botões das Portas
	LEFT_DOOR_BUTTON   	   = auto()
	RIGHT_DOOR_BUTTON      = auto()

	# Botões das Luzes
	LEFT_LIGHT_BUTTON 	   = auto()
	RIGHT_LIGHT_BUTTON 	   = auto()

	# Animatronicos
	FREDDY				   = auto()
	BONNIE				   = auto()
	CHICA				   = auto()
	FOXY				   = auto()

	CAMERA			   	   = auto()
	CAMERA_TRANSITION	   = auto()
	CAMERA_MOVEMENT	   	   = auto()
