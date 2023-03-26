""" Core module for main character logic. """
from typing import Optional

import pygame as pg


CHAR_SPEED = 10

class Character(pygame.sprite.Sprite):
    """ User controllable character. """

    def __init__(self, screen: pg.Surface,
                 img: Optional[str] = None, *groups) -> None:
        super().__init__(self)

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

