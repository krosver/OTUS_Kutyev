"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine

class Car (Vehicle,Engine):
    def set_engine(self, set_volume, set_pistons):
        self.volume = set_volume
        self.pistons = set_pistons


# test = Car(10,50,5)
# test.set_engine(7,8)
# test.start()
# test.move(5)
