import src.systems.utils
import pygame
from src.scenes.main_menu import SceneMainMenu
from src.components.game_states import GameEvents


class SceneIntro:
    _teste_surface: pygame.Surface = pygame.surface.Surface((100, 100))
    _teste_rect = _teste_surface.fill(pygame.Color("green"))
    
    def events(self) -> None:
        for event in pygame.event.get():
            src.systems.utils.exit_game(event)

    def updates(self) -> None:
        pass

    def draws(self, display_surface: pygame.Surface) -> None:
        display_surface.blit(
            self._teste_surface,
            self._teste_rect
        )

    def state_transition(self, context, event):
        if event == GameEvents.TIME_PASSED:
            context.set_state(SceneMainMenu())
