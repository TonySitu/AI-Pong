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
    MAX_ANGLE = 30
    RADIUS = 7

    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y

        angle = _get_random_angle(-self.MAX_ANGLE, self.MAX_ANGLE, [0])
        position = 1 if random.random() < 0.5 else -1

        self.x_vel = position * abs(math.cos(angle) * self.MAX_VEL)
        self.y_vel = position * abs(math.sin(angle) * self.MAX_VEL)

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.RADIUS)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        angle = _get_random_angle(-30, 30, [0])
        self.y_vel = self.MAX_VEL * math.sin(angle)
        self.x_vel *= -1
