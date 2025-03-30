from code.ball import Ball
from code.const import WIN_HEIGHT
from code.entity import Entity
from code.player import Player


class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity, entity_list: list[Entity]):
        if isinstance(entity, Ball):
            if entity.rect.top > WIN_HEIGHT:
                entity_list.remove(entity)
                player = next((e for e in entity_list if isinstance(e, Player)), None)
                player.is_shooting = False

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity, entity_list)
