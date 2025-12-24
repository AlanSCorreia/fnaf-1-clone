from enum import Enum, auto


class InGameStates(Enum):
	WITHOUT_CAMERA = auto()
	WITH_CAMERA	   = auto()
	GAME_OVER	   = auto()
