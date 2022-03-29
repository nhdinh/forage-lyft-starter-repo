from typing import List

from abstract.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires_sensor_data: List[float]):
        super().__init__(tires_sensor_data)

    def need_services(self) -> bool:
        return sum(self.tires_sensor_data) >= 3.0
