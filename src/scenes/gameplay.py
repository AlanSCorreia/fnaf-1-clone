from src.scenes.game_over import SceneGameOver
from src.scenes.night_won import SceneNightWon
from src.scenes.main_menu import SceneMainMenu
from src.components.game_states import GameEvents


class SceneGameplay:
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(self, context, event):
        if event == GameEvents.DIED:
            context.set_state(SceneGameOver())

        elif event == GameEvents.SURVIVED:
            context.set_state(SceneNightWon())
        
        elif event == GameEvents.ESCAPE_PRESSED:
            context.set_state(SceneMainMenu())
