from typing import Callable


EVENTS: list[str] = [
	"mouse_hold",
	"mouse_release",
	"mouse_hover"
]


class EventEmitter:
	def __init__(self) -> None:
		self.listeners: dict[str, Callable] = dict()

	def add_event_listener(self, event, callback):
		if event not in self.listeners.keys():
			self.listeners[event] = callback
	
	def event_emitter(self, event, *data):
		if event in EVENTS:
		
			listener = self.listeners[event]
			listener(*data)
