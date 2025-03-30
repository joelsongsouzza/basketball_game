from abc import ABC

import pygame

from code.ball import Ball
from code.entity import Entity


class Player(Entity, ABC):
    def __init__(self, name: str, position: tuple, ball: Ball):
        super().__init__(name, position)
        self.direction = 1
        self.speed = 1
        self.max_movement = 150
        self.start_y = position[1]
        self.ball = ball

    @staticmethod
    def shoot(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.K_x:
                    pass
        # self.ball.shoot()

    def move(self):
        movement = self.speed * self.direction
        self.rect.centery += movement
        if abs(self.rect.centery - self.start_y) >= self.max_movement:
            self.direction *= -1