from src.scenes.main_menu import SceneMainMenu
from src.scenes.game_events import GameEvents


class SceneHardestChallengeWon:
    def __init__(
        self,
        context
    ) -> None:

        self.context = context
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(
        self,
        event
    ) -> None:

        if event == GameEvents.TIME_PASSED:
            self.context.set_state(SceneMainMenu(self.context))
