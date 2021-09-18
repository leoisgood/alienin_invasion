#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/8/21 16:59
# @E-mail: leo.liu@italki.com
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏类资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # 初始化一个外星人
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()  # 飞船类更新位置
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.K_q:
                sys.exit()

    def _check_keydown_events(self, event):
        # helpmethod for check keyup events
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # 发射子弹
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # helpmethod for check keyup events
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入bullets编组"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        # 检查是否有子弹击中外星人，
        # 如果是，就删除响应的子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        # return collisions
        if not self.aliens:
            # 删除现有的子弹并创建一群新的外星人
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """
        检查是否有外星人位于屏幕边缘,
        并更新正群外星人的位置。
        """
        self._check_fleet_edge()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")

    def _create_fleet(self):
        # 创建外星人群
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)  # 外星人区域的宽度
        number_aliens_x = available_space_x // (2 * alien_width)  # 整除得到外星人每行的数量

        # 计算可以容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)  # 外星人区域的高度
        number_rows = available_space_y // (2 * alien_height)  # 整除得到外星人群的行数

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # 创建一个外星人，并将其放到当前行
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edge(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # 改变方向

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
