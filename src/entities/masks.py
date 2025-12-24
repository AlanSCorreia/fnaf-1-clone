from . import flags
from . import bitmasks


entities_masks = {
	flags.Flags.MOUSE			   : bitmasks.Bitmasks.STATE,
	flags.Flags.OFFICE			   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.BACKGROUND,
	flags.Flags.SHOW_STAGE		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.DINING_AREA		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.PIRATE_COVE		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.WEST_HALL		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.WEST_HALL_CORNER   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.SUPPLY_CLOSET	   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.EAST_HALL		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.EAST_HALL_CORNER   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.BACKSTAGE		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.KITCHEN			   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.RESTROOMS		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.BUTTON  | bitmasks.Bitmasks.BACKGROUND | bitmasks.Bitmasks.CAMERA,
	flags.Flags.FAN			 	   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.FRAME,
	flags.Flags.LEFT_DOOR 		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.FRAME,
	flags.Flags.RIGHT_DOOR		   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.FRAME,
	flags.Flags.LEFT_BUTTONS_PANEL : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE,
	flags.Flags.RIGHT_BUTTONS_PANEL: bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE,
	flags.Flags.LEFT_DOOR_BUTTON   : bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE     | bitmasks.Bitmasks.BUTTON | bitmasks.Bitmasks.ENERGY_USAGE,
	flags.Flags.RIGHT_DOOR_BUTTON  : bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE     | bitmasks.Bitmasks.BUTTON | bitmasks.Bitmasks.ENERGY_USAGE,
	flags.Flags.LEFT_LIGHT_BUTTON  : bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE     | bitmasks.Bitmasks.BUTTON | bitmasks.Bitmasks.ENERGY_USAGE,
	flags.Flags.RIGHT_LIGHT_BUTTON : bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE     | bitmasks.Bitmasks.BUTTON | bitmasks.Bitmasks.ENERGY_USAGE,
	flags.Flags.CAMERA			   : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.STATE | bitmasks.Bitmasks.FRAME 		   | bitmasks.Bitmasks.TRANSITION_FRAME | bitmasks.Bitmasks.STATIC | bitmasks.Bitmasks.ENERGY_USAGE,
	flags.Flags.CAMERA_TRANSITION  : bitmasks.Bitmasks.SURFACE   | bitmasks.Bitmasks.RECTANGLE | bitmasks.Bitmasks.FRAME | bitmasks.Bitmasks.TRANSITION_FRAME | bitmasks.Bitmasks.STATIC,
	flags.Flags.CAMERA_MOVEMENT	   : bitmasks.Bitmasks.STATE,
	flags.Flags.FREDDY			   : bitmasks.Bitmasks.ANIMATRONIC,
	flags.Flags.BONNIE			   : bitmasks.Bitmasks.ANIMATRONIC,
	flags.Flags.CHICA			   : bitmasks.Bitmasks.ANIMATRONIC,
	flags.Flags.FOXY			   : bitmasks.Bitmasks.ANIMATRONIC
}
