from .Subject import Subject
import abc
import os
from game import settings


class Unit(Subject):

    direction = 0
    max_directions = 4

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)
        # os.system('cls')
        return method

    def step_up(self, val):
        self.direction = settings.DIRECTIONS['up']

    def step_down(self, val):
        self.direction = settings.DIRECTIONS['down']

    def step_left(self, val):
        self.direction = settings.DIRECTIONS['left']

    def step_right(self, val):
        self.direction = settings.DIRECTIONS['right']
