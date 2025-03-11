import abc

class FlyingObjects(metaclass=abc.ABCMeta):
    _flyingOjects = []
    def __init__(self, name):
        self._in_air = False
        self.name = name
        type(self)._flyingOjects.append(self)

    @abc.abstractmethod
    def take_off(self):
        self._in_air = True

    @abc.abstractmethod
    def land(self):
        self._in_air = False

    @classmethod
    def flying_objects(cls):
        return cls._flyingOjects
    
    def __str__(self):
        return self.name

