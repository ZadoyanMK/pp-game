from .Subject import Subject
import abc
import os


class Unit(Subject, abc.ABC):

    direction = 0

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)
        os.system('cls')
        return method

    @abc.abstractmethod
    def interaction(self, ob):
        pass

    def step_up(self, val):
        pass

    def step_down(self, val):
        pass

    def step_left(self, val):
        pass

    def step_right(self, val):
        pass
