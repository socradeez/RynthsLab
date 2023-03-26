""" Bullets fired by the player and enemies. """
from typing import Optional, Tuple, Union

import pygame as pg


class BasicProjectile(pg.sprite.Sprite):
    """ Simple projectile that moves in a straight line and can bounce off a surface. """

    def __init__(self,
                 screen: pg.Surface,
                 start_loc: Union[Tuple[int, int], pg.math.Vector2],
                 start_dir: Union[Tuple[int, int], pg.math.Vector2],
                 velocity: float,
                 img: Optional[str] = None,
                 *groups) -> None:
        super().__init__(self)

        # initialize the sprite
        pass


    def draw(self) -> None:
        """ Draw the projectile to the screen. """
        pass


    def update(self) -> None:
        """ Update the projectile's position. """
        pass


    def check_collision(self) -> None:
        """ Check if the projectile has collided with anything. """
        pass

