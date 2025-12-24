from .game_states import GameStates
from .ingame_states import InGameStates
from .nights import Nights
from ..entities import flags


class Globals:
	def __init__(self) -> None:
		self.game_state 	   = GameStates.IN_GAME
		self.ingame_state 	   = InGameStates.WITHOUT_CAMERA
		self.camera_background = flags.Flags.SHOW_STAGE
		self.current_night 	   = Nights.FIRST
		
		self.position_offset_limit = {
			"min": -320,
			"max": 10
		}

		self.position_offset = {
			"vertical": 0,
			"base": 0
		}

		self.camera_position_offset = {
			"vertical": 0,
			"base": 0
		}
