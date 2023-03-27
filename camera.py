#camera class for display logic
import environment
from typing import Optional

import pygame as pg

class Camera:
    def __init__(self, abs_position, resolution, max_x, max_y):
        self.resolution = resolution
        self.abs_position = abs_position
        self.get_boundaries()
        self.max_x = max_x
        self.max_y = max_y

    def update(self, screen, target, map,
               key_input: Optional = None,
               mouse_input: Optional = None):
        if target.abs_position[0] - (self.resolution[0] // 2) < 0:
            self.abs_position[0] = 0
        elif target.abs_position[0] + (self.resolution[0] // 2) >= self.max_x:
            self.abs_position[0] = self.max_x - self.resolution[0]
        else:
            self.abs_position[0] = target.abs_position[0] - (self.resolution[0] // 2)
        if target.abs_position[1] - (self.resolution[1] // 2) < 0:
            self.abs_position[1] = 0
        elif target.abs_position[1] + (self.resolution[1] // 2) >= self.max_y:
            self.abs_position[1] = self.max_y - self.resolution[1]
        else:
            self.abs_position[1] = target.abs_position[1] - (self.resolution[1] // 2)
        self.get_boundaries()
        self.get_walls_visible(map)
        if key_input is not None or mouse_input is not None:
            self.update_character(target, key_input, mouse_input)
        self.render_sprites(screen, target)

    def update_character(self, target, key_input, mouse_input):
        target.update_bounds(self.hwalls, self.vwalls)
        target.update(key_input, mouse_input)

    def get_boundaries(self):
        self.abs_left = self.abs_position[0]
        self.abs_right = self.abs_position[0] + self.resolution[0]
        self.abs_top = self.abs_position[1]
        self.abs_bottom = self.abs_position[1] + self.resolution[1]

    def get_walls_visible(self, map):
        self.hwalls = pg.sprite.Group()
        self.vwalls = pg.sprite.Group()
        #get the index range for walls inside display area
        x_wall_range = range(int(self.abs_left // 5), int(min(self.abs_right // 55 + 1, 50)))
        y_wall_range = range(int(self.abs_top // 55), int(min(self.abs_bottom // 55 + 1, 50)))
        for x in x_wall_range:
            for y in y_wall_range:
                if map.hwalls[y][x] == 'bl':
                    self.hwalls.add(environment.HWall((y, x)))
                if map.vwalls[y][x] == 'bl':
                    self.vwalls.add(environment.VWall((y, x)))

    def render_sprites(self, screen, target: pg.sprite.Sprite):
        screen.fill((255, 255, 255))
        for wall in self.hwalls:
            wall.draw(screen, self)
        for wall in self.vwalls:
            wall.draw(screen, self)
        target.draw()
        pg.display.flip()



