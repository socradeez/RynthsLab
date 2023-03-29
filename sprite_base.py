#base sprite class to utilize for any sprites that will be drawn to the screen
#custom class is necessary due to absolute vs relative positioning for camera
from dataclasses import dataclass
from typing import List, NamedTuple, Tuple

import pygame as pg


class Position:
    # thinking of fancier position validation or absolute/relative positioning
    # here, but for now just a simple descriptor for x and y locs
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        instance.__dict__[self.storage_name] = value


class SpriteCus(pg.sprite.Sprite):

    x = Position()
    y = Position()
    rel_x = Position()
    rel_y = Position()

    def __init__(self, abs_position: Tuple[int, int]):
        super().__init__()
        self.x, self.y = pg.math.Vector2(abs_position)
        self.cam_position = pg.math.Vector2(0, 0)
        self.rect: pg.Rect

    @property
    def abs_position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @abs_position.setter
    def abs_position(self, value: Tuple[int, int]):
        self.rect.move_ip(value[0] - self.x, value[1] - self.y)
        self.x, self.y = value

    @property
    def cam_position(self) -> Tuple[int, int]:
        return (self.rel_x, self.rel_y)

    @cam_position.setter
    def cam_position(self, value: List[int]):
        self.rel_x, self.rel_y = value

    def dx(self, value: int):
        self.x += value
        self.rect.move_ip(value, 0)

    def dy(self, value: int):
        self.y += value
        self.rect.move_ip(0, value)

    def update_rel(self, camera):
        self.cam_position = self.abs_position - camera.abs_position
        return self.cam_position

    def draw(self, camera):
        self.update_rel(camera)
        self.rect.topleft = self.cam_position
        camera.screen.blit(self.image, self.rect)
