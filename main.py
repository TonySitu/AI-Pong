import pygame

from pong import game
from pong import ball
from pong import paddle


class PongGame:
    def __init__(self, window, width, height):
        self.game = game.GameModel(window, width, height)
        self.ball = self.game.ball
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle

    def game_loop(self):
        while True:
            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            game_info = self.game.loop()


def main():
    pass


if __name__ == "__main__":
    main()
