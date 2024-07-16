import pygame
import random
import math


def _get_random_angle(min_angle, max_angle, excluded):
    angle = 0
    while angle in excluded:
        angle = math.radians(random.randrange(min_angle, max_angle))

    return angle


class Ball:
    MAX_VEL = 5
    RADIUS = 7

    def __init__(self, x, y):
        self.x = original_x = x
        self.y = original_y = y

        angle = _get_random_angle(-30, 30, [0])
        position = 1 if random.random() < 0.5 else -1

        self.x_vel = position * abs(math.cos(angle) * self.MAX_VEL)
        self.y_vel = position * abs(math.sin(angle) * self.MAX_VEL)
