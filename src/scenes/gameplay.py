import pygame

from src.scenes.game_over import SceneGameOver
from src.scenes.night_won import SceneNightWon
from src.scenes.main_menu import SceneMainMenu
from src.scenes.game_events import GameEvents

from src.userInterface.implementation import GROUPS


class SceneGameplay:
    
    def events(
        self
    ) -> None:
        pass

    def updates(
        self
    ) -> None:
        pass

    def draws(
        self,
        display_surface
    ) -> None:
        
        GROUPS["off_camera"].draw(display_surface)

    def state_transition(
        self,
        context,
        event: pygame.Event
    ) -> None:
    
        if event == GameEvents.DIED:
            context.set_state(SceneGameOver())

        elif event == GameEvents.SURVIVED:
            context.set_state(SceneNightWon())
        
        elif event.type == pygame.KEYDOWN\
        and  event.key  == pygame.K_ESCAPE:
            context.set_state(SceneMainMenu())
