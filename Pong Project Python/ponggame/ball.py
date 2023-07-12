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

"""contains ball class"""

import pygame


class PongBall:
    """pong ball class"""

    default_radius = 5

    def __init__(
            self, surface, pos_vector=pygame.Vector2(0, 0), vel_vector=pygame.Vector2(0, 0)\
    ):
        """initializes"""
        self._surface = surface
        self._velocity = vel_vector
        self._position = pos_vector
        self._speed = 0
        self._hit_bottom = False
        self._hit_top = False
        self._rect = pygame.draw.circle(
            self._surface, pygame.Color((200, 50, 50)), self._position, 5
        )
        self._sound = pygame.mixer.Sound(
            "sound/269718__michorvath__ping-pong-ball-hit.wav"
        )

    def draw(self):
        """draws ball on surface"""
        self._rect = pygame.draw.circle(
            self._surface, pygame.Color((200, 50, 50)), self._position, 5
        )

    def change_pos(self, x_pos, y_pos):
        """forces position to change"""
        self._position.x = x_pos
        self._position.y = y_pos

    def bounce(self):
        """changes the velocity vector of the ball based on edges"""
        if self._position.x < 0:
            self._velocity.reflect_ip((1, 0))
            self._sound.play()
        if self._position.x > self._surface.get_width():
            self._velocity.reflect_ip((1, 0))
            self._sound.play()
        if self._position.y < 0:
            self._velocity.reflect_ip((0, 1))
            self._hit_top = True
            self._sound.play()
        if self._position.y > self._surface.get_height():
            self._velocity.reflect_ip((0, 1))
            self._hit_bottom = True
            self._sound.play()

    def forced_bounce(self, vector):
        """changes velocity given a normal vector"""
        self._velocity.reflect_ip(vector)
        self._velocity.scale_to_length(self._speed)
        self._speed += 0.3
        self._sound.play()

    def update_pos(self):
        """updates position based on velocity vector"""
        self._position.x += self._velocity.x
        self._position.y += self._velocity.y

    def reset(self):
        """resets ball to middle and sets speed to zero"""
        self.change_pos(self._surface.get_width() / 2, self._surface.get_height() / 2)
        self._velocity = pygame.Vector2(0, 0)
        self._speed = 0
        self._hit_bottom = False
        self._hit_top = False

    def start(self, to_player):
        """starts the ball moving"""
        if to_player:
            self._velocity = pygame.Vector2(1, 3)
            self._speed = self._velocity.magnitude()
        else:
            self._velocity = pygame.Vector2(1, -3)
            self._speed = self._velocity.magnitude()

    @property
    def rect(self):
        """returns rect"""
        return self._rect

    @property
    def hit_top(self):
        """returns true if ball hit top of surface"""
        return self._hit_top

    @property
    def hit_bottom(self):
        """returns true if ball hit bottom of surface"""
        return self._hit_bottom
