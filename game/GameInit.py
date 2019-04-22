from general import Map, GlobalStat
from units import Pacman, Block, Point, Mine, Dacman
import os
from game import settings
import readchar


class GameInit:

    help_message = "Instructions"
    pacman = None
    dacman = None

    def __init__(self):
        self.pacman = Pacman()
        self.dacman = Dacman()
        self._generate_field_data()
        self.regenerate()

    def _generate_field_data(self):
        for _ in range(settings.BLOCK_COUNT):
            c = Block()
            Map.set_to_map_data(
                x=c.coord_x, y=c.coord_y,
                val=settings.BLOCK_FIELD, ob=c)

        for _ in range(settings.POINT_COUNT):
            c = Point()
            Map.set_to_map_data(
                x=c.coord_x, y=c.coord_y,
                val=settings.POINT_FIELD.format(c.value), ob=c)

        for _ in range(settings.MINE_COUNT):
            c = Mine()
            Map.set_to_map_data(
                x=c.coord_x, y=c.coord_y,
                val=settings.MINE_FIELD.format(c.value), ob=c)

    def regenerate(self):
        os.system('cls')
        print(f"Game was started!!!\n\n{self.help_message}\n")
        print(f"Pacman lives: {GlobalStat.get_lives()['pacman']}")
        print(f"Pacman score: {GlobalStat.get_score()['pacman']}\n")

        print(f"Dacman lives: {GlobalStat.get_lives()['dacman']}")
        print(f"Dacman score: {GlobalStat.get_score()['dacman']}\n")

        print(f"Points left: {GlobalStat.get_point_count()}\n\n")

        Map.set_to_map_data(
            x=self.pacman.coord_x, y=self.pacman.coord_y,
            val=settings.PACMAN_DIRECTIONS[self.pacman.direction], ob=self.pacman)

        Map.set_to_map_data(
            x=self.dacman.coord_x, y=self.dacman.coord_y,
            val=settings.DACMAN_DIRECTIONS[self.dacman.direction], ob=self.dacman)

        Map.print_map()

    def _step(self, v):
        self.pacman.move(v)
        self.dacman.move(v)

        print(v)
        self.regenerate()

    def _end_game_message(self, key=None):
        print(f'\n\nYour score: {GlobalStat.get_score()}\n\n')

    def _is_end_game(self):
        return GlobalStat.get_lives()['pacman'] == 0 \
            or GlobalStat.get_lives()['dacman'] == 0 \
            or GlobalStat.get_point_count() == 0

    def _run_pacman(self, key=None):
        while not self._is_end_game():
            try:
                v = readchar.readkey()
            except KeyboardInterrupt:
                self._end_game_message()
                return

            self._step(v)

        self._end_game_message()

    def run(self):
        self._run_pacman()

