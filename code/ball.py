from abc import ABC

import pygame

from code.entity import Entity


class Ball(Entity, ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.position = position
        self.x_speed = 5
        self.y_speed = -10
        self.already_collided = False
        self.scored = False
        self.has_popped = False

    def move(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        self.y_speed += 0.3

        if self.scored and not self.has_popped:
            self.surf = pygame.image.load('./assets/' + "empty" + '.png').convert_alpha()
            self.has_popped = True
