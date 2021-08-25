#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/8/21 19:01
# @E-mail: leo.liu@italki.com
#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/8/21 18:30
# @E-mail: leo.liu@italki.com\
import pygame
import sys


class Gamewindow:
    """绘制蓝色背景的pygame窗口"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption('yasuo')
        self.role = Role(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.role.blitme()
            pygame.display.flip()


class Role:
    """管理游戏角色"""

    def __init__(self, game):
        """初始化飞船并设置其初始位置"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # 加载游戏人物图像并获取其外接矩形
        self.image = pygame.image.load('../images/y2.gif')
        self.rect = self.image.get_rect()

        # 对于游戏人物，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制游戏人物"""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    Gamewindow().run_game()
