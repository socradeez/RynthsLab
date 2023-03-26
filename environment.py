import sprite_base

class VWall(sprite_base.SpriteCus):
    #initialize the wall by taking the indices from the vwall matrix
    def __init__(self, indices):
        #convert the indices the absolute pixel position on the map (cells are 50x50px and walls are 5x55px)
        y, x = indices
        abs_x = (x - 1) * 55 + 50
        abs_y = y * 55
        abs_position = (abs_x, abs_y)
        super().__init__(abs_position)

