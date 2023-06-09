""" Core module for main character logic. """
import copy
from typing import Optional, Tuple, Union

import pygame as pg

import sprite_base
import projectile


CHAR_SPEED = 2

keybindings = {
    'up': pg.K_w,
    'down': pg.K_s,
    'left': pg.K_a,
    'right': pg.K_d,
}

class Character(sprite_base.EntityCus):
    """ User controllable character. """
    bounds = pg.sprite.Group()

    def __init__(self, abs_dims, camera,
                 abs_position: Tuple[int, int],
                 look_pos: Tuple[int],
                 image: Optional[str] = None) -> None:
        super().__init__(abs_position=abs_position)
        self.camera = camera
        self.map_right, self.map_bottom = abs_dims
        self.look_pos = pg.math.Vector2(look_pos)
        self.image: pg.Surface = pg.Surface((5, 5))
        self.image.fill((136, 8, 8))
        self.rect = self.image.get_rect()

    '''def draw(self) -> None:
        """ Draw the character to the screen. """
        pg.draw.rect(self.screen, (136,8,8), self.rect)'''

    '''def update(self, key_input) -> None:
        """ Update character based on input. """
        self.update_loc(key_input)'''
        

    def update_pos(self, key_input) -> None:
        """ Update the character's position."""
        start_pos = copy.deepcopy(self.abs_position)
        x = 0
        y = 1

        if key_input[keybindings['up']]:
            self.dy(-CHAR_SPEED)
            if (self.check_collision() or (self.y < 0)):
                self.dy(CHAR_SPEED)

        if key_input[keybindings['down']]:
            self.dy(CHAR_SPEED)
            if (self.check_collision() or
                    (self.y > self.map_bottom - self.rect.height)):
                self.dy(-CHAR_SPEED)

        if key_input[keybindings['left']]:
            self.dx(-CHAR_SPEED)
            if (self.check_collision() or (self.x < 0)):
                self.dx(CHAR_SPEED)

        if key_input[keybindings['right']]:
            self.dx(CHAR_SPEED)
            if (self.check_collision() or
                    (self.x > self.map_right - self.rect.width)):
                self.dx(-CHAR_SPEED)

    def check_collision(self) -> bool:
        """ Check for collision with another object based on current position. """
        collision = pg.sprite.spritecollideany(sprite=self,
                                               group=self.bounds)
        if collision is not None:
            return True
        else:
            return False

    def update_dir(self, mouse_input) -> None:
        """ Update the character's direction. """
        pass

    def use_weapon(self, mouse_input, group) -> None:
        """ Use the character's weapon. """
        group.add(projectile.BasicProjectile(self, mouse_input))
        pass

    def animate(self) -> None:
        """ Animate the character. """
        # thinking different image for each direction
        pass

    def update_bounds(self, *bounds: pg.sprite.Group) -> None:
        """ Update the bounds of the character. """
        self.bounds.empty()
        self.bounds.add(*bounds)
