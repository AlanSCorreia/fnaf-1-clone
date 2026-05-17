from enum import Enum
import pygame


class GameEvents(Enum):

	TIME_PASSED   		  = pygame.event.custom_type()
	OPTION_SELECTED 	  = pygame.event.custom_type()
	CUSTOM_NIGHT_SELECTED = pygame.event.custom_type()
	SURVIVED			  = pygame.event.custom_type()
	DIED				  = pygame.event.custom_type()
