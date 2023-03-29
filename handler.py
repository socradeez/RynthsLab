#class for entity handler. This class will be responsible for updating the abs_positions and cam_positions/rects for all entities currently tracked

import pygame as pg

class EntityHandler:
    def __init__(self, camera, character):
        self.camera = camera
        self.character = character
        self.enemies = pg.sprite.Group()
        self.char_projectiles = pg.sprite.Group()
        self.enemy_projectiles = pg.sprite.Group()

    def update_abs_positions(self, keys_pressed, map):
        self.character.update_bounds(self.camera.walls)
        self.character.update_pos(keys_pressed)
        self.camera.update_pos(map, self.character)
        for projectile in self.char_projectiles:
            projectile.update_pos()
        for projectile in self.enemy_projectiles:
            projectile.update_pos()
        for enemy in self.enemies:
            enemy.update_pos()

    def update_rects(self):
        self.character.update_rel(self.camera)
        self.sprite_groups = [self.camera.walls, self.enemies, self.char_projectiles, self.enemy_projectiles]
        for group in self.sprite_groups:
            for sprite in group:
                sprite.update_rel(self.camera)
