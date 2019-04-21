from game import settings


class GlobalStat:

    _score = 0
    _lives = settings.PACMAN_LIVES
    _point_list = list()

    @classmethod
    def get_score(cls):
        return cls._score

    @classmethod
    def update_score(cls, v):
        cls._score += v

    @classmethod
    def get_lives(cls):
        return cls._lives

    @classmethod
    def update_lives(cls, v):
        cls._lives -= v
