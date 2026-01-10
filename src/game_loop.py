# Todo:
#	Objetos como State e Frame tem várias redundancias que pode ser unificadas
#	Mudar o background das cameras com base na sala que eles estão
#	Adicionar tempo que demora cada hora da noite
#	Adicionar a mecânica de energia
#	Mudar o background do Office assim que a energia acabar


import sys

import pygame
from . import setup

from . import entities

from . import surfaces_imports
from . import components
from . import systems
from . import events


while True:

	delta_time: float = setup.clock.tick(120)/1000
	current_time: int = pygame.time.get_ticks()
	mouse_position: tuple[int, int] = pygame.mouse.get_pos()
	update_position_without_camera: int = int(500*delta_time)
	update_position_with_camera: int = int(150*delta_time)

	# Events

	
	#########################################################################
	# Updates 																#
	#########################################################################

	systems.camera.update_camera_direction(entities.flags.Flags.CAMERA_MOVEMENT,
									current_time,
									components.state.states,
									systems.state.update,
									_globals.camera_position_offset,
									_globals.position_offset_limit)
	
	systems.state.update_ingame(entities.flags.Flags.CAMERA,
								_globals,
								components.ingame_states.InGameStates,
								components.state.states)

	for state_id in entities.ids.states:

		systems.state.update_availability(state_id,
										  components.state.states,
										  current_time)

	for frame_id in entities.ids.frames:

		if components.frame.frames[frame_id].is_animation_playing:

			if systems.animation.check_frames_delay(frame_id,
										   			components.frame.frames,
													current_time):
				
				if components.frame.frames[frame_id].is_reversing:

					systems.animation.decrement_frame_index(frame_id,
													  components.frame.frames,
													  surfaces_imports.animated)
					
				else:

					systems.animation.increment_frame_index(frame_id,
													  components.frame.frames,
													  surfaces_imports.animated)

				surfaces = None

				if frame_id in entities.ids.static_surfaces:

					surfaces = components.surfaces.surfaces["static"]

				else:

					surfaces = components.surfaces.surfaces["animated"]

				systems.animation.update_frame(frame_id,
								   			   surfaces,
											   components.frame.frames,
											   surfaces_imports.animated,
											   current_time)
				
				systems.state.update_animation(frame_id,
								   			   components.frame.frames,
											   surfaces_imports.animated)

	match _globals.ingame_state:

		case components.ingame_states.InGameStates.WITHOUT_CAMERA:
			systems.camera.update_office_objects_position(update_position_without_camera,
												  		   mouse_position[0],
														   _globals.position_offset,
														   _globals.position_offset_limit)
			
			vertical_offset = _globals.position_offset["vertical"]

			for inanimate_id in entities.ids.inanimate_rectangles:
				components.rectangles.rectangles["inanimate"][inanimate_id].x += vertical_offset
	
			for animated_id in entities.ids.animated_rectangles:
				components.rectangles.rectangles["animated"][animated_id].x += vertical_offset
	
			components.rectangles.rectangles["backgrounds"][entities.flags.Flags.OFFICE].x += vertical_offset
	
			setup.display_surface.blit(components.surfaces.surfaces["backgrounds"][entities.flags.Flags.OFFICE],
									   components.rectangles.rectangles["backgrounds"][entities.flags.Flags.OFFICE])

			for animated_surf_id in entities.ids.animated_surfaces:
				setup.display_surface.blit(components.surfaces.surfaces["animated"][animated_surf_id],
											components.rectangles.rectangles["animated"][animated_surf_id])

			for inanimate_surf_id in entities.ids.inanimate_surfaces:
				setup.display_surface.blit(components.surfaces.surfaces["inanimate"][inanimate_surf_id],
											components.rectangles.rectangles["inanimate"][inanimate_surf_id])
		
		case components.ingame_states.InGameStates.WITH_CAMERA:
			systems.camera.update_background_position(entities.flags.Flags.CAMERA_MOVEMENT,
											 		  components.state.states,
													  update_position_with_camera,
											 		  _globals.camera_position_offset)
			
			if components.state.states[entities.flags.Flags.CAMERA_MOVEMENT].is_available:
				components.rectangles.rectangles["backgrounds"][_globals.camera_background].x += _globals.camera_position_offset["vertical"]

			setup.display_surface.blit(components.surfaces.surfaces["backgrounds"][_globals.camera_background],
									   components.rectangles.rectangles["backgrounds"][_globals.camera_background])
	
			for camera_id in entities.ids.cameras:
				setup.display_surface.blit(components.surfaces.surfaces["rooms_buttons"][camera_id],
										   components.rectangles.rectangles["rooms_buttons"][camera_id])
			
			setup.camera_static_ui.draw()

	for static_surf_id in entities.ids.static_surfaces:

		if systems.bitmask.has_component(entities.masks.components_masks[static_surf_id],
							   		 	 entities.bitmasks.Bitmasks.TRANSITION_FRAME):
			
			if components.frame.frames[static_surf_id].is_animation_playing:
				
				setup.display_surface.blit(components.surfaces.surfaces["static"][static_surf_id],
										   components.rectangles.rectangles["static"][static_surf_id])
	
	setup.static_ui.draw()

	systems.utils.debug(setup.debug_font,
					 	_globals.ingame_state,
					 	components.ingame_states.InGameStates,
						_globals,
					 	setup.display_surface,
						entities.flags.Flags,
						components.rectangles.rectangles,
						components.frame.frames,
						components.state.states)

	pygame.display.update()
