import pygame

from forcepush.inputs.handler.Handler import Handler


class InputManager(object):
    def __init__(self):
        self.handlers = {}
        self._register_handlers()

    def handle_pygame(self):
        for event in pygame.event.get():
            print(event)
            if event.type in self.handlers:
                for handler in self.handlers[event.type]:
                    handler.handle(event)

    def _register_handlers(self):
        pass

    def register_handler(self, handler: Handler):
        for event_type, sub_handler in handler.get_event_types():
            if event_type not in self.handlers:
                self.handlers[event_type] = []
            print(event_type, sub_handler)
            self.handlers[event_type].append(sub_handler)
