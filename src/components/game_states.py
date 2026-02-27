from enum import IntFlag, auto


class GameStates(IntFlag):
	
	INTRO 			  = auto()
	MAIN_MENU    	  = auto()
	MENU_CUSTOM_NIGHT = auto()
	LOADING 		  = auto()
	IN_GAME		  	  = auto()
	WIN_SCREEN 		  = auto()
	GAME_OVER		  = auto()
	EXIT			  = auto()


class GameEvents(IntFlag):

	TIME_PASSED   		 = auto()
	START_PRESSED 		 = auto()
	CUSTOM_NIGHT_PRESSED = auto()
	ESCAPE_PRESSED 		 = auto()
	SURVIVED			 = auto()
	DIED				 = auto()


GAME_STATE_TRANSITIONS: dict[GameStates, dict[GameEvents, GameStates]] = {
	GameStates.INTRO: {
		GameEvents.TIME_PASSED: GameStates.MAIN_MENU
	},

	GameStates.IN_GAME: {
		GameEvents.DIED			 : GameStates.GAME_OVER,
		GameEvents.SURVIVED		 : GameStates.WIN_SCREEN,
		GameEvents.ESCAPE_PRESSED: GameStates.MAIN_MENU
	},

	GameStates.MAIN_MENU: {
		GameEvents.START_PRESSED	   : GameStates.LOADING,
		GameEvents.ESCAPE_PRESSED	   : GameStates.EXIT,
		GameEvents.CUSTOM_NIGHT_PRESSED: GameStates.MENU_CUSTOM_NIGHT
	},

	GameStates.GAME_OVER: {
		GameEvents.TIME_PASSED: GameStates.MAIN_MENU
	},

	GameStates.WIN_SCREEN: {
		GameEvents.TIME_PASSED: GameStates.MAIN_MENU
	},

	GameStates.MENU_CUSTOM_NIGHT: {
		GameEvents.START_PRESSED : GameStates.LOADING,
		GameEvents.ESCAPE_PRESSED: GameStates.MAIN_MENU
	}
}
