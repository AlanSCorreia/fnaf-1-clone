from typing import Callable
from enum import Enum


class Events(Enum):
	MOUSE_HOLD = 0,
	MOUSE_RELEASE = 1,
	MOUSE_HOVER = 2


class EventEmitter:
	def __init__(self) -> None:
		self.listeners: dict[Events, Callable] = dict()

	def add_event_listener(self, event, callback):
		if event not in self.listeners.keys():
			self.listeners[event] = callback
	
	def event_emitter(self, event, *data):
		if event in Events:
		
			listener = self.listeners[event]
			listener(*data)
