# Todo:
#	Adicionar os animatronicos em salas
#	Permitir que os animatronicos troquem de sala
#	Adicionar uma rota para cada animatronico seguir
#	Mudar o background das cameras com base na sala que eles estão
#	Permitir que apenas um botão de luz seja ligado por vez
#	Adicionar as noites
#	Aumentar a dificuldade dos animatronicos em certa hora da noite
#	Adicionar tempo que demora cada hora da noite
#	Adicionar a mecânica de energia
#	Calcular a quantidade de energia em uso para mostrar na UI "Usage: "
#	Mudar o background do Office assim que a energia acabar
#	
# Propostas:

import sys

import pygame
import setup

import entities
import ids
import surfaces_imports
import components
import systems


_globals = components._Globals()

while True:

	delta_time = setup.clock.tick(120)/1000
	current_time = pygame.time.get_ticks()
	mouse_position = pygame.mouse.get_pos()
	update_position_without_camera = int(500*delta_time)
	update_position_with_camera = int(150*delta_time)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
				
		if event.type == pygame.MOUSEMOTION:
			systems.camera.activate(entities.Entities.CAMERA,
						   			event,
									current_time,
									setup.static_ui.camera_button_rect,
									components.frames,
									components.states,
									systems.state.update)
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1\
			and components.states[entities.Entities.MOUSE].is_available:
				# print(pygame.mouse.get_pos())
				match _globals.ingame_state:
					case components.InGameStates.WITHOUT_CAMERA:
						panel_buttons_id = None
						door_id = None
						office_surface_id = 0
						door_animatronic = None
						animatronic_final_destination = None
	
						if event.pos[0] < setup.window_width/2:
							panel_buttons_id = ids.left_button_panel
							door_id = entities.Entities.LEFT_DOOR
							office_surface_id = 1
							door_animatronic = entities.Entities.BONNIE
							animatronic_final_destination = entities.Entities.LEFT_DOOR
						else:
							panel_buttons_id = ids.right_button_panel
							door_id = entities.Entities.RIGHT_DOOR
							office_surface_id = 2
							door_animatronic = entities.Entities.CHICA
							animatronic_final_destination = entities.Entities.RIGHT_DOOR

						for button_id in panel_buttons_id[1:]:
							if systems.state.update_button(button_id,
														   components.rectangles["inanimate"],
														   components.states,
														   current_time,
														   mouse_position):
			
								systems.office.update_button_panel_surface(panel_buttons_id,
												   						   components.states,
																		   components.surfaces["inanimate"],
																		   surfaces_imports.inanimate)
			
								systems.office.update_surface(entities.Entities.OFFICE,
									  						  door_animatronic,
															  panel_buttons_id[2],
															  office_surface_id,
															  components.states,
															  components.surfaces["backgrounds"],
															  surfaces_imports.backgrounds,
															  components.current_room,
															  animatronic_final_destination)
			
								systems.state.update_door(door_id,
								  						  panel_buttons_id[1],
														  current_time,
														  systems.state.update,
														  components.states,
														  components.frames)
			
								systems.office.deny_multiple_lights_on(entities.Entities.LEFT_LIGHT_BUTTON,
																	   entities.Entities.RIGHT_LIGHT_BUTTON,
																	   panel_buttons_id,
																	   components.states,
																	   systems.state.update,
																	   current_time,
																	   components.surfaces["inanimate"],
																	   surfaces_imports.inanimate)

					case components.InGameStates.WITH_CAMERA:
						for button_id in ids.rooms_buttons:
							if systems.state.update_button(button_id,
									  					   components.rectangles["rooms_buttons"],
														   components.states,
														   current_time,
														   mouse_position):
			
								components.frames[entities.Entities.CAMERA_TRANSITION].is_animation_playing = True
								
								systems.camera.update_background(button_id,
																components.rectangles,
																_globals)
	
	systems.camera.update_direction(entities.Entities.CAMERA_MOVEMENT,
									current_time,
									components.states,
									systems.state.update,
									_globals.camera_position_offset,
									_globals.position_offset_limit)
	
	systems.state.update_ingame(entities.Entities.CAMERA,
								_globals,
								components.InGameStates,
								components.states)

	for state_id in ids.states:
		systems.state.update_availability(state_id,
										  components.states,
										  current_time)

	for frame_id in ids.frames:
		if components.frames[frame_id].is_animation_playing:

			if systems.animation.check_frames_delay(frame_id,
										   			components.frames,
													current_time):
				
				if components.frames[frame_id].is_reversing:
					systems.animation.decrement_frame(frame_id,
													  components.frames,
													  surfaces_imports.animated)
				else:
					systems.animation.increment_frame(frame_id,
													  components.frames,
													  surfaces_imports.animated)

				surfaces = None

				if frame_id in ids.static_surfaces:
					surfaces = components.surfaces["static"]
				else:
					surfaces = components.surfaces["animated"]

				systems.animation.update_frame(frame_id,
								   			   surfaces,
											   components.frames,
											   surfaces_imports.animated,
											   current_time)
				
				systems.state.update_animation(frame_id,
								   			   components.frames,
											   surfaces_imports.animated)

	match _globals.ingame_state:
		case components.InGameStates.WITHOUT_CAMERA:
			systems.camera.update_dinamic_objects_position(update_position_without_camera,
												  		   mouse_position[0],
														   _globals.position_offset,
														   _globals.position_offset_limit)
			
			vertical_offset = _globals.position_offset["vertical"]

			for inanimate_id in ids.inanimate_rectangles:
				components.rectangles["inanimate"][inanimate_id].x += vertical_offset
	
			for animated_id in ids.animated_rectangles:
				components.rectangles["animated"][animated_id].x += vertical_offset
	
			components.rectangles["backgrounds"][entities.Entities.OFFICE].x += vertical_offset
	
			setup.display_surface.blit(components.surfaces["backgrounds"][entities.Entities.OFFICE],
									   components.rectangles["backgrounds"][entities.Entities.OFFICE])

			for animated_surf_id in ids.animated_surfaces:
				setup.display_surface.blit(components.surfaces["animated"][animated_surf_id],
											components.rectangles["animated"][animated_surf_id])

			for inanimate_surf_id in ids.inanimate_surfaces:
				setup.display_surface.blit(components.surfaces["inanimate"][inanimate_surf_id],
											components.rectangles["inanimate"][inanimate_surf_id])
		
		case components.InGameStates.WITH_CAMERA:
			systems.camera.update_background_position(entities.Entities.CAMERA_MOVEMENT,
											 		  components.states,
													  update_position_with_camera,
											 		  _globals.camera_position_offset)
			
			if components.states[entities.Entities.CAMERA_MOVEMENT].is_available:
				components.rectangles["backgrounds"][_globals.camera_background].x += _globals.camera_position_offset["vertical"]

			setup.display_surface.blit(components.surfaces["backgrounds"][_globals.camera_background],
									   components.rectangles["backgrounds"][_globals.camera_background])
	
			for camera_id in ids.camera:
				setup.display_surface.blit(components.surfaces["rooms_buttons"][camera_id],
										   components.rectangles["rooms_buttons"][camera_id])
			
			setup.camera_static_ui.draw()

	for static_surf_id in ids.static_surfaces:
		if systems.bitmask.has_component(entities.entities_mask[static_surf_id],
							   		 	 entities.Bitmasks.TRANSITION_FRAME):
			if components.frames[static_surf_id].is_animation_playing:
				setup.display_surface.blit(components.surfaces["static"][static_surf_id],
										   components.rectangles["static"][static_surf_id])
	
	setup.static_ui.usage = 1 # Nivel de consumo de energia
	setup.static_ui.draw()

	systems.utils.debug(setup.debug_font,
					 	_globals.ingame_state,
					 	components.InGameStates,
						_globals,
					 	setup.display_surface,
						entities.Entities,
						components.rectangles,
						components.frames,
						components.states)

	pygame.display.update()
