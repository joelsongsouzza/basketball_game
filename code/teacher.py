from abc import ABC
import pygame
import random

from code.entity import Entity


class Teacher(Entity, ABC):
    LOOK_EVENT = pygame.USEREVENT + 1

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.position = position
        self.is_going_to_look = False
        self.is_looking = False
        pygame.time.set_timer(self.LOOK_EVENT, 4000)

    def move(self):
        pass

    def update_is_looking(self):
        if self.is_going_to_look:
            self.surf = pygame.image.load('./assets/' + 'teacher_standing' + '.png').convert_alpha()
            self.is_looking = True
            self.is_going_to_look = False
            return
        elif self.is_looking:
            self.surf = pygame.image.load('./assets/' + 'teacher_sitting' + '.png').convert_alpha()
            self.is_looking = False
            return

        self.is_going_to_look = random.choice([True, False])
        if self.is_going_to_look:
            self.surf = pygame.image.load('./assets/' + 'teacher_alert' + '.png').convert_alpha()
            return
