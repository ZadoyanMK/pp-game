from general import FieldSubjects, GlobalStat
from random import randint
from game import settings
from .Dacman import Dacman
from .Pacman import Pacman


class Point(FieldSubjects):

    # def __init__(self, *a, **k):
    #     super(FieldSubjects, self).__init__(*a, **k)
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        self.value = randint(settings.POINT_MIN_VALUE, settings.POINT_MAX_VALUE)

    def interaction(self, ob=None, x=None, y=None):
        if isinstance(ob, Pacman):
            GlobalStat.update_pacman_score(self.value)
        else:
            GlobalStat.update_dacman_score(self.value)
        return True
