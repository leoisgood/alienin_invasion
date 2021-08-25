#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/8/21 18:30
# @E-mail: leo.liu@italki.com\
import pygame
import sys


class Bluesky:
    """绘制蓝色背景的pygame窗口"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (135, 206, 235)
        pygame.display.set_caption('Blue sky')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    Bluesky().run_game()
