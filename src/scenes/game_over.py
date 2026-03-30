from src.scenes.main_menu import SceneMainMenu
from src.ecs.components.game_events import GameEvents


class SceneGameOver:
    
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

        if event == GameEvents.TIME_PASSED:
            context.set_state(SceneMainMenu())
