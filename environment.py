from typing import Union

import sprite_base
import pygame as pg

class HWall(sprite_base.SpriteCus):
    def __init__(self, indices):
        self.indices = indices
        y, x = indices
        abs_x = x * 55 - 5
        abs_y = y * 55 + 50
        abs_position = (abs_x, abs_y)
        super().__init__(abs_position)
        self.width = 60
        self.height = 5
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))

class VWall(sprite_base.SpriteCus):
    def __init__(self, indices):
        self.indices = indices
        y, x = indices
        abs_x = x * 55 + 50
        abs_y = y * 55 - 5
        abs_position = (abs_x, abs_y)
        super().__init__(abs_position)
        self.width = 5
        self.height = 60
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))




