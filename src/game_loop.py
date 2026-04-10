import src.setup	  as setup
import src.ecs.entities	  as entities
import src.ecs.systems	  as systems
import src.ecs.components as components
import src.scenes	  as scenes


def game_loop():
	current_night = components.nights.Nights.FIRST
	scene_context = scenes.context.SceneContext(setup.DISPLAY_SURFACE)


	while True:

		delta_time: float = setup.CLOCK.tick(120)/1000
		current_time: int = setup.pygame.time.get_ticks()
		mouse_position: tuple[int, int] = setup.pygame.mouse.get_pos()
		update_position_without_camera: int = int(500*delta_time)
		update_position_with_camera: int = int(150*delta_time)

		scene_context.run_loop()

		setup.pygame.display.update()
