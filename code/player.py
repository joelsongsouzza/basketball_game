from abc import ABC

import pygame
from pygame import K_SPACE

from code.ball import Ball
from code.entity import Entity


class Player(Entity, ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.position = position
        self.direction = 1
        self.speed = 1
        self.max_movement = 150
        self.start_y = position[1]
        self.is_shooting = False

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_x]:
            if not self.is_shooting:
                self.is_shooting = True
                self.surf = pygame.image.load('./assets/' + 'dude_without_ball' + '.png').convert_alpha()
                return Ball('ball', (self.rect.centerx, self.rect.top), 5, -10)

    def move(self):
        movement = self.speed * self.direction
        self.rect.centery += movement
        if abs(self.rect.centery - self.start_y) >= self.max_movement:
            self.direction *= -1