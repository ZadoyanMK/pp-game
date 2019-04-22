from .Subject import Subject
from .Map import Map
from game import settings


class Unit(Subject):

    directions_str = ""
    step = 1

    def interaction(self, ob=None, x=None, y=None):
        local_x = x if x else self.coord_x
        local_y = y if y else self.coord_y

        m = Map.get_game_map()
        if not m[local_x][local_y]:
            return True
        
        if isinstance(ob, self.__class__):
            return False

        return m[local_x][local_y].interaction(ob=self)

    direction = 0

    def move(self, v):
        if v.upper() == self.directions_str[0]:
            self.step_up(self.step)
        if v.upper() == self.directions_str[1]:
            self.step_down(self.step)
        if v.upper() == self.directions_str[2]:
            self.step_right(self.step)
        if v.upper() == self.directions_str[3]:
            self.step_left(self.step)


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
