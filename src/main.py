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


_globals = components._globals.Globals()

while True:

	delta_time = setup.clock.tick(120)/1000
	current_time = pygame.time.get_ticks()
	mouse_position = pygame.mouse.get_pos()
	update_position_without_camera = int(500*delta_time)
	update_position_with_camera = int(150*delta_time)

	# Events

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE:

				pygame.quit()
				sys.exit()
				
		if event.type == pygame.MOUSEMOTION:
			
			systems.camera.activate(entities.flags.Flags.CAMERA,
						   			event,
									current_time,
									setup.static_ui.camera_button_rect,
									components.frame.frames,
									components.state.states,
									systems.state.update)
			
			setup.static_ui.usage = systems.utils.define_energy_usage(entities.ids.energy_usage,
														   	  		  components.state.states)
			
		if event.type == pygame.MOUSEBUTTONDOWN:

			if event.button == 1\
			and components.state.states[entities.flags.Flags.MOUSE].is_available:
				
				match _globals.ingame_state:
					
					case components.ingame_states.InGameStates.WITHOUT_CAMERA:
						door_id 					  = None
						door_animatronic 			  = None
						panel_buttons_id 			  = None
						office_surface_id 			  = 0
						animatronic_final_destination = None
	
						if event.pos[0] < setup.window_width/2:
							door_id 					  = entities.flags.Flags.LEFT_DOOR
							door_animatronic 			  = entities.flags.Flags.BONNIE
							panel_buttons_id 			  = entities.ids.left_button_panel
							office_surface_id 			  = 1
							animatronic_final_destination = entities.flags.Flags.LEFT_DOOR

						else:
							door_id 					  = entities.flags.Flags.RIGHT_DOOR
							door_animatronic 			  = entities.flags.Flags.CHICA
							panel_buttons_id 			  = entities.ids.right_button_panel
							office_surface_id 			  = 2
							animatronic_final_destination = entities.flags.Flags.RIGHT_DOOR

						for button_id in panel_buttons_id[1:]:

							if systems.state.update_button(button_id,
														   components.rectangles.rectangles["inanimate"],
														   components.state.states,
														   current_time,
														   mouse_position):
			
								systems.office.update_button_panel_surface(entities.ids.left_button_panel,
												   						   entities.ids.right_button_panel,
												   						   components.state.states,
																		   components.surfaces.surfaces["inanimate"],
																		   surfaces_imports.inanimate)
			
								systems.office.update_surface(entities.flags.Flags.OFFICE,
									  						  door_animatronic,
															  panel_buttons_id[2],
															  office_surface_id,
															  components.state.states,
															  components.surfaces.surfaces["backgrounds"],
															  surfaces_imports.backgrounds,
															  components.current_room_index.current_room_index,
															  animatronic_final_destination)
			
								systems.state.update_door(door_id,
								  						  panel_buttons_id[1],
														  current_time,
														  systems.state.update,
														  components.state.states,
														  components.frame.frames)
			
								systems.office.deny_multiple_lights_on(entities.ids.left_button_panel,
																	   entities.ids.right_button_panel,
																	   components.state.states,
																	   systems.state.update,
																	   current_time,
																	   components.surfaces.surfaces["inanimate"],
																	   surfaces_imports.inanimate)

					case components.ingame_states.InGameStates.WITH_CAMERA:

						for button_id in entities.ids.rooms_buttons:

							if systems.state.update_button(button_id,
									  					   components.rectangles.rectangles["rooms_buttons"],
														   components.state.states,
														   current_time,
														   mouse_position):
			
								components.frame.frames[entities.flags.Flags.CAMERA_TRANSITION].is_animation_playing = True
								
								systems.camera.update_current_background_position_while_changing_background(button_id,
																components.rectangles.rectangles,
																_globals)
					
				setup.static_ui.usage = systems.utils.define_energy_usage(entities.ids.energy_usage,
														   	  			  components.state.states)

		if event.type == events.FREDDY_MOVEMENT_OPPORTUNITY:

			if systems.animatronic.movement_opportunity(entities.flags.Flags.FREDDY,
											   			components.nights.Nights.FIRST,
											   			components.difficult_levels.difficult_levels):
				
				# print("Freddy moved")
				pass

		if event.type == events.BONNIE_MOVEMENT_OPPORTUNITY:

			bonnie_id = entities.flags.Flags.BONNIE
			print(f"Bonnie is at: {components.current_room.current_room[bonnie_id]}")

			# se bonnie não estiver no escritorio:
			if components.current_room.current_room[bonnie_id] != entities.flags.Flags.OFFICE:
				
				# se bonnie suceder na oportunidade de movimento:
				if systems.animatronic.movement_opportunity(bonnie_id,
															components.nights.Nights.FIRST,
															components.difficult_levels.difficult_levels):
					
					print("Bonnie moved")
					
					# se bonnie estiver na última sala da sua rota(porta esquerda):
					if systems.animatronic.is_at_last_room(bonnie_id,
														components.routes.routes,
														components.current_room.current_room):

						# se a porta estiver aberta:
							# bonnie entra no escritorio
						# se não:
							# bonnie voltará para o west hall
						systems.animatronic.try_enter_office(bonnie_id,
															entities.flags.Flags.LEFT_DOOR,
															entities.flags.Flags.OFFICE,
															components.state.states,
															components.routes.routes,
															components.current_room_index.current_room_index,
															components.current_room.current_room)
					
					# se não:
					else:
						
						# bonnie avançará para a próxima sala
						systems.animatronic.route_progression(bonnie_id,
																components.routes.routes,
																components.current_room.current_room,
																components.current_room_index.current_room_index)

						# atualizar o background da sala que bonnie está
			
			# se não:
			else:
				
				# se o player ativar a câmera:
					# se o player ficar mais de 30 segundos com a câmera ativada
					# ou se o player desativar a câmera:
						# desativar a câmera
						# executar jumpscare
						# mudar estado ingame para game_over
				# se não:
					# office stalling(não pode atacar o player)
				pass

		if event.type == events.CHICA_MOVEMENT_OPPORTUNITY:

			if systems.animatronic.movement_opportunity(entities.flags.Flags.CHICA,
											   			components.nights.Nights.FIRST,
											   			components.difficult_levels.difficult_levels):
				
				# print("Chica moved")
				pass

		if event.type == events.FOXY_MOVEMENT_OPPORTUNITY:

			if systems.animatronic.movement_opportunity(entities.flags.Flags.FOXY,
											   			components.nights.Nights.FIRST,
											   			components.difficult_levels.difficult_levels):
				
				# print("Foxy moved")
				pass

	#########################################################################
	# Updates 																#
	#########################################################################

	systems.camera.update_direction(entities.flags.Flags.CAMERA_MOVEMENT,
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

					systems.animation.decrement_frame(frame_id,
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
			systems.camera.update_dinamic_objects_position(update_position_without_camera,
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

		if systems.bitmask.has_component(entities.masks.entities_masks[static_surf_id],
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
