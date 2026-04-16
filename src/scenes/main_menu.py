import pygame

import src.utils as utils

from src.scenes.game_events import GameEvents


class SceneMainMenu:
    _teste_surface: pygame.Surface = pygame.surface.Surface((200, 100))
    _teste_rect = _teste_surface.fill(pygame.Color("red"))

    def __init__(
        self,
        context
    ) -> None:
        
        self.context = context

    def events(
        self
    ) -> None:
        
        for event in pygame.event.get():
            utils.exit_game(event)

    def updates(
        self
    ) -> None:
        pass

    def draws(
        self,
        display_surface
    ) -> None:
        
        display_surface.blit(
            self._teste_surface,
            self._teste_rect
        )

    def state_transition(
        self,
        event: pygame.Event
    ) -> None:
    
        from src.scenes.loading import SceneLoading
        
        if event == GameEvents.OPTION_PRESSED:
            self.context.set_state(SceneLoading(self.context))

        elif event.type == pygame.KEYDOWN\
        and  event.key  == pygame.K_ESCAPE:
            utils.exit_game(event)
