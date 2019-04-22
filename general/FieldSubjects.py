from general import Subject, Map
from random import randint
from game import settings


class FieldSubjects(Subject):

    def __init__(self, *a, **kw):
        super(Subject, self).__init__(*a, **kw)

        m = Map.get_game_map()
        coord_x = randint(0, settings.FIELD_SIZE_X - 1)
        coord_y = randint(0, settings.FIELD_SIZE_Y - 1)

        while m[coord_x][coord_y] is not None:
            coord_x = randint(0, settings.FIELD_SIZE_X - 1)
            coord_y = randint(0, settings.FIELD_SIZE_Y - 1)

        self.coord_x = coord_x
        self.coord_y = coord_y
