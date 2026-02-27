import src.setup as setup
import src.entities as entities
import src.components as components
import src.systems as systems


def updates(delta_time,
			current_time,
			mouse_position,
			game_state,
			update_position_with_camera,
			update_position_without_camera) -> None:

	systems.camera.set_direction(
		entities.IDS["CAMERA_MOVEMENT"],
		current_time,
		components.states.STATES,
		setup.POSITIONS_OFFSET["CAMERA"],
		setup.POSITIONS_OFFSET_OFFICE_LIMITS
	)
	
	# systems.states.update_ingame(entities.flags.Flags.CAMERA,
	# 							components.ingame_states.InGameStates,
	# 							components.state.states)

	for state_name in entities.IDS_FILTERED["STATES"]:

		systems.states.update_availability(
			entities.IDS[state_name],
			components.states.STATES,
			current_time
		)

	for frame_name in entities.IDS_FILTERED["ANIMATED_PROPS"]:

		if components.frames.FRAMES[entities.IDS[frame_name]].is_animation_playing:

			if systems.animations.check_frames_delay(
				entities.IDS[frame_name],
				components.frames.FRAMES,
				current_time
			):
				
				if components.frames.FRAMES[entities.IDS[frame_name]].is_reversing:

					systems.animations.decrement_frame_index(
						entities.IDS[frame_name],
						components.frames.FRAMES,
						components.setup_surfaces.ALL_ANIMATED_PROPS
					)
					
				else:

					systems.animations.increment_frame_index(
						entities.IDS[frame_name],
						components.frames.FRAMES,
						components.setup_surfaces.ALL_ANIMATED_PROPS
					)

				systems.animations.update_frame(
					entities.IDS[frame_name],
					components.frames.FRAMES,
					"normal",
					components.surfaces.CURRENT_ANIMATED_PROPS,
					components.setup_surfaces.ALL_ANIMATED_PROPS,
					current_time
				)
				
				systems.animations.update(
					entities.IDS[frame_name],
					components.frames.FRAMES,
					components.setup_surfaces.ALL_ANIMATED_PROPS
				)

	if components.states.STATES[entities.IDS["CAMERA"]].state\
	and components.states.STATES[entities.IDS["CAMERA"]].is_available:

		systems.camera.update_background_movement(
			entities.IDS["CAMERA_MOVEMENT"],
			components.states.STATES,
			update_position_with_camera,
			setup.POSITIONS_OFFSET["CAMERA"]
		)
		
		if components.states.STATES[entities.IDS["CAMERA_MOVEMENT"]].is_available:
			components.rectangles.BACKGROUNDS[components.rectangles.CURRENT_ROOM_ON_CAMERA].x += setup.POSITIONS_OFFSET["CAMERA"]["vertical"]

		setup.DISPLAY_SURFACE.blit(
			components.surfaces.CURRENT_BACKGROUNDS[components.rectangles.CURRENT_ROOM_ON_CAMERA],
			components.rectangles.BACKGROUNDS[entities.IDS["CAMERA"]]
		)

		for camera_name in entities.IDS_FILTERED["CAMERA"]:
			setup.DISPLAY_SURFACE.blit(
				components.surfaces.CURRENT_CAMERA_BUTTONS[camera_name],
				components.rectangles.CAMERA_BUTTONS[camera_name]
			)
	
	else:

		systems.office.update_object_positions(
			update_position_without_camera,
			mouse_position[0],
			setup.POSITIONS_OFFSET["OFFICE"],
			setup.POSITIONS_OFFSET_OFFICE_LIMITS
		)

		for inanimate_name in entities.IDS_FILTERED["INANIMATED_PROPS"]:
			components.rectangles.INANIMATED_PROPS[entities.IDS[inanimate_name]].x += setup.POSITIONS_OFFSET["OFFICE"]["vertical"]

		for animated_name in entities.IDS_FILTERED["ANIMATED_PROPS"]:
			components.rectangles.ANIMATED_PROPS[entities.IDS[animated_name]]["normal"].x += setup.POSITIONS_OFFSET["OFFICE"]["vertical"]

		components.rectangles.BACKGROUNDS[entities.IDS["OFFICE"]].x += setup.POSITIONS_OFFSET["OFFICE"]["vertical"]

		setup.DISPLAY_SURFACE.blit(
			components.surfaces.CURRENT_BACKGROUNDS[entities.IDS["OFFICE"]],
			components.rectangles.BACKGROUNDS[entities.IDS["OFFICE"]]
		)

		for animated_surf_name in entities.IDS_FILTERED["ANIMATED_PROPS"]:
			setup.DISPLAY_SURFACE.blit(components.surfaces.CURRENT_ANIMATED_PROPS[entities.IDS[animated_surf_name]]["normal"],
									   components.rectangles.ANIMATED_PROPS[entities.IDS[animated_surf_name]]["normal"])

		for inanimate_surf_name in entities.IDS_FILTERED["INANIMATED_PROPS"]:
			setup.DISPLAY_SURFACE.blit(components.surfaces.CURRENT_INANIMATED_PROPS[entities.IDS[inanimate_surf_name]],
									   components.rectangles.INANIMATED_PROPS[entities.IDS[inanimate_surf_name]])
