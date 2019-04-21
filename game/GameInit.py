from general import Map, GlobalStat
from units import Pacman, Block, Point
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
        for _ in range(settings.POINT_COUNT):
            c = Point()
            Map.set_to_map_data(
                x=c.coord_x, y=c.coord_y,
                val=settings.POINT_FIELD, ob=c)

        for _ in range(settings.BLOCK_COUNT):
            c = Block()
            Map.set_to_map_data(
                x=c.coord_x, y=c.coord_y,
                val=settings.BLOCK_FIELD, ob=c)

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

    def step(self, v):
        if v.upper() == 'W':
            self.pacman.step_up(1)
        if v.upper() == 'S':
            self.pacman.step_down(1)
        if v.upper() == 'D':
            self.pacman.step_right(1)
        if v.upper() == 'A':
            self.pacman.step_left(1)
        self.regenerate()

    def run(self):
        while True:
            v = None

            try:
                v = readchar.readkey()
            except KeyboardInterrupt:
                print("Goodbye")
                return

            self.step(v)
