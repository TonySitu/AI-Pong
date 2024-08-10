import pygame
from paddle import Paddle
from ball import Ball

pygame.init()


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

    def _check_ball_out_of_bounds(self):
        """
        Returns True if ball is out of bounds, false otherwise.
        :return bool:
        """
        if self.ball.x < 0:
            self.right_score += 1
        elif self.ball.x > self.window_width:
            self.left_score += 1
        else:
            return False

        return True

    def _check_ball_within_paddle_height(self, paddle):
        return paddle.y <= self.ball.y <= paddle.y + Paddle.HEIGHT

    def _check_ball_within_paddle_width(self, paddle):
        return self.ball.RADIUS <= paddle.x + Paddle.WIDTH

    def _check_ball_within_paddle(self, paddle):
        """
        Returns True if ball is within bounds of paddle, False otherwise.

        :param paddle that the bounds of the ball are being compared with:
        :return bool:
        """
        return self._check_ball_within_paddle_height(paddle) and self._check_ball_within_paddle_width(paddle)

    def _find_y_vel(self, paddle):
        middle_y = paddle.y + Paddle.HEIGHT / 2
        difference_in_y = middle_y - self.ball.y
        reduction_factor = (Paddle.HEIGHT / 2) / self.ball.MAX_VEL
        y_vel = difference_in_y / reduction_factor
        return y_vel

    def _handle_collisions(self):
        ball = self.ball
        left_paddle = self.left_paddle
        right_paddle = self.right_paddle

        if ball.y + ball.RADIUS >= self.window_height:
            ball.y_vel *= -1
        elif ball.y - ball.RADIUS <= 0:
            ball.y_vel *= -1

        ball.x_vel *= -1

        if ball.x_vel < 0:
            if self._check_ball_within_paddle(left_paddle):
                y_vel = self._find_y_vel(left_paddle)
                ball.y_vel = -1 * y_vel
                self.left_hits += 1

        else:
            if self._check_ball_within_paddle(right_paddle):
                y_vel = self._find_y_vel(right_paddle)
                ball.y_vel = -1 * y_vel
                self.right_hits += 1

    def loop(self):
        self.ball.move()
        self._handle_collisions()

        if self._check_ball_out_of_bounds():
            self.ball.reset()

        game_state = GameState(self.left_hits, self.right_hits, self.left_score, self.right_score)

        return game_state

    def draw(self, draw_score=True, draw_hits=False):
        if draw_score:
            self._draw_score()

        if draw_hits:
            self._draw_hits()

        self.window.fill(self.BLACK)
        self._draw_divider()
        self.left_paddle.draw(self.window)
        self.right_paddle.draw(self.window)

        self.ball.draw(self.window)

    def move_paddle(self, left_paddle=True, up=True):
        # todo change method to take in the actual paddle as the arg
        if left_paddle:
            if up and self.left_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.left_paddle.y + Paddle.VEL > self.window_height:
                return False

            self.left_paddle.move(up)
        else:
            if up and self.right_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.right_paddle.y + Paddle.VEL > self.window_height:
                return False

            self.right_paddle.move(up)

        return True

    def reset(self):
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
