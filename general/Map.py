import numpy as np
from game.settings import FIELD_SIZE_X, FIELD_SIZE_Y


class Map:

    size_x = FIELD_SIZE_X
    size_y = FIELD_SIZE_Y
    value = None

    @classmethod
    def generate_map(cls):
        cls.value = np.zeros((cls.size_x, cls.size_y), dtype=str)

        for i in range(cls.size_x):
            for j in range(cls.size_y):
                cls.value[i, j] = " " * 3
        print(cls.value)
