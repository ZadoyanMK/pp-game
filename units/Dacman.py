from general import Unit
from game import settings


class Dacman(Unit):

    direction = 0
    coord_x = settings.FIELD_SIZE_X - 1
    coord_y = settings.FIELD_SIZE_Y - 1

    def move(self, v):
        if v.upper() == '8':
            self.step_up(1)
        if v.upper() == '5':
            self.step_down(1)
        if v.upper() == '6':
            self.step_right(1)
        if v.upper() == '4':
            self.step_left(1)
