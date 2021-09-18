#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/9/16 22:05
# @E-mail: leo.liu@italki.com
import pygame
from settings import Settings
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, star_sky):
        """初始化每颗星的位置"""
        super().__init__()
        self.screen = star_sky.screen

        # 加载星星图像并设置其rect属性
        self.image = pygame.image.load('../images/yasuo.bmp')
        self.rect = self.image.get_rect()

        # 设置星星的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星的精确水平位置
        self.x = float(self.rect.x)
