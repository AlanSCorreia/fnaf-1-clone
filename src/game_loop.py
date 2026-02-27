# Todo:
#	Objetos como State e Frame tem várias redundancias que pode ser unificadas
#	Mudar o background das cameras com base na sala que eles estão
#	Adicionar tempo que demora cada hora da noite
#	Adicionar a mecânica de energia
#	Mudar o background do Office assim que a energia acabar
import src.setup				  as setup
import src.entities				  as entities
import src.systems				  as systems
import src.components			  as components

import src.events				  as events
import src.updates 				  as updates
import src.ui					  as ui


GAME_STATE	 : components.game_states.GameStates = components.game_states.GameStates.IN_GAME
CURRENT_NIGHT: components.nights.Nights 	  	  = components.nights.Nights.FIRST


while True:

	DELTA_TIME: float = setup.CLOCK.tick(120)/1000
	CURRENT_TIME: int = setup.pygame.time.get_ticks()
	MOUSE_POSITION: tuple[int, int] = setup.pygame.mouse.get_pos()
	UPDATE_POSITION_WITHOUT_CAMERA: int = int(500*DELTA_TIME)
	UPDATE_POSITION_WITH_CAMERA: int = int(150*DELTA_TIME)

	#########################################################################
	# Events																#
	#########################################################################
	events.game_intro()

	#########################################################################
	# Updates 																#
	#########################################################################
	updates.updates(
		DELTA_TIME,
		CURRENT_TIME,
		MOUSE_POSITION,
		GAME_STATE,
		UPDATE_POSITION_WITH_CAMERA,
		UPDATE_POSITION_WITHOUT_CAMERA
	)

	ui.elements_off_camera_group.draw(
		setup.DISPLAY_SURFACE
	)

	setup.pygame.display.update()
