import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            selected_menu_item = menu.run()

            if selected_menu_item == MENU_OPTIONS[0]:
                level = Level(self.window, 'classroom_background')
                level_return = level.run()
            elif selected_menu_item == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
            else:
                pass
