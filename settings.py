#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/8/21 17:47
# @E-mail: leo.liu@italki.com
class Settings:
    """所有设置类"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 7
        self.bullet_height = 13
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed = 0.5
        self.fleet_drop_speed = 30
        # fleet_direction为1表示向右移，为-1表示左移。
        self.fleet_direction = 1
