from abc import ABC

from code.const import WIN_HEIGHT, GRAVITY
from code.entity import Entity


class Ball(Entity, ABC):
    def __init__(self, name: str, position: tuple, x_speed, y_speed, ):
        super().__init__(name, position)
        self.name = name
        self.position = position
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.retention = 100
        self.is_shooting = False

    def shoot(self):
        self.is_shooting = True

    def move(self):
        if self.is_shooting:
            self.rect.centerx += self.x_speed
            self.rect.centery += self.y_speed
            self.y_speed += 0.3

            if self.rect.y >= 800:
                self.is_shooting = False
                self.rect.centery = 300
                self.y_speed = 0
