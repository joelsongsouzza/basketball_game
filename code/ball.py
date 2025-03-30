from abc import ABC

from code.entity import Entity


class Ball(Entity, ABC):
    def __init__(self, name: str, position: tuple, x_speed, y_speed, ):
        super().__init__(name, position)
        self.name = name
        self.position = position
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        self.y_speed += 0.3
