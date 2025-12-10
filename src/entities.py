from enum import Flag, auto


class Entities(Flag):
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


class Bitmasks(Flag):
	ANIMATRONIC  	 = auto()
	CAMERA 		   	 = auto()
	BACKGROUND	  	 = auto()
	BUTTON 		  	 = auto()
	STATE 		  	 = auto()
	STATIC	  	  	 = auto()
	FRAME 		  	 = auto()
	TRANSITION_FRAME = auto()
	RECTANGLE	  	 = auto()
	SURFACE		  	 = auto()


entities_mask = {
	Entities.MOUSE				: Bitmasks.STATE,
	Entities.OFFICE			 	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.BACKGROUND,
	Entities.SHOW_STAGE		 	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.DINING_AREA		: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.PIRATE_COVE		: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.WEST_HALL			: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.WEST_HALL_CORNER	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.SUPPLY_CLOSET		: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.EAST_HALL			: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.EAST_HALL_CORNER	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.BACKSTAGE			: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.KITCHEN			: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.RESTROOMS			: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.BUTTON  | Bitmasks.BACKGROUND | Bitmasks.CAMERA,
	Entities.FAN			 	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.FRAME,
	Entities.LEFT_DOOR 		 	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.FRAME,
	Entities.RIGHT_DOOR		 	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.FRAME,
	Entities.LEFT_BUTTONS_PANEL : Bitmasks.SURFACE   | Bitmasks.RECTANGLE,
	Entities.RIGHT_BUTTONS_PANEL: Bitmasks.SURFACE   | Bitmasks.RECTANGLE,
	Entities.LEFT_DOOR_BUTTON   : Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON,
	Entities.RIGHT_DOOR_BUTTON	: Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON,
	Entities.LEFT_LIGHT_BUTTON	: Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON,
	Entities.RIGHT_LIGHT_BUTTON : Bitmasks.RECTANGLE | Bitmasks.STATE     | Bitmasks.BUTTON,
	Entities.CAMERA			 	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.STATE | Bitmasks.FRAME 		   | Bitmasks.TRANSITION_FRAME | Bitmasks.STATIC,
	Entities.CAMERA_TRANSITION	: Bitmasks.SURFACE   | Bitmasks.RECTANGLE | Bitmasks.FRAME | Bitmasks.TRANSITION_FRAME | Bitmasks.STATIC,
	Entities.CAMERA_MOVEMENT	: Bitmasks.STATE,
	Entities.FREDDY			 	: Bitmasks.ANIMATRONIC,
	Entities.BONNIE			 	: Bitmasks.ANIMATRONIC,
	Entities.CHICA				: Bitmasks.ANIMATRONIC,
	Entities.FOXY				: Bitmasks.ANIMATRONIC
}
