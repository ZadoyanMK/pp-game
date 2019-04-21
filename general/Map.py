import numpy as np
from game.settings import FIELD_SIZE_X, FIELD_SIZE_Y, EMPTY_FIELD


class Map:

    _size_x = FIELD_SIZE_X
    _size_y = FIELD_SIZE_Y
    _value = None

    @classmethod
    def generate_map(cls):
        cls._value = []
        for _ in range(cls._size_x):
            row = []
            for j in range(cls._size_y):
                row.append(EMPTY_FIELD)

            cls._value.append(row)

    @classmethod
    def _check_map(cls):
        if cls._value is None:
            cls.generate_map()

    @classmethod
    def get_map(cls):
        cls._check_map()
        return cls._value

    @classmethod
    def set_to_map_data(cls, x=None, y=None, val=None):
        cls._check_map()
        cls._value[x][y] = f'{val}'

    @classmethod
    def print_map(cls):
        cls._check_map()
        for i in range(cls._size_x):
            for j in range(cls._size_x):
                print(cls._value[i][j], end=" ")
            print()
