from general import FieldSubjects, GlobalStat
from random import randint
from game import settings
from .Pacman import Pacman


class Mine(FieldSubjects):

    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        self.value = randint(settings.MINE_MIN_VALUE, settings.MINE_MAX_VALUE)

    def interaction(self, ob=None, x=None, y=None):
        if isinstance(ob, Pacman):
            GlobalStat.update_pacman_lives(self.value)
        else:
            GlobalStat.update_dacman_lives(self.value)
        return True
