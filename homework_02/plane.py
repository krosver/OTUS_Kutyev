"""
создайте класс `Plane`, наследник `Vehicle`
"""
from plistlib import load
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0 
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption,max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo=max_cargo
    
    def load_cargo(self,load_weight):
        try:
            if (self.cargo + load_weight <= self.max_cargo):
                self.cargo += load_weight
            else:   
                raise CargoOverload()
        except CargoOverload:
            print("Перегружен!\n")
    
    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo 


