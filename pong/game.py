import pygame
from paddle import Paddle
from ball import Ball
import random


class GameState:
    def __init__(self, left_hits, right_hits, left_points, right_points):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_points = left_points
        self.right_points = right_points


class GameModel:
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.left_paddle = Paddle(10, self.window_height // 2 - Paddle.HEIGHT // 2)
        self.right_paddle = Paddle(self.window_width - 10 - Paddle.WIDTH, self.window_height // 2 - Paddle.HEIGHT // 2)
        self.ball = Ball(self.window_width // 2, self.window_height // 2)

        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
        self.window = window

    def _draw_divider(self):
        for i in range(10, self.window_height, self.window_height // 20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(
                self.window, self.WHITE, (self.window_width // 2 - 5, i, 10, self.window_height // 20))

    def _draw_score(self):
        left_score_text = self.SCORE_FONT.render(f"{self.left_score}", 1, self.WHITE)
        right_score_text = self.SCORE_FONT.render(f"{self.right_score}", 1, self.WHITE)
        self.window.blit(left_score_text, (self.window_width // 4 - left_score_text.get_width() // 2, 20))
        print(self.window_width // 4 - left_score_text.get_width() // 2)
        self.window.blit(right_score_text, (self.window_width * (3 / 4) - right_score_text.get_width() // 2, 20))
        print(self.window_width * (3 / 4) - right_score_text.get_width() // 2)

    def _draw_hits(self):
        hits_text = self.SCORE_FONT.render(f"{self.left_hits + self.right_hits}", 1, self.RED)
        self.window.blit(hits_text, (self.window_width // 2 - hits_text.get_width() // 2, 10))

    def draw(self, draw_score=True, draw_hits=False):
        self.window.fill(self.BLACK)

        self._draw_divider()

        if draw_score:
            self._draw_score()

        if draw_hits:
            self._draw_hits()

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.window)

        self.ball.draw(self.window)

    def move_paddle(self, left_paddle=True, up=True):
        if left_paddle:
            if up and self.left_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.left_paddle.y + Paddle.VEL > self.window_height:
                return False

            self.left_paddle.move(up)
        else:
            if up and self.right_paddle - Paddle.VEL < 0:
                return False
            if not up and self.right_paddle.y + Paddle.VEL > self.window_height:
                return False

            self.right_paddle.move(up)

    def reset(self):
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
