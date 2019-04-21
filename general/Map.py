import numpy as np
from game.settings import FIELD_SIZE_X, FIELD_SIZE_Y, EMPTY_FIELD


class Map:

    _size_x = FIELD_SIZE_X
    _size_y = FIELD_SIZE_Y
    _display_map = None
    _game_map = None

    @classmethod
    def generate_map(cls):
        cls._display_map = []
        cls._game_map = []
        for _ in range(cls._size_x):
            row_display = []
            row_game = []
            for j in range(cls._size_y):
                row_display.append(EMPTY_FIELD)
                row_game.append(None)

            cls._display_map.append(row_display)
            cls._game_map.append(row_game)

    @classmethod
    def _check_map(cls):
        if cls._display_map is None:
            cls.generate_map()

    @classmethod
    def get_display_map(cls):
        cls._check_map()
        return cls._display_map

    @classmethod
    def get_game_map(cls):
        cls._check_map()
        return cls._game_map

    @classmethod
    def set_to_map_data(cls, x=None, y=None, val=None, ob=None):
        cls._check_map()
        cls._display_map[x][y] = f'{val}'
        cls._game_map[x][y] = ob

    @classmethod
    def print_map(cls):
        cls._check_map()
        for i in range(cls._size_x):
            for j in range(cls._size_x):
                print(cls._display_map[i][j], end=" ")
            print()
