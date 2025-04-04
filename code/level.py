

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.const import COLOR_ORANGE, WIN_WIDTH
from code.entity import Entity
from code.entity_factory import EntityFactory
from code.entity_mediator import EntityMediator
from code.player import Player
from code.teacher import Teacher


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('classroom_background'))
        self.entity_list.append(EntityFactory.get_entity('dude'))
        self.entity_list.append(EntityFactory.get_entity('trash_bin'))
        self.entity_list.append(EntityFactory.get_entity('teacher'))

    def run(self, ):
        pygame.mixer_music.load('./assets/menu_background_music.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        player =  next(filter(lambda e: isinstance(e, Player), self.entity_list))
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
                if event.type == Teacher.LOOK_EVENT:
                    teacher = next((e for e in self.entity_list if isinstance(e, Teacher)), None)
                    teacher.update_is_looking()

            self.level_text(24, 'Segure X para arremessar a bola!', (255, 0 ,0), (250, 330))
            self.level_text(30, f'Pontuação: {player.points}        Tentativas: {player.shoots_left}', (255, 255, 255), (140, 25))
            self.level_text(30, f'Power:', (255, 255, 255), (140, 80))
            self.level_text(10, f'{("█" * max(0, int(player.power * 10) - 10))}', (237, 28, 36), (240, 93))

            pygame.display.flip()

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_teacher_is_looking(self.entity_list, self.window)
            EntityMediator.verify_attempts_are_over(self.entity_list, self.window)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)