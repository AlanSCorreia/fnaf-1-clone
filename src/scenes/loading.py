from src.scenes.gameplay import SceneGameplay
from src.components.game_states import GameEvents


class SceneLoading:
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(self, context, event):
        if event == GameEvents.TIME_PASSED:
            context.set_state(SceneGameplay())
