from src.components.game_states import GameEvents


class SceneNightWon:
    
    def events(self) -> None:
        pass

    def updates(self) -> None:
        pass

    def draws(self) -> None:
        pass

    def state_transition(self, context, event):
        from src.scenes.loading import SceneLoading

        if event == GameEvents.TIME_PASSED:
            context.set_state(SceneLoading())
