import pygame

from forcepush.inputs.handler.handler import Handler


class InputManager(object):
    def __init__(self):
        self.handlers = {
            "event": {},
            "key": {},
            "mouse": {}
        }
        self._register_handlers()

    def handle_pygame(self):
        for event in pygame.event.get():
            if event.type in self.handlers['event']:
                for handler in self.handlers['event'][event.type]:
                    handler.handle(event)

        for key_type, handlers in self.handlers['key'].items():
            if pygame.key.get_pressed()[key_type]:
                for handler in handlers:
                    handler.handle(key_type)

        # TODO: Add pygame.mouse stuff

    def _register_handlers(self):
        pass

    def register_handler(self, handler: Handler):
        for handler_type, event_type, subhandler in handler.get_event_types():
            if event_type not in self.handlers[handler_type]:
                self.handlers[handler_type][event_type] = []
            self.handlers[handler_type][event_type].append(subhandler)

    def deregister_handler(self, handler: Handler):
        # TODO: Remove handler from self.handlers using get_event_types
        pass
