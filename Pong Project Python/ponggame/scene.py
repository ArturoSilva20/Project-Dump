# Arturo Silva
# CPSC 386-00
# 2022-07-24
# arturitosilva20@csu.fullerton.edu
# @ArturoSilva20
#
# Lab 04-01
#
# Simple Pong game
#

"""contains scene objects"""

import pygame
from ponggame import ball
from ponggame import paddle


def make_text(text, color, bgcolor, top, left):
    """creates a text surface and rect"""
    basic_font = pygame.font.Font("freesansbold.ttf", 20)
    text_surf = basic_font.render(text, True, color, bgcolor)
    text_rect = text_surf.get_rect()
    text_rect.center = (top, left)
    return (text_surf, text_rect)


class Scene:
    """basic scene object"""

    def __init__(self, screen, color=(50, 50, 50)):
        """initializes"""
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(color)
        self._frame_rate = 30
        self._sound = True

    def draw(self):
        """draws scene background"""
        self._screen.blit(self._background, (0, 0))

    def handle_event(self, event):
        """handles events of scene"""
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            self._sound = False

    def handle_input(self):
        """input if needed"""

    def update(self):
        """update if needed"""


class TitleScene(Scene):
    """title scene class"""

    def draw(self):
        """draws background and text for title"""
        super().draw()
        text_surf, text_rect = make_text(
            "PongGame",
            (0, 0, 0),
            (50, 50, 50),
            self._screen.get_width() / 2,
            self._screen.get_height() / 2,
        )
        self._screen.blit(text_surf, text_rect)
        text_surf, text_rect = make_text(
            "Press Space to Continue",
            (0, 0, 0),
            (50, 50, 50),
            self._screen.get_width() / 2,
            self._screen.get_height() - 20,
        )
        self._screen.blit(text_surf, text_rect)
        text_surf, text_rect = make_text(
            "Use Left and Right arrow keys to move",
            (0, 0, 0),
            (50, 50, 50),
            self._screen.get_width() / 2,
            self._screen.get_height() - 40,
        )
        self._screen.blit(text_surf, text_rect)


class GameScene(Scene):
    """game scene object"""

    def __init__(self, screen, color=(50, 50, 50)):
        """initializes"""
        super().__init__(screen, color)
        self._ball = ball.PongBall(self._screen)
        self._ball.change_pos(
            self._screen.get_width() / 2, self._screen.get_height() / 2
        )
        self._paddle1 = paddle.Paddle(screen)
        self._paddle1.change_pos(
            self._screen.get_width() / 2, self._screen.get_height() - 40
        )
        self._paddle2 = paddle.EnemyPaddle(self._screen)
        self._paddle2.change_pos(self._screen.get_width() / 2, 40)
        self._user_input = pygame.key.get_pressed()
        self._awaiting = True
        self._player_score = 0
        self._com_score = 0
        self._player_last = True

    def draw(self):
        """draws game objects and prompts"""
        super().draw()
        if self._awaiting:
            text_surf, text_rect = make_text(
                "Press Enter to continue",
                (0, 0, 0),
                (50, 50, 50),
                self._screen.get_width() / 2,
                self._screen.get_height() - 200,
            )
            self._screen.blit(text_surf, text_rect)
        self._paddle1.draw()
        self._paddle2.draw()
        self._ball.draw()
        self.update()

    def update_score(self):
        """updates score and displays text"""
        if self._ball.hit_top:
            self._player_score += 1
            self.restart()

        if self._ball.hit_bottom:
            self._com_score += 1
            self.restart()
        string = "You: " + str(self._player_score) + "    Com: " + str(self._com_score)
        text_surf, text_rect = make_text(
            string, (0, 0, 0), (50, 50, 50), self._screen.get_width() / 2, 20
        )
        self._screen.blit(text_surf, text_rect)

    def start(self):
        """starts game movement"""
        self._awaiting = False
        self._ball.start(self._player_last)

    def restart(self):
        """resets ball and prompt"""
        self._ball.reset()
        self._awaiting = True

    def handle_input(self):
        """handles game input"""
        self._user_input = pygame.key.get_pressed()
        if self._user_input[pygame.K_LEFT]:
            self._paddle1.move_left()
        if self._user_input[pygame.K_RIGHT]:
            self._paddle1.move_right()
        if self._user_input[pygame.K_RETURN]:
            self.start()

    def game_over(self):
        """Returns true if score reaches a certain amount"""
        if self._player_score == 5 or self._com_score == 5:
            return True
        return False

    def update(self):
        """updates game objects and checks for changes in collisions"""
        self._ball.bounce()
        collide1 = self._paddle1.check_collision(self._ball.rect)
        collide2 = self._paddle2.check_collision(self._ball.rect)
        if collide1:
            offset = self._paddle1.rect.centerx - self._ball.rect.centerx
            vector = pygame.Vector2(offset / 120, 1)
            self._ball.forced_bounce(vector)
        if collide2:
            offset = self._paddle2.rect.centerx - self._ball.rect.centerx
            vector = pygame.Vector2(offset / 120, 1)
            self._ball.forced_bounce(vector)
        self._ball.update_pos()
        self._paddle2.track_ball(self._ball.rect.x)
        self.update_score()

    def did_player_win(self):
        """returns true if player beat computer"""
        if self._player_score > self._com_score:
            return True
        return False

    def remove_score(self):
        """resets score"""
        self._player_score = 0
        self._com_score = 0

    @property
    def player_score(self):
        """returns player score"""
        return self._player_score

    @property
    def computer_score(self):
        """returns computer score"""
        return self._com_score


class WinnerScene(Scene):
    """winner display screen"""

    def __init__(self, screen, color=(50, 50, 50)):
        """initializes"""
        super().__init__(screen, color)
        self._player_won = False
        self._player_score = 0
        self._computer_score = 0

    def draw(self):
        """draws text to display who won"""
        super().draw()
        text = "Computer Won"
        if self._player_won:
            text = "You Won!"
        text_surf, text_rect = make_text(
            text,
            (0, 0, 0),
            (50, 50, 50),
            self._screen.get_width() / 2,
            self._screen.get_height() / 2,
        )
        self._screen.blit(text_surf, text_rect)
        text_surf, text_rect = make_text(
            "Press Space to continue",
            (0, 0, 0),
            (50, 50, 50),
            self._screen.get_width() / 2,
            self._screen.get_height() - 80,
        )
        self._screen.blit(text_surf, text_rect)

        score_text = (
            "Player: "
            + str(self._player_score)
            + " Computer: "
            + str(self._computer_score)
        )
        text_surf, text_rect = make_text(
            score_text,
            (0, 0, 0),
            (50, 50, 50),
            self._screen.get_width() / 2,
            self._screen.get_height() / 3,
        )
        self._screen.blit(text_surf, text_rect)

    def player_won(self, player):
        """takes boolean and sets the player to win if they won"""
        self._player_won = player

    def add_score(self, player, computer):
        """stores score of players"""
        self._player_score = player
        self._computer_score = computer
