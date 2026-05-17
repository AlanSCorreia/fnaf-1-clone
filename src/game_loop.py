import src.setup  as setup
import src.scenes as scenes
import src.utils  as utils


def game_loop():
	scene_context = scenes.context.SceneContext(setup.DISPLAY_SURFACE)

	while True:
		update_position_without_camera: int = int(500*utils.get_delta_time(60))
		update_position_with_camera: int = int(150*utils.get_delta_time(60))
		scene_context.run_loop()

		setup.pygame.display.update()
