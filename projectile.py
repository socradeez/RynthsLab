""" Bullets fired by the player and enemies. """
from typing import Optional, Tuple, Union

import pygame as pg
import sprite_base
import math
import character

class BasicProjectile(sprite_base.EntityCus):
    """ Simple projectile that moves in a straight line and can bounce off a surface. """

    def __init__(self,
                 shooter,
                 target: pg.math.Vector2,
                 img: Optional[str] = None,
                 *groups) -> None:
        super().__init__(shooter.abs_position)
        self.image = pg.Surface((2, 2))
        self.image.fill((150, 150, 0))
        self.speed = 4
        self.velocity = pg.math.Vector2(target) - pg.math.Vector2(shooter.rect.center)
        self.velocity.scale_to_length(self.speed)
        self.velocity = pg.math.Vector2(math.floor(self.velocity[0]), math.floor(self.velocity[1]))
        self.rect = self.image.get_rect(topleft=shooter.rect.center)
        # initialize the sprite
        pass


    def update(self) -> None:
        """ Update the projectile's position. """
        self.abs_position = self.abs_position + self.velocity
        pass

    def draw(self, camera):
        self.update_rel(camera)
        self.rect.topleft = self.cam_position
        if pg.sprite.spritecollideany(self, camera.vwalls) or pg.sprite.spritecollideany(self, camera.hwalls):
            self.kill()
            return
        camera.screen.blit(self.image, self.rect)

    def check_collision(self) -> None:
        """ Check if the projectile has collided with anything. """
        pass

