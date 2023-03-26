#base sprite class to utilize for any sprites that will be drawn to the screen
#custom class is necessary due to absolute vs relative positioning for camera
import pygame

class SpriteCus(pygame.sprite.Sprite):
    def __init__(self, abs_position):
        super().__init__()
        self.abs_position = abs_position
