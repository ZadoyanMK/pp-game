from general import FieldSubjects, GlobalStat
from random import randint
from game import settings


class Point(FieldSubjects):

    def interaction(self, ob=None, x=None, y=None):
        self.value = randint(settings.POINT_MIN_VALUE, settings.POINT_MAX_VALUE)

        GlobalStat.update_score(self.value)
        return True
