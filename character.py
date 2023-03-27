""" Core module for main character logic. """
import copy
from typing import Optional, List, Tuple, Union

import pygame as pg
import sprite_base


CHAR_SPEED = 2

keybindings = {
    'up': pg.K_w,
    'down': pg.K_s,
    'left': pg.K_a,
    'right': pg.K_d,
}

class Character(sprite_base.SpriteCus):
    """ User controllable character. """

    def __init__(self, abs_position: Union[pg.math.Vector2, Tuple(int, int)],
                 look_pos: Union[pg.math.Vector2, List[int]],
                 screen: pg.Surface,
                 image: Optional[str] = None, *groups: pg.sprite.Group) -> None:
        super().__init__(abs_position=abs_position)
        self.screen = screen
        self.look_pos = pg.math.Vector2(look_pos)
        self.image: pg.Surface = pg.Surface((5, 5))
        self.image.fill((136, 8, 8))
        self.rect = self.image.get_rect()
        self.groups = groups

    @property
    def screen_top(self) -> int:
        """ Return the top of the screen. """
        return self.screen.get_rect().top

    @property
    def screen_bottom(self) -> int:
        """ Return the bottom of the screen. """
        return self.screen.get_rect().bottom

    @property
    def screeen_left(self) -> int:
        """ Return the left of the screen. """
        return self.screen.get_rect().left

    @property
    def screen_right(self) -> int:
        """ Return the right of the screen. """
        return self.screen.get_rect().right

    def draw(self) -> None:
        """ Draw the character to the screen. """
        pg.draw.rect(self.screen, (136,8,8), self.rect)

    def update(self, key_input, mouse_input, *groups) -> None:
        """ Update character based on input. """
        self.groups = groups
        self.update_loc(key_input)
        self.update_dir(mouse_input)
        self.use_weapon(mouse_input)
        self.draw()

    def update_loc(self, key_input) -> None:
        """ Update the character's position."""
        start_pos = copy.deepcopy(self.abs_position)
        print(self.abs_position)
        x = 0
        y = 1

        if key_input[keybindings['up']]:
            self.abs_position[y] -= CHAR_SPEED
            collision_adj = self.check_collision(start_pos, x)
            if collision_adj:
                self.abs_position = start_pos - collision_adj
            self.rect.move_ip(0, -CHAR_SPEED)

        if key_input[keybindings['down']]:
            self.abs_position[y] += CHAR_SPEED
            collision_adj = self.check_collision(start_pos, x)
            if collision_adj:
                self.abs_position = start_pos + collision_adj

        if key_input[keybindings['left']]:
            self.abs_position[x] -= CHAR_SPEED
            collision_adj = self.check_collision(start_pos, y)
            if collision_adj:
                self.abs_position = start_pos - collision_adj

        if key_input[keybindings['right']]:
            self.abs_position[x] += CHAR_SPEED
            collision_adj = self.check_collision(start_pos, y)
            if collision_adj:
                self.abs_position = start_pos + collision_adj


        # restrict character to screen
        if (self.abs_position[0] < self.screeen_left) or \
                (self.abs_position[0] > self.screen_right):
            self.abs_position[0] = start_pos[0]

        if (self.abs_position[1] < self.screen_top) or \
                (self.abs_position[1] > self.screen_bottom):
            self.abs_position[1] = start_pos[1]

    def check_collision(self, start_pos, axis):
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
