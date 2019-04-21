from general.Map import Map
import os


class Game:

    help_message = "Instructions"

    def _init_resources(self):
        Map.generate_map()

    def run(self):
        os.system('cls')
        print(f"Game was started!!!\n\n{self.help_message}\n")

        self._init_resources()
