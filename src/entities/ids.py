from ..systems.bitmask import filter_entities_components
from . import bitmasks
from . import flags
from . import masks


static_surfaces = filter_entities_components(flags.Flags,
											 [bitmasks.Bitmasks.SURFACE,
			 								  bitmasks.Bitmasks.STATIC],
											 [bitmasks.Bitmasks.CAMERA],
											 masks.entities_masks)

inanimate_surfaces = filter_entities_components(flags.Flags,
												[bitmasks.Bitmasks.SURFACE],
												[bitmasks.Bitmasks.FRAME,
												bitmasks.Bitmasks.STATIC,
												bitmasks.Bitmasks.BACKGROUND],
												masks.entities_masks)

inanimate_rectangles = filter_entities_components(flags.Flags,
												  [bitmasks.Bitmasks.RECTANGLE],
												  [bitmasks.Bitmasks.FRAME,
			   									  bitmasks.Bitmasks.STATIC,
												  bitmasks.Bitmasks.BACKGROUND],
												  masks.entities_masks)

animated_surfaces = filter_entities_components(flags.Flags,
											   [bitmasks.Bitmasks.FRAME],
											   [bitmasks.Bitmasks.STATIC],
											   masks.entities_masks)

animated_rectangles = filter_entities_components(flags.Flags,
												 [bitmasks.Bitmasks.FRAME],
												 [bitmasks.Bitmasks.STATIC],
												 masks.entities_masks)

states = filter_entities_components(flags.Flags,
									[bitmasks.Bitmasks.STATE],
									None,
									masks.entities_masks)

left_button_panel = [flags.Flags.LEFT_BUTTONS_PANEL,
					 flags.Flags.LEFT_DOOR_BUTTON,
					 flags.Flags.LEFT_LIGHT_BUTTON]

right_button_panel = [flags.Flags.RIGHT_BUTTONS_PANEL,
					  flags.Flags.RIGHT_DOOR_BUTTON,
					  flags.Flags.RIGHT_LIGHT_BUTTON]

panel_buttons = filter_entities_components(flags.Flags,
										   [bitmasks.Bitmasks.BUTTON],
										   [bitmasks.Bitmasks.CAMERA],
										   masks.entities_masks)

frames = filter_entities_components(flags.Flags,
									[bitmasks.Bitmasks.FRAME],
									None,
									masks.entities_masks)

cameras = filter_entities_components(flags.Flags,
									[bitmasks.Bitmasks.CAMERA],
									None,
									masks.entities_masks)

rooms_buttons = filter_entities_components(flags.Flags,
										   [bitmasks.Bitmasks.BUTTON,
			  								bitmasks.Bitmasks.CAMERA],
										   None,
										   masks.entities_masks)

animatronics = filter_entities_components(flags.Flags,
										  [bitmasks.Bitmasks.ANIMATRONIC],
										  None,
										  masks.entities_masks)

energy_usage = filter_entities_components(flags.Flags,
										  [bitmasks.Bitmasks.ENERGY_USAGE],
										  None,
										  masks.entities_masks)