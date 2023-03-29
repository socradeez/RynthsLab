import pygame as pg
import random
import mapgen
import camera
import character
import sys
import handler

class Game:
    def __init__(self, resolution):
        #setup pygame and the game window
        pg.init()
        self.resolution = resolution
        self.load_map(1)
        self.abs_dimensions = pg.math.Vector2(self.map.abs_dims[0], self.map.abs_dims[1])
        self.camera = camera.Camera(pg.math.Vector2(150, 150), resolution, self.abs_dimensions[0], self.abs_dimensions[1])
        self.character = character.Character(self.abs_dimensions, self.camera, abs_position=pg.math.Vector2(0, 0),
                                             look_pos=pg.math.Vector2(0,0))
        self.handler = handler.EntityHandler(self.camera, self.character)
        self.camera.update_pos(self.map, self.character)
        self.clock = pg.time.Clock()
        self.run()

    def load_map(self, map):
        #generate a map object given a level number or title as input
        self.map = mapgen.Map(1)

    def run(self):
        while True:
            self.clock.tick(120)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.character.use_weapon(pg.mouse.get_pos(), self.handler.char_projectiles)
            k_input = pg.key.get_pressed()
            m_input = pg.mouse.get_pos()
            #updates abs_pos for all entities, (char first, then camera, then everything else)
            self.handler.update_abs_positions(k_input, self.map)
            #update all rects for entities tracked
            self.handler.update_rects()
            #draw all tracked sprites
            self.camera.render_sprites(self.handler)

mygame = Game((1000, 800))
mygame.load_map(1)
