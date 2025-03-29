from code.Const import WIN_HEIGHT
from code.background import Background
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'forest_background':
                return [Background('forest_background', (0, 0))]
            case 'dude':
                return Player('dude', (100, WIN_HEIGHT / 2))
