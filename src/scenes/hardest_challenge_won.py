from src.scenes.main_menu import SceneMainMenu
from src.components.game_states import GameEvents


class SceneHardestChallengeWon:
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(self, context, event):
        if event == GameEvents.TIME_PASSED:
            context.set_state(SceneMainMenu())
