#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/9/16 21:59
# @E-mail: leo.liu@italki.com
import pygame
from settings import Settings


class StarSky:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Star sky')
        self.stars = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        self.stars.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    sk = StarSky()
    sk.run_game()
