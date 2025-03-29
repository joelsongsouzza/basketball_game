from code.background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'forest_background':
                return [Background('forest_background', (0, 0))]
