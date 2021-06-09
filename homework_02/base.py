from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 10
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"Weight: {self.weight}, status: {self.started}, fuel: {self.fuel}, consumption: {self.fuel_consumption}"

    def start(self):
        if self.started is False and self.fuel > 0:
            self.started = True
            print(f"{self.__class__.__name__} started!")
        else:
            raise exceptions.LowFuelError
        return f"Start vehicle: {self.started}"

    def move(self, distance):
        fuel_amount = distance * self.fuel_consumption
        if self.fuel < fuel_amount:
            raise exceptions.NotEnoughFuel
        self.fuel -= fuel_amount
        print(f"Total distance: {distance}, spent fuel: {fuel_amount}, left fuel: {self.fuel}")


if __name__ == '__main__':
    car = Vehicle(100, 60, 12)
    print(car)
    car.fuel = 0
    car.start()
    car.move(6)
    print(car)
