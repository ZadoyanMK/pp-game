from general import FieldSubjects, GlobalStat
from random import randint
from game import settings


class Mine(FieldSubjects):

    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        self.value = randint(settings.MINE_MIN_VALUE, settings.MINE_MAX_VALUE)

    def interaction(self, ob=None, x=None, y=None):
        GlobalStat.update_lives(self.value)
        return True
