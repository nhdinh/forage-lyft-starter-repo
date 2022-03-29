from datetime import datetime

from abstract import Battery, Engine
from car import Car


class Thovex(Car):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__(engine, battery)
        self.last_service_date = datetime.today().date()
