import pygame
from pygame.sprite import Sprite
from settings import Settings


class Bullet(Sprite):
    """管理飞船发射的所有子弹的类"""

    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = Settings()
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再将其移动到正确位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midleft

        # 存储用小数表示子弹位置
        self.x = float(self.rect.x)

        # 发射标志
        self.fire_bullet = False

    def update(self):
        """发射标志为True，向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.x += self.settings.bullet_speed
        # 更新子弹的rect的y坐标
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


