import pygame

from src.scenes.main_menu import SceneMainMenu
from src.scenes.game_events import GameEvents


class SceneCustomNightMenu:
    def __init__(
        self,
        context
    ) -> None:
    
        self.context = context
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(
        self,
        display_surface: pygame.Surface
    ) -> None:
        pass

    def state_transition(
        self,
        event
    ) -> None:

        from src.scenes.loading import SceneLoading
        
        if event == GameEvents.OPTION_PRESSED:
            self.context.set_state(SceneLoading(self.context))

        elif event.type == pygame.KEYDOWN\
        and  event.key  == pygame.K_ESCAPE:
            self.context.set_state(SceneMainMenu(self.context))
