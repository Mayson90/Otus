from homework_02.engine import Engine
from homework_02.base import Vehicle

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):
    engine = Engine(2, 4)

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(self, fuel, fuel_consumption)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(self, engine):
        self.engine = engine


if __name__ == '__main__':
    freelander = Car(2000, 60, 10, )
    print("Engine volume:", freelander.engine.volume, "Engine pistons:", freelander.engine.pistons)
