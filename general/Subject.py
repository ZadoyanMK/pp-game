import abc


class Subject(metaclass=abc.ABCMeta):

    coord_x = 0
    coord_y = 0
    value = 1

    @abc.abstractmethod
    def interaction(self, ob):
        pass
