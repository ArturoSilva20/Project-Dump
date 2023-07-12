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

"""contains paddle class"""

import pygame


class Paddle:
    """player paddle class"""

    def __init__(self, surface, position=(0, 0)):
        self._surface = surface
        self._radius = 3
        self._width = 60
        self._height = 5
        self._color = pygame.Color((0, 0, 0))
        self._rect = pygame.Rect(position, (self._width, self._height))

    def draw(self):
        """draws paddle"""
        self._rect = pygame.draw.rect(self._surface, self._color, self._rect)

    def change_pos(self, x_pos, y_pos):
        """forcibly changes the paddle position"""
        self._rect.centerx = x_pos
        self._rect.centery = y_pos

    def move_left(self):
        """moves paddle left 5 pixels"""
        if self._rect.x > 0:
            self._rect.x -= 5

    def move_right(self):
        """moves paddle right 5 pixels"""
        if self._rect.right < (self._surface.get_width()):
            self._rect.x += 5

    def check_collision(self, rect):
        """returns true if collides with a given rect"""
        if self._rect.colliderect(rect):
            return True
        return False

    @property
    def rect(self):
        """returns rect object of paddle"""
        return self._rect


class EnemyPaddle(Paddle):
    """enemy paddle class with simple tracking"""

    def track_ball(self, ball_x):
        """simple tracking of ball limited by movement speed"""
        if self._rect.centerx < ball_x:
            self.move_right()
        if self._rect.centerx > ball_x:
            self.move_left()
