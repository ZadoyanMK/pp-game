from general import Unit


class Pacman(Unit):

    direction = 1
    coord_y = 0
    coord_x = 0

    def move(self, v):
        if v.upper() == 'W':
            self.step_up(1)
        if v.upper() == 'S':
            self.step_down(1)
        if v.upper() == 'D':
            self.step_right(1)
        if v.upper() == 'A':
            self.step_left(1)
