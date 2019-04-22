from game import settings


class GlobalStat:

    _pacman_score = 0
    _dacman_score = 0

    _pacman_lives = settings.PACMAN_LIVES
    _dacman_lives = settings.DACMAN_LIVES

    _point_count = settings.POINT_COUNT

    @classmethod
    def get_score(cls):
        return {
            'dacman': cls._dacman_score,
            'pacman': cls._pacman_score
        }

    @classmethod
    def update_pacman_score(cls, v):
        cls._pacman_score += v
        cls._point_count -= 1

    @classmethod
    def update_dacman_score(cls, v):
        cls._dacman_score += v
        cls._point_count -= 1

    @classmethod
    def get_lives(cls):
        return {
            'dacman': cls._dacman_lives,
            'pacman': cls._pacman_lives
        }

    @classmethod
    def update_pacman_lives(cls, v):
        cls._pacman_lives -= v

    @classmethod
    def update_dacman_lives(cls, v):
        cls._dacman_lives -= v

    @classmethod
    def get_point_count(cls):
        return cls._point_count
