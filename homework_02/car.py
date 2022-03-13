"""
создайте класс `Car`, наследник `Vehicle`
"""
from pyparsing import null_debug_action
from base import Vehicle
from engine import Engine

class Car (Vehicle,Engine):
    # volume = 0 
    # pistons = 0
    # engine = Engine(volume,pistons)
    # engine = Engine
    def set_engine(self, Engine):
        self.engine = Engine

 