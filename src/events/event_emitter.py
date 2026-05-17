import pygame

from typing import Callable
from enum import Enum


class GUIEvents(Enum):
	MOUSE_HOLD	   = pygame.event.custom_type(),
	MOUSE_RELEASE  = pygame.event.custom_type(),
	MOUSE_HOVER    = pygame.event.custom_type(),
	START_FADE_IN  = pygame.event.custom_type(),
	START_FADE_OUT = pygame.event.custom_type(),
	END_FADE_IN	   = pygame.event.custom_type(),
	END_FADE_OUT   = pygame.event.custom_type(),


class GUIEventEmitter:
	def __init__(self) -> None:
		self.listeners: dict[GUIEvents, Callable] = dict()

	def add_event_listener(self, event, callback):
		if event not in self.listeners.keys():
			self.listeners[event] = dict()
		
		self.listeners[event].update(callback)
	
	def event_emitter(self, event, *data):
		if event in GUIEvents:
		
			listener = self.listeners[event]
			listener(*data)
