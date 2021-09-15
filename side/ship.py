#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/8/21 17:57
# @E-mail: leo.liu@italki.com
import pygame
from side.settings import Settings


class Ship:
    """管理飞船类"""

    def __init__(self, ai_game):
        """出货实话飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = Settings()
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕左侧的中央
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

#
# if __name__ == '__main__':
#     Ship(ai)
