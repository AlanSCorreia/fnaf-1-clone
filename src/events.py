import sys

import pygame

import entities


def event_call(event, code) -> None:

	code()


def exit_game() -> None:
	
    pygame.quit()
    sys.exit()


def toggle_camera_state() -> None:
    if rectangle.collidepoint(event.pos):
		systems.camera.activate(entities.flags.Flags.CAMERA,
						 		event,
								current_time,
								setup.static_ui.camera_button_rect,
								components.frame.frames,
								components.state.states,
								systems.state.update)
			
	setup.static_ui.usage = systems.utils.define_energy_usage(entities.ids.energy_usage,
														   	  		  components.state.states)



FREDDY_MOVEMENT_OPPORTUNITY = pygame.event.custom_type()
BONNIE_MOVEMENT_OPPORTUNITY = pygame.event.custom_type()
CHICA_MOVEMENT_OPPORTUNITY  = pygame.event.custom_type()
FOXY_MOVEMENT_OPPORTUNITY   = pygame.event.custom_type()

pygame.time.set_timer(FREDDY_MOVEMENT_OPPORTUNITY, delay[entities.flags.Flags.FREDDY])
pygame.time.set_timer(BONNIE_MOVEMENT_OPPORTUNITY, delay[entities.flags.Flags.BONNIE])
pygame.time.set_timer(CHICA_MOVEMENT_OPPORTUNITY,  delay[entities.flags.Flags.CHICA ])
pygame.time.set_timer(FOXY_MOVEMENT_OPPORTUNITY,   delay[entities.flags.Flags.FOXY  ])


def event_loop():

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			exit_game()
		
		if event.type == pygame.KEYDOWN\
		and event.key == pygame.K_ESCAPE:

			exit_game()
				
		if event.type == pygame.MOUSEMOTION:
			
			if rectangle.collidepoint(event.pos):
				
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
