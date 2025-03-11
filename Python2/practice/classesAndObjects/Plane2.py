from FlyingObjects import FlyingObjects

class Plane(FlyingObjects):

    @property
    def pilot_awake(self):
        return True
    def take_off(self):
        if self.pilot_awake:
            super().take_off()
        self._in_air = True