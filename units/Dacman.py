from general import Unit
from game import settings


class Dacman(Unit):

    direction = 0
    coord_x = settings.FIELD_SIZE_X - 1
    coord_y = settings.FIELD_SIZE_Y - 1
    directions_str = "8564"
    step = 1
