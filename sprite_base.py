#base sprite class to utilize for any sprites that will be drawn to the screen
#custom class is necessary due to absolute vs relative positioning for camera
from typing import List

import pygame

class SpriteCus(pygame.sprite.Sprite):
    def __init__(self, abs_position: List[int]):
        super().__init__()
        self.abs_position = abs_position
        self.cam_position = [0, 0]
