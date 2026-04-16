import pygame

from src.scenes.game_over import SceneGameOver
from src.scenes.night_won import SceneNightWon
from src.scenes.main_menu import SceneMainMenu
from src.scenes.game_events import GameEvents

from src.userInterface.implementation import GROUPS


class SceneGameplay:
    def __init__(
        self,
        context
    ) -> None:

        self.context = context
    
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
        event: pygame.Event
    ) -> None:
    
        if event == GameEvents.DIED:
            self.context.set_state(SceneGameOver(self.context))

        elif event == GameEvents.SURVIVED:
            self.context.set_state(SceneNightWon(self.context))
        
        elif event.type == pygame.KEYDOWN\
        and  event.key  == pygame.K_ESCAPE:
            self.context.set_state(SceneMainMenu(self.context))
