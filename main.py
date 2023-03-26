import pygame as pg
import random
import mapgen

class Game:
    def __init__(self, resolution):
        #setup pygame and the game window
        pg.init()
        self.resolution = resolution
        self.screen = pg.display.set_mode(resolution)
    
    def load_map(self, map):
        #generate a map object given a level number or title as input
        self.map = mapgen.Map(1)
        

mygame = Game((200, 200))
mygame.load_map(1)
