import random

import pygame

from code.ball import Ball
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity
from code.level_finish import LevelFinish
from code.player import Player
from code.teacher import Teacher
from code.trash_bin import TrashBin



class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity, entity_list: list[Entity]):
        if isinstance(entity, Ball):
            if entity.rect.top > WIN_HEIGHT or entity.rect.left > WIN_WIDTH:
                entity_list.remove(entity)
                player = next((e for e in entity_list if isinstance(e, Player)), None)
                player.is_shooting = False
                player.surf = pygame.image.load('./assets/' + 'dude' + '.png').convert_alpha()

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity, entity_list)
            for j in range(len(entity_list)):
                entity2 = entity_list[j]
                if isinstance(entity, Ball) and isinstance(entity2, TrashBin) and entity.already_collided == False:
                    player = next((e for e in entity_list if isinstance(e, Player)), None)
                    EntityMediator.__check_ball_with_bin_collision(entity, entity2, player)

    @staticmethod
    def verify_teacher_is_looking(entity_list: list[Entity], window):
        player = next((e for e in entity_list if isinstance(e, Player)), None)
        teacher = next((e for e in entity_list if isinstance(e, Teacher)), None)

        if player.is_shooting and teacher.is_looking:
            LevelFinish(window, 'classroom_background', 'O professor te viu!', player.points).run()

    @staticmethod
    def verify_attempts_are_over(entity_list: list[Entity], window):
        player = next((e for e in entity_list if isinstance(e, Player)), None)
        if player.shoots_left == 0 and not player.is_shooting:
            LevelFinish(window, 'classroom_background', 'Suas bolinhas acabaram', player.points).run()

    @staticmethod
    def __check_ball_with_bin_collision(ball: Ball, trashbin: TrashBin, player: Player):
        ball_bottom = ball.rect.bottom
        ball_top = ball.rect.top
        ball_left = ball.rect.left
        ball_right = ball.rect.right

        trashbin_top = trashbin.rect.top
        trashbin_bottom = trashbin.rect.bottom
        trashbin_left = trashbin.rect.left
        trashbin_right = trashbin.rect.right

        collided_top = (
                ball_bottom >= trashbin_top > ball_top and
                ball_right > trashbin_left and
                ball_left < trashbin_right
        )

        collided_top_center = (
                ball_bottom >= trashbin_top > ball_top and
                ball_right > trashbin_left + 30 and
                ball_left < trashbin_right - 30
        )

        collided_left = (
                ball_right >= trashbin_left > ball_left and
                ball_bottom > trashbin_top and
                ball_top < trashbin_bottom
        )

        if collided_top_center:
            ball.x_speed = 0
            ball.y_speed = 0
            ball.already_collided = True
            ball.scored = True

            new_x = random.randint(300, 540)
            new_y = 650

            trashbin.rect.centerx =  new_x
            trashbin.rect.top = new_y
            player.points += 1
        elif collided_top:
            ball.y_speed *= -1
            ball.already_collided = True
        elif collided_left:
            ball.x_speed *= -1
            ball.already_collided = True
