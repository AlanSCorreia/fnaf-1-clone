from systems.bitmask import filter_entities_components
import entities


static_surfaces = filter_entities_components(entities.Entities,
											 [entities.Bitmasks.SURFACE,
			 								  entities.Bitmasks.STATIC],
											 [entities.Bitmasks.CAMERA],
											 entities.entities_mask)

inanimate_surfaces = filter_entities_components(entities.Entities,
												   [entities.Bitmasks.SURFACE],
												   [entities.Bitmasks.FRAME,
													entities.Bitmasks.STATIC,
													entities.Bitmasks.BACKGROUND],
												   entities.entities_mask)

inanimate_rectangles = filter_entities_components(entities.Entities,
												[entities.Bitmasks.RECTANGLE],
												[entities.Bitmasks.FRAME,
			 									 entities.Bitmasks.STATIC,
												 entities.Bitmasks.BACKGROUND],
												entities.entities_mask)

animated_surfaces = filter_entities_components(entities.Entities,
											   [entities.Bitmasks.FRAME],
											   [entities.Bitmasks.STATIC],
											   entities.entities_mask)

animated_rectangles = filter_entities_components(entities.Entities,
										   [entities.Bitmasks.FRAME],
										   [entities.Bitmasks.STATIC],
										   entities.entities_mask)

states = filter_entities_components(entities.Entities,
									[entities.Bitmasks.STATE],
									None,
									entities.entities_mask)

left_button_panel = [entities.Entities.LEFT_BUTTONS_PANEL,
					 entities.Entities.LEFT_DOOR_BUTTON,
					 entities.Entities.LEFT_LIGHT_BUTTON]

right_button_panel = [entities.Entities.RIGHT_BUTTONS_PANEL,
					  entities.Entities.RIGHT_DOOR_BUTTON,
					  entities.Entities.RIGHT_LIGHT_BUTTON]

panel_buttons = filter_entities_components(entities.Entities,
										   [entities.Bitmasks.BUTTON],
										   [entities.Bitmasks.CAMERA],
										   entities.entities_mask)

frames = filter_entities_components(entities.Entities,
									[entities.Bitmasks.FRAME],
									None,
									entities.entities_mask)

camera = filter_entities_components(entities.Entities,
									[entities.Bitmasks.CAMERA],
									None,
									entities.entities_mask)

rooms_buttons = filter_entities_components(entities.Entities,
										   [entities.Bitmasks.BUTTON,
			  								entities.Bitmasks.CAMERA],
										   None,
										   entities.entities_mask)

animatronics = filter_entities_components(entities.Entities,
										  [entities.Bitmasks.ANIMATRONIC],
										  None,
										  entities.entities_mask)
