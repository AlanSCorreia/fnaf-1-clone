import pygame

from src.scenes.main_menu import SceneMainMenu
from src.scenes.game_events import GameEvents


class SceneCustomNightMenu:
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(
        self,
        context,
        event
    ) -> None:

        from src.scenes.loading import SceneLoading
        
        if event == GameEvents.OPTION_PRESSED:
            context.set_state(SceneLoading())

        elif event.type == pygame.KEYDOWN\
        and  event.key  == pygame.K_ESCAPE:
            context.set_state(SceneMainMenu())
