from typing import List

from abstract.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires_sensor_data: List[float]):
        super().__init__(tires_sensor_data)

    def need_services(self) -> bool:
        return any([d for d in self.tires_sensor_data if d >= 0.9])
