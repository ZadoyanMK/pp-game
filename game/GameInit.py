from general.Map import Map
from units import Pacman
import os
from game import settings
import readchar


class GameInit:

    help_message = "Instructions"
    pacman = None

    def __init__(self):
        self.regenerate()

    def regenerate(self):
        os.system('cls')
        print(f"Game was started!!!\n\n{self.help_message}\n")

        self.pacman = Pacman()

        Map.set_to_map_data(
            x=self.pacman.coord_x, y=self.pacman.coord_y,
            val=settings.PACMAN_DIRECTIONS[self.pacman.direction])

        Map.print_map()

    def step(self, v):
        if v.capitalize() == 'W':
            print('up')
            self.pacman.step_up(1)
        if v.capitalize() == 'S':
            self.pacman.step_down(1)
        if v.capitalize() == 'D':
            self.pacman.step_right(1)
        if v.capitalize() == 'A':
            self.pacman.step_left(1)

        self.regenerate()
        print(settings.PACMAN_DIRECTIONS[self.pacman.direction])
        print(self.pacman.direction)

    def run(self):
        while True:
            v = None
            try:
                v = readchar.readkey()
            except KeyboardInterrupt:
                print("Goodbye")
                return

            self.step(v)
            print(v.capitalize())
