""" Core module for main character logic. """
import copy
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

test_char_rect = pg.Rect(0, 0, 5, 5)

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
        self.image: pg.Surface = pg.Surface((5, 5))
        self.image.fill((136, 8, 8))
        self.rect = self.image.get_rect()
        self.groups = groups

    def draw(self) -> None:
        """ Draw the character to the screen. """
        pg.draw.rect(self.screen, (136,8,8), self.rect)

    def update(self, key_input, mouse_input, *groups) -> None:
        """ Update character based on input. """
        self.groups = groups
        self.update_loc(key_input)
        print("Current position:", self.abs_position)
        self.update_dir(mouse_input)
        self.use_weapon(mouse_input)

    def update_loc(self, key_input) -> None:
        """ Update the character's position."""
        move_dist = 5
        start_pos = copy.deepcopy(self.abs_position)
        x = 0
        y = 1
        if key_input[keybindings['up']]:
            self.abs_position[y] -= 5
            collision_adj = self.check_collision(start_pos, x)
            if collision_adj:
                self.abs_position = start_pos - collision_adj

        if key_input[keybindings['down']]:
            self.abs_position[y] += 5
            collision_adj = self.check_collision(start_pos, x)
            if collision_adj:
                self.abs_position = start_pos + collision_adj

        if key_input[keybindings['left']]:
            self.abs_position[x] -= 5
            collision_adj = self.check_collision(start_pos, y)
            if collision_adj:
                self.abs_position = start_pos - collision_adj

        if key_input[keybindings['right']]:
            self.abs_position[x] += 5
            collision_adj = self.check_collision(start_pos, y)
            if collision_adj:
                self.abs_position = start_pos + collision_adj

    def check_collision(self, start_pos, axis) -> Tuple[int, int]:
        """ Check for collision with another object based on current position. """
        collision_object: sprite_base.SpriteCus = pg.sprite.spritecollideany(sprite=self,
                                                                             group=self.groups[axis])
        if collision_object:
            print("collision detected:", collision_object)
            coll_pos = collision_object.abs_position
            return start_pos - coll_pos
        else:
            return None


    def update_dir(self, mouse_input) -> None:
        """ Update the character's direction. """

    def use_weapon(self, mouse_input) -> None:
        """ Use the character's weapon. """

    def animate(self) -> None:
        """ Animate the character. """
        # thinking different image for each direction
