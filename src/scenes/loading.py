from src.scenes.gameplay import SceneGameplay
from src.scenes.game_events import GameEvents


class SceneLoading:
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
            self.context.set_state(SceneGameplay(self.context))
