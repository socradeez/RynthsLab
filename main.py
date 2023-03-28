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
        self.character = character.Character(abs_position=(0, 0),
                                             look_pos=(0,0),
                                             screen=self.screen)
        self.character.draw()
        self.camera.update(self.screen, self.character, self.map)
        self.clock = pg.time.Clock()
        self.run()

    def load_map(self, map):
        #generate a map object given a level number or title as input
        self.map = mapgen.Map(1)

    def update_screen(self, key_input, mouse_input):
        self.camera.update(self.screen,
                           self.character,
                           self.map,
                           key_input=key_input,
                           mouse_input=mouse_input)

    def run(self):
        while True:
            self.clock.tick(120)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            k_input = pg.key.get_pressed()
            m_input = pg.mouse.get_pos()
            self.update_screen(key_input=k_input, mouse_input=m_input)

mygame = Game((1000, 800))
mygame.load_map(1)
