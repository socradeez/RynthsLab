import pygame as pg
import random
import mapgen
import camera
import character
import sys

class Game:
    def __init__(self, resolution):
        #setup pygame and the game window
        pg.init()
        self.resolution = resolution
        self.screen = pg.display.set_mode(resolution)
        self.load_map(1)
        self.abs_dimensions = (self.map.abs_dims[0], self.map.abs_dims[1])
        self.camera = camera.Camera([150, 150], resolution, self.abs_dimensions[0], self.abs_dimensions[1])
        self.character = character.Character(abs_position=[150, 150],
                                             look_pos=(0,0),
                                             screen=self.screen)
        self.character.draw()
        self.camera.update(self.screen, self.character, self.map)
        self.run()

    def load_map(self, map):
        #generate a map object given a level number or title as input
        self.map = mapgen.Map(1)

    def update_screen(self):
        self.camera.update(self.screen, self.character, self.map)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pressed_keys = pg.key.get_pressed()
            if pressed_keys[pg.K_w]:
                self.character.abs_position[1] -= 1
            if pressed_keys[pg.K_s]:
                self.character.abs_position[1] += 1
            if pressed_keys[pg.K_a]:
                self.character.abs_position[0] -= 1
            if pressed_keys[pg.K_d]:
                self.character.abs_position[0] += 1
            self.update_screen()

mygame = Game((1000, 800))
mygame.load_map(1)
