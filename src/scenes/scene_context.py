from src.scenes.intro import SceneIntro


class SceneContext:
    def __init__(
        self,
        display_surface
    ):
        self._state = SceneIntro()
        self._display_surface = display_surface
    
    def set_state(self, state):
        self._state = state

    def run_loop(self):
        self._state.events()
        self._state.updates()
        self._state.draws(self._display_surface)
