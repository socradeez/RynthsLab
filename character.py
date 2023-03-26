""" Core module for main character logic. """
from typing import Optional, Tuple, Union

import pygame as pg
import sprite_base


CHAR_SPEED = 10

keybindings = {
    'up': pg.K_w,
    'down': pg.K_s,
    'left': pg.K_a,
    'right': pg.K_d,
}

test_char_rect = pg.Rect(0, 0, 32, 32)

class Character(sprite_base.SpriteCus):
    """ User controllable character. """

    def __init__(self, abs_position: Union[pg.math.Vector2, Tuple[int, int]],
                 look_pos: Union[pg.math.Vector2, Tuple[int, int]],
                 screen: pg.Surface,
                 image: Optional[str] = None, *groups: pg.sprite.Group) -> None:
        super().__init__(abs_position)

        self.screen = screen
        self.abs_position: pg.math.Vector2 = pg.math.Vector2(abs_position)
        self.look_pos = pg.math.Vector2(look_pos)
        self.image: pg.Surface = pg.Surface((32, 32))
        self.image.fill((136, 8, 8))
        self.rect = self.image.get_rect()


    def draw(self) -> None:
        """ Draw the character to the screen. """
        pg.draw.rect(self.screen, (136,8,8), test_char_rect)

    def update(self, key_input, mouse_input) -> None:
        """ Update character based on input. """
        self.update_loc(key_input)
        self.update_dir(mouse_input)
        self.use_weapon(mouse_input)
        self.animate()

    def update_loc(self, key_input) -> None:
        """ Update the character's position."""
        if key_input[keybindings['up']]:
            self.abs_position[1] -= 32
        if key_input[keybindings['down']]:
            self.abs_position[1] += 32
        if key_input[keybindings['left']]:
            self.abs_position[0] -= 32
        if key_input[keybindings['right']]:
            self.abs_position[0] += 32

    def update_dir(self, mouse_input) -> None:
        """ Update the character's direction. """

    def use_weapon(self, mouse_input) -> None:
        """ Use the character's weapon. """

    def animate(self) -> None:
        """ Animate the character. """
        # thinking different image


if __name__ == '__main__':
    screen = pg.display.set_mode((400, 400))
    char =  Character((0, 0), (0, 0), screen)
    char.draw()

    while
