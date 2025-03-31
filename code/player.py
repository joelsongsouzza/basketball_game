from abc import ABC

import pygame

from code.ball import Ball
from code.entity import Entity


class Player(Entity, ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.position = position
        self.is_shooting = False
        self.power = 1
        self.shoots_left = 15
        self.points = 0

    def shoot(self):
        if not self.is_shooting:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_x]:
                if self.power < 7:
                    self.power += 0.15
            elif self.power > 1:
                power_stored = min(7, self.power)
                self.power = 1
                self.shoots_left -= 1
                self.is_shooting = True
                self.surf = pygame.image.load('./assets/' + 'dude_without_ball' + '.png').convert_alpha()
                return Ball('ball', (self.rect.left, self.rect.top), power_stored)


    def move(self):
        pass