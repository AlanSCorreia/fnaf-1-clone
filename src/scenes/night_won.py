from src.ecs.components.game_events import GameEvents


class SceneNightWon:
    
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

        from src.scenes.loading import SceneLoading

        if event == GameEvents.TIME_PASSED:
            context.set_state(SceneLoading())
