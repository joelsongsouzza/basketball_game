from abc import ABC

from code.entity import Entity


class TrashBin(Entity, ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.position = position

    def move(self):
        pass
