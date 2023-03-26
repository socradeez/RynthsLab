""" Core module for main character logic. """
from typing import Optional

import pygame as pg
import sprite_base


CHAR_SPEED = 10

keybindings = {
    'up': pg.K_w,
    'down': pg.K_s,
    'left': pg.K_a,
    'right': pg.K_d,
}

class Character(sprite_base.SpriteCus):
    """ User controllable character. """

    def __init__(self, abs_position, screen: pg.Surface,
                 img: Optional[str] = None, *groups) -> None:
        super().__init__(abs_position)

        # initialize the sprite
        pass

    def draw(self) -> None:
        pass

    def update_loc(self) -> None:
        """ Update the character's position."""
        pass

    def update_dir(self) -> None:
        """ Update the character's direction. """
        pass

    def use_weapon(self) -> None:
        """ Use the character's weapon. """
        pass

    def animate(self) -> None:
        """ Animate the character. """
        # thinking different image for each direction
        pass

