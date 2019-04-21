from general import Unit, Map
from units import Block, Point


class Pacman(Unit):

    direction = 1

    def interaction(self, ob=None, x=None, y=None):
        local_x = x if x else self.coord_x
        local_y = y if y else self.coord_y

        m = Map.get_game_map()
        if not m[local_x][local_y]:
            return True

        return m[local_x][local_y].interaction(ob=self)
