from abc import ABC

from code.entity import Entity


class Player(Entity, ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direction = 1
        self.speed = 1
        self.max_movement = 150
        self.start_y = position[1]

    def shoot(self):
        pass

    def move(self):
        movement = self.speed * self.direction
        print(f'{self.speed} * {self.direction} = {movement}')
        self.rect.centery += movement
        if abs(self.rect.centery - self.start_y) >= self.max_movement:
            self.direction *= -1