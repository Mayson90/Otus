"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(self, fuel, fuel_consumption)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        cargo_amount = self.cargo + load
        if self.max_cargo < cargo_amount:
            raise exceptions.CargoOverload
        self.cargo = cargo_amount
        print(f"Max cargo: {self.max_cargo}, Load: {load}, Current cargo: {self.cargo}")

    def remove_all_cargo(self):
        cargo = self.cargo
        if self.cargo > 0:
            self.cargo = 0
        return cargo


if __name__ == '__main__':
    airbus = Plane(300, 200, 20, 400)
    airbus.cargo = 300
    airbus.load_cargo(99)
    print(airbus.cargo)
    airbus.remove_all_cargo()
    print(airbus.cargo)
