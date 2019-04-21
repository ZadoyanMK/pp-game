import readchar
from .GlobalGameData import GlobalGameData


class Game(object):

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)

        GlobalGameData.update_points(1)
        print(GlobalGameData.get_points())

        return method

    def test(self):
        print(GlobalGameData.get_field())
        print("Increase")

    def run(self):
        print("Game starts!")
        while True:
            try:
                input_move = readchar.readkey()  # input("> ")
            except (EOFError, KeyboardInterrupt):
                print("Game over!")
                return

            print(input_move)
            print("-" * 5)

            self.test()

            if input_move == 'q':
                return
