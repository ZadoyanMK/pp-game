import numpy as np


class GlobalGameData:

    points = 0
    field = np.zeros((10, 10), dtype=str)

    @classmethod
    def set_field(cls, field):
        cls.field = field

    @classmethod
    def get_field(cls):

        return cls.field

    @classmethod
    def get_points(cls):
        return cls.points

    @classmethod
    def update_points(cls, p):
        cls.points += p
