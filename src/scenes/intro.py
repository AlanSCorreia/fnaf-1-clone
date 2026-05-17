import pygame

from src.userInterface.setup import UI_GROUPS, ELEMENTS_TYPE

import src.utils as utils
from src.events.game_events import GameEvents
from src.scenes.main_menu import SceneMainMenu


class SceneIntro:
    _teste_surface: pygame.Surface = pygame.surface.Surface((100, 100))
    _teste_rect = _teste_surface.fill(pygame.Color("green"))

    def __init__(
        self,
        context
    ) -> None:

        self.context = context
        self.timer = utils.set_timer(3000)
        
    def events(
        self
    ) -> None:

        for event in pygame.event.get():
            utils.exit_game(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                ELEMENTS_TYPE["text"]["epilepsy_warning"].fade_in()
                print(ELEMENTS_TYPE["text"]["epilepsy_warning"].image.get_alpha())

            # if event.type == self.timer:
            #     self.state_transition(GameEvents.TIME_PASSED)

    def updates(
        self
    ) -> None:

        UI_GROUPS["intro"].update()

    def draws(
        self,
        display_surface: pygame.Surface
    ) -> None:

        # display_surface.blit(
        #     self._teste_surface,
        #     self._teste_rect
        # )
        display_surface.fill("black")
        UI_GROUPS["intro"].draw(display_surface)

    def state_transition(
        self,
        event
    ) -> None:

        if event == GameEvents.TIME_PASSED:
            self.context.set_state(SceneMainMenu(self.context))
