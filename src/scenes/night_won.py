from src.scenes.game_events import GameEvents


class SceneNightWon:
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

        from src.scenes.loading import SceneLoading

        if event == GameEvents.TIME_PASSED:
            self.context.set_state(SceneLoading(self.context))
