import uuid


class Entity(object):
    def __init__(self):
        # TODO: Generate UUID
        self.id = uuid.uuid4()

    def tick(self):
        pass