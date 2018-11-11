import numpy as np

from forcepush.logic.entity.entity import Entity

class Viewport(object):
    def __init__(self, width : int, height : int):
        self.width = width
        self.height = height

        self.offset = np.array([0, 0])

        self.focus_entity = None
        self._entity_offset = np.array([self.width / 2, self.height / 2])

    def set_focus(self, entity: Entity):
        self.focus_entity = entity
        self.update()

    def update(self):
        if self.focus_entity:
            self.offset = self._entity_offset - self.focus_entity.pos
