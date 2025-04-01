import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.entity import Entity
from code.entity_factory import EntityFactory

class LevelFinish:
    def __init__(self, window, name, reason, points):
        self.window = window
        self.name = name
        self.reason = reason
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('classroom_background'))
        self.points = points

    def run(self, ):
        pygame.mixer_music.load('./assets/menu_background_music.wav')
        pygame.mixer_music.play(-1)


        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

            self.level_text(30, f'ACABOU O JOGO!', (255, 255, 255), (140, 25))
            self.level_text(24, f'{self.reason}', (255, 255, 255), (140, 60))
            self.level_text(24, f'Pontuação: {self.points}', (255, 255, 255), (140, 90))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)