from code.const import WIN_HEIGHT, WIN_WIDTH
from code.background import Background
from code.ball import Ball
from code.player import Player
from code.trash_bin import TrashBin


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'classroom_background':
                return [Background('classroom_background', (0, 0))]
            case 'dude':
                return Player('dude', (25, 570))
            case 'trash_bin':
                return TrashBin('trash_bin', (500, 650))
