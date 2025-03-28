import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
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
                pass
            elif selected_menu_item == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
