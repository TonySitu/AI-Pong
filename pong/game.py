import pygame
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

        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
        self.window = window
