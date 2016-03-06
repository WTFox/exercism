import operator

__author__ = 'anthonyfox'

NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'


class Robot(object):
    def __init__(self, initial_bearing=NORTH, coordx=0, coordy=0):
        self.coordinates = (coordx, coordy)
        self.bearing = initial_bearing
        self.directions = [EAST, SOUTH, WEST, NORTH]

    def turn_left(self):
        new_direction = self.directions.index(self.bearing) - 1
        try:
            self.bearing = self.directions[new_direction]
        except IndexError:
            self.bearing = self.directions[len(self.directions)]

    def turn_right(self):
        new_direction = self.directions.index(self.bearing) + 1
        try:
            self.bearing = self.directions[new_direction]
        except IndexError:
            self.bearing = self.directions[0]

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = tuple(map(operator.add, self.coordinates, (0, 1)))

        elif self.bearing == EAST:
            self.coordinates = tuple(map(operator.add, self.coordinates, (1, 0)))

        elif self.bearing == SOUTH:
            self.coordinates = tuple(map(operator.add, self.coordinates, (0, -1)))

        elif self.bearing == WEST:
            self.coordinates = tuple(map(operator.add, self.coordinates, (-1, 0)))

    def simulate(self, instructions):
        hash_map = dict(
            L="turn_left",
            R="turn_right",
            A="advance"
        )

        for i in instructions:
            getattr(self, hash_map[i])()

