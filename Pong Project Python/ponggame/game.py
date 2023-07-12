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

"""contains pong_game class"""
import sys
import pygame
from ponggame import scene


class PongGame:
    """pong game class"""

    def __init__(self, window_width=400, window_height=600):
        """initialize"""
        pygame.init()  # initialize pygame
        pygame.font.init()  # initialize fonts
        pygame.mixer.init()  # initialize sound
        self._window_size = (
            window_width,
            window_height,
        )  # initializes window height and width
        self._clock = pygame.time.Clock()  # create clock
        self._screen = pygame.display.set_mode(self._window_size)  # create window
        pygame.display.set_caption("Pong!")
        self._run = True

        if not pygame.font:
            print("Warning: fonts are disabled.")
        if not pygame.mixer:
            print("Warning: sound is disabled")

        self._scene_index = 0
        self._default_scene = scene.Scene(self._screen)
        self._title_scene = scene.TitleScene(self._screen)
        self._game_scene = scene.GameScene(self._screen)
        self._win_scene = scene.WinnerScene(self._screen)
        self._scene_list = [self._title_scene, self._game_scene, self._win_scene]

    def exit(self):
        """exits pygame and system"""
        self._run = False
        pygame.font.quit()
        pygame.quit()
        sys.exit()

    def handle_event(self, event):
        """handles general controls of game"""
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.exit()
        if event.type == pygame.QUIT:
            self.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_scene()

    def draw_scene(self):
        """draws current scene"""
        self._scene_list[self._scene_index].draw()

    def next_scene(self):
        """shifts to next scene"""
        if self._scene_index == 0 or self._scene_index == 2:
            self._scene_index += 1
        if self._scene_index > 2:
            self._scene_index = 0

    def handle_input(self):
        """handles the input for a given scene"""
        self._scene_list[self._scene_index].handle_input()

    def run(self):
        """runs the game loop"""
        while self._run:
            for event in pygame.event.get():
                self.handle_event(event)

            self.handle_input()
            self.draw_scene()

            if self._scene_list[1].game_over():
                self._scene_list[2].player_won(self._scene_list[1].did_player_win())
                com_score = self._scene_list[1].computer_score
                player_score = self._scene_list[1].player_score
                self._scene_list[1].remove_score()
                self._scene_list[2].add_score(player_score, com_score)
                self._scene_index = 2

            pygame.display.update()
            self._clock.tick(60)
