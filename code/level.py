

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.entity import Entity
from code.entity_factory import EntityFactory
from code.entity_mediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('forest_background'))
        self.entity_list.append(EntityFactory.get_entity('dude'))
        self.entity_list.append(EntityFactory.get_entity('trash_bin'))

    def run(self, ):
        pygame.mixer_music.load('./assets/menu_background_music.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, Player):
                    shot = ent.shoot()
                    if shot is not None:
                        self.entity_list.append(shot)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True, color=text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)