from code.const import WIN_HEIGHT
from code.background import Background
from code.ball import Ball
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'forest_background':
                return [Background('forest_background', (0, 0))]
            case 'dude':
                return Player('dude', (100, WIN_HEIGHT / 2), Ball('ball', (110, WIN_HEIGHT / 2), 5, -10))
            case 'ball':
                return Ball('ball', (110, WIN_HEIGHT / 2), 5, -10)
