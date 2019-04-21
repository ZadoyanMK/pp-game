from general import Subject
from random import randint
from game import settings


class FieldSubjects(Subject):

    def __init__(self, *a, **kw):
        super(Subject, self).__init__(*a, **kw)

        self.coord_x = randint(0, settings.FIELD_SIZE_X - 1)
        self.coord_y = randint(0, settings.FIELD_SIZE_Y - 1)
