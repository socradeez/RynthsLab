#camera class for display logic
import environment
import pygame as pg

class Camera:
    def __init__(self, abs_position, resolution, max_x, max_y):
        self.resolution = resolution
        self.abs_position = abs_position
        self.get_boundaries()
        self.hwalls = pg.sprite.Group()
        self.vwalls = pg.sprite.Group()
        self.max_x = max_x
        self.max_y = max_y

    def update(self,screen, target, map):
        if target.abs_position[0] - (self.resolution[0] // 2) < 0:
            self.abs_position[0] = self.resolution[0] // 2
        elif target.abs_position[0] + (self.resolution[0] // 2) > self.max_x:
            self.abs_position[0] = self.max_x - self.abs_position[0]
        else:
            self.abs_position[0] = target.abs_position[0] - (self.resolution[0] // 2)
        if target.abs_position[1] - (self.resolution[1] // 2) < 0:
            self.abs_position[1] = self.resolution[1] // 2
        elif target.abs_position[1] + (self.resolution[1] // 2) > self.max_y:
            self.abs_position[1] = self.max_y - self.abs_position[1]
        else:
            self.abs_position[1] = target.abs_position[1] - (self.resolution[1] // 2)
        self.get_walls_visible(map)
        self.render_sprites(screen)

    def get_boundaries(self):
        self.min_x = self.abs_position[0]
        self.max_x = self.abs_position[0] + self.resolution[0]
        self.min_y = self.abs_position[1]
        self.max_x = self.abs_position[1] + self.resolution[1]

    def get_walls_visible(self, map):
        #get the index range for walls inside display area
        x_wall_range = range(self.min_x // 55, self.max_x // 55)
        y_wall_range = range(self.min_y // 55, self.max_y // 55)
        self.visible_hwall_indices = [wall.indices for wall in self.hwalls]
        self.visible_vwall_indices = [wall.indices for wall in self.vwalls]
        #check the map matrix and create sprites for any existing walls in the display area
        for x in x_wall_range:
            for y in y_wall_range:
                if map.hwalls[y][x] == 'bl' and (y, x) not in self.visible_hwall_indices:
                    self.hwalls.add(environment.HWall((y, x)))
                if map.vwalls[y][x] == 'bl' and (y, x) not in self.visible_vwall_indices:
                    self.vwalls.add(environment.VWall((y, x)))

    def render_sprites(self, screen):
        screen.fill((255, 255, 255))
        for wall in self.hwalls:
            wall.draw(screen, self)
        for wall in self.vwalls:
            wall.draw(screen, self)
        pg.display.flip()
                

        