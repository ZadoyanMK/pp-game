from .Subject import Subject
from .Map import Map
from game import settings


class Unit(Subject):

    direction = 0

    def _check_valid(self, x=None, y=None):
        if x:
            return x in range(settings.FIELD_SIZE_X) and self.interaction(x=x)
        if y:
            return y in range(settings.FIELD_SIZE_Y) and self.interaction(y=y)

        return True

    def step_up(self, val):
        self.direction = settings.DIRECTIONS['up']
        Map.set_to_map_data(
            x=self.coord_x, y=self.coord_y,
            val=settings.EMPTY_FIELD)
        if self._check_valid(x=self.coord_x - val):
            self.coord_x -= val

    def step_down(self, val):
        self.direction = settings.DIRECTIONS['down']
        Map.set_to_map_data(
            x=self.coord_x, y=self.coord_y,
            val=settings.EMPTY_FIELD)
        if self._check_valid(x=self.coord_x + val):
            self.coord_x += val

    def step_left(self, val):
        self.direction = settings.DIRECTIONS['left']
        Map.set_to_map_data(
            x=self.coord_x, y=self.coord_y,
            val=settings.EMPTY_FIELD)
        if self._check_valid(y=self.coord_y - val):
            self.coord_y -= val

    def step_right(self, val):
        self.direction = settings.DIRECTIONS['right']
        Map.set_to_map_data(
            x=self.coord_x, y=self.coord_y,
            val=settings.EMPTY_FIELD)
        if self._check_valid(y=self.coord_y + val):
            self.coord_y += val
