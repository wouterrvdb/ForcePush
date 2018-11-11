import uuid
import numpy as np

class Entity(object):
    def __init__(self):
        # TODO: Generate UUID
        self.id = uuid.uuid4()

        self.pos = np.array([0, 0])

    def tick(self):
        pass