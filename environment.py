import sprite_base
import pygame as pg

class VWall(sprite_base.SpriteCus):
    #initialize the wall by taking the indices from the vwall matrix
    def __init__(self, indices):
        #convert the indices the absolute pixel position on the map (cells are 50x50px and walls are 5x55px)
        self.indices = indices
        y, x = indices
        abs_x = x * 55 + 50
        abs_y = y * 55
        abs_position = (abs_x, abs_y)
        super().__init__(abs_position)
        self.def_width = 5
        self.def_height = 55
        self.rect: pg.Rect

    def draw(self, screen, camera):
        if self.abs_position[0] < camera.abs_position[0]:
            self.cam_position[0] = 0
            self.width = self.def_width - (camera.abs_position[0] - self.abs_position[0])
        else:
            self.cam_position[0] = self.abs_position[0] - camera.abs_position[0]
            self.width = self.def_width
        if self.abs_position[1] < camera.abs_position[1]:
            self.cam_position[1] = 0
            self.height = self.def_height - (camera.abs_position[1] - self.abs_position[1])
        else:
            self.cam_position[1] = self.abs_position[1] - camera.abs_position[1]
            self.height = self.def_height
        self.rect = pg.Rect(self.cam_position[0], self.cam_position[1], self.width, self.height)
        self.image = pg.draw.rect(screen, (0, 0, 0), self.rect)

class HWall(sprite_base.SpriteCus):
    def __init__(self, indices):
        self.indices = indices
        y, x = indices
        abs_x = x * 55
        abs_y = y * 55 + 50
        abs_position = (abs_x, abs_y)
        super().__init__(abs_position)
        self.def_width = 55
        self.def_height = 5
        self.rect: pg.Rect

    def draw(self, screen, camera):
        if self.abs_position[0] < camera.abs_left:
            self.cam_position[0] = 0
            self.width = self.def_width - (camera.abs_left - self.abs_position[0])
        else:
            self.cam_position[0] = self.abs_position[0] - camera.abs_position[0]
            self.width = self.def_width
        if self.abs_position[1] < camera.abs_top:
            self.cam_position[1] = 0
            self.height = self.def_height - (camera.abs_top - self.abs_position[1])
        else:
            self.cam_position[1] = self.abs_position[1] - camera.abs_top
            self.height = self.def_height
        self.rect = pg.Rect(self.cam_position[0], self.cam_position[1], self.width, self.height)
        if self.indices[1] == 3:
            self.image = pg.draw.rect(screen, (255, 0, 0), self.rect)
        else:
            self.image = pg.draw.rect(screen, (0, 0, 0), self.rect)
