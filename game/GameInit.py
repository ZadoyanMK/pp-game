from general import Map, GlobalStat
from units import Pacman, Block, Point, Mine
import os
from game import settings
import readchar


class GameInit:

    help_message = "Instructions"
    pacman = None

    def __init__(self):
        self.pacman = Pacman()
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
        print(f"Lives: {GlobalStat.get_lives()}")
        print(f"Score: {GlobalStat.get_score()}")
        print(f"Points left: {GlobalStat.get_point_count()}\n\n")

        Map.set_to_map_data(
            x=self.pacman.coord_x, y=self.pacman.coord_y,
            val=settings.PACMAN_DIRECTIONS[self.pacman.direction], ob=self.pacman)

        Map.print_map()

    def _step(self, v):
        if v.upper() == 'W':
            self.pacman.step_up(1)
        if v.upper() == 'S':
            self.pacman.step_down(1)
        if v.upper() == 'D':
            self.pacman.step_right(1)
        if v.upper() == 'A':
            self.pacman.step_left(1)
        self.regenerate()

    def _end_game_message(self, key=None):
        print(f'\n\nYour score: {GlobalStat.get_score()}\n\n')

    def _run_pacman(self, key=None):
        while GlobalStat.get_lives() > 0 and GlobalStat.get_point_count() > 0:
            try:
                v = readchar.readkey()
            except KeyboardInterrupt:
                self._end_game_message()
                return

            self._step(v)

        self._end_game_message()

    def run(self):
        self._run_pacman()

