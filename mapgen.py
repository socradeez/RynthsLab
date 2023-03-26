import numpy as np
import random

class Map:
    config = {1: {
                'dims': (50, 50)
    }}
    def __init__(self, level):
        #map object takes in the level number as argument to determine settings (size, rooms, etc)
        self.level = level
        self.make_maze()
    
    def make_maze(self):
        #generate 2 arrays; one each for horizontal and vertical walls
        #start by getting the dimensions of the maze matrix from the config options
        width = Map.config[self.level]['dims'][0]
        height = Map.config[self.level]['dims'][1]
        #initialize the arrays needed for maze generation and the cell stack
        cells = np.array([['uv'] * height] * width)
        hwalls = np.array([['bl'] * height] * width)
        vwalls = np.array([['bl'] * height] * width)
        stack = []
        #all steps shown are directly from the wiki:
        #choose the initial cell
        y, x = (0, 0)
        #mark it as visited
        cells[y][x] = 'v'
        #push it to the stack
        stack.append((x, y))
        #while the stack is not empty
        while len(stack) != 0:
            #pop the last cell from the stack (regular ii_walk uses a random cell from the stack, this method uses the most recent cell for longer dead-ends)
            newcell = stack.pop(-1)
            #make it the current cell
            y, x = newcell
            #get the coordinates of all neighbors
            neighbor_coords = [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]
            #validate neighbor coordinates to prune any nonvalid coordinates
            checkcoords = [coord for coord in neighbor_coords if (-1 < coord[0] < width and -1 < coord[1] < height)]
            #get the values of all valid neighbor coordinates
            values = [cells[coord[0]][coord[1]] for coord in checkcoords]
            #check if there are any unvisited neighbors of the current cell
            if 'uv' in values:
                #push the current cell to the stack
                stack.append(newcell)
                #choose one of the unvisited neighbors coordinates
                choice = random.choice(checkcoords)
                #if keep choosing a random neighbor until you find one that is unvisited (not efficient)
                while cells[choice[0]][choice[1]] != 'uv':
                    choice = random.choice(checkcoords)
                #remove the wall between the current cell and chosen neighbor cell ('ub' stands for 'unblocked')
                if choice[0] < y:
                    hwalls[y - 1][x] = 'ub'
                elif choice[0] > y:
                    hwalls[y][x] = 'ub'
                elif choice[1] < x:
                    vwalls[y][x - 1] = 'ub'
                elif choice[1] > x:
                    vwalls[y][x] = 'ub'
                #mark the chosen neighbor cell as visited
                cells[choice[0]][choice[1]] = 'v'
                #push it to the stack
                stack.append(choice)
        #finally, save the wall matrices as attributes of the Map object
        self.hwalls = hwalls
        self.vwalls = vwalls
