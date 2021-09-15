#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/9/5 21:29
# @E-mail: leo.liu@italki.com
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始外形并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)


if __name__ == '__main__':
    # Alien.rect()
    pass
