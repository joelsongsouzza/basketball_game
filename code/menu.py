import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu_background_bigger.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/menu_background_music.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Basketball Game", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTIONS[i], COLOR_ORANGE, ((WIN_WIDTH / 2), (450 + (i * 50))))
                else:
                    self.menu_text(50, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), (450 + (i * 50))))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = menu_option + 1 if menu_option != 2 else 0
                    if event.key == pygame.K_UP:
                        menu_option = menu_option - 1 if menu_option != 0 else 2
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)