from code.ball import Ball
from code.entity import Entity


class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Ball):
            # destroy
            pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity)
