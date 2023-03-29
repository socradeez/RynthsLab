""" Pathing algorithms for NPC movement.

    Notes
    -----
    Module may be merged with mapgen.py in the future.
"""
import heapq
import numpy
from typing import Tuple, Union, NamedTuple, List, Optional, Set, Dict

from mapgen import Map


class Coord(NamedTuple):
    x: int
    y: int


class Node:
    def __init__(self, position: Tuple[int, int], parent=None):
        self.position = Coord(*position)
        self.parent = parent
        self.g = 0 # cost from start to current node
        self.h = 0 # heuristic cost from current node to end; euclidean distance
        self.f = numpy.inf # total cost of node

    def __lt__(self, other):
        return self.cost < other.cost

    @property
    def cost(self):
        return self.g + self.h

def euclidean_distance(start, end):
    """ Euclidean distance between two points.
    """
    x1, y1 = start
    x2, y2 = end
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def taxicab_distance(start, end):
    """ Taxicab distance between two points.
    """
    x1, y1 = start
    x2, y2 = end
    return abs(x2 - x1) + abs(y2 - y1)

def get_neighbors(pos: Union[Coord, Tuple[int, int]], space: numpy.ndarray):
    """ Get the neighbors of a node in a given 2D space.
    """
    if not isinstance(pos, Coord):
        pos = Coord(*pos)

    neighors = []
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
       neighbor_pos = (pos.x + dx, pos.y + dy)

def astar(start, end, space):
    """ A* pathfinding algorithm. """
    start_node = Node(start)
    end_node = Node(end)
    open_list = []
