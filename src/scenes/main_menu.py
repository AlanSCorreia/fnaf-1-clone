import pygame

import src.ecs.systems as systems

from src.scenes.game_events import GameEvents


class SceneMainMenu:
    
    def events(
        self
    ) -> None:
        pass

    def updates(
        self
    ) -> None:
        pass

    def draws(
        self
    ) -> None:
        pass

    def state_transition(
        self,
        context,
        event: pygame.Event
    ) -> None:
    
        from src.scenes.loading import SceneLoading
        
        if event == GameEvents.OPTION_PRESSED:
            context.set_state(SceneLoading())

        elif event.type == pygame.KEYDOWN\
        and  event.key  == pygame.K_ESCAPE:
            systems.utils.exit_game(event)
            
