from src.scenes.main_menu import SceneMainMenu
from src.components.game_states import GameEvents


class SceneCustomNightMenu:
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(self, context, event):
        from src.scenes.loading import SceneLoading
        
        if event == GameEvents.OPTION_PRESSED:
            context.set_state(SceneLoading())

        elif event == GameEvents.ESCAPE_PRESSED:
            context.set_state(SceneMainMenu())
