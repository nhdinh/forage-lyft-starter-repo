from abstract import Engine, Battery
from car import Car


class Calliope(Car):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__(engine, battery)
