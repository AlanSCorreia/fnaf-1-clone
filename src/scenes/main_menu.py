from src.components.game_states import GameEvents


class SceneMainMenu:
    
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
            pass
            # game_exit()
