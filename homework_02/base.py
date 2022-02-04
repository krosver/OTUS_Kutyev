from abc import ABC
from exceptions import LowFuelError,NotEnoughFuel

class Vehicle(ABC):
    weight= 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption

    
    def start (self):
        try:
            if (self.started == False):
                if (self.fuel > 0):
                    self.started=True
                else:
                    raise LowFuelError()
        except LowFuelError:
            print("Нет топлива в баке!\n")
            

    def move (self, distance):
        try:
            if (self.fuel_consumption * distance <= self.fuel):
                self.fuel -= self.fuel_consumption * distance
                print(f"Оставшееся топливо {self.fuel}")
            else:
                raise NotEnoughFuel()
        except NotEnoughFuel:
            print("Недостаточно топлива в баке!\n")
            


