from abc import ABC, abstractmethod
from typing import List


class Tires(ABC):
    def __init__(self, tires_sensor_data: List[float]):
        self.tires_sensor_data = tires_sensor_data

    @abstractmethod
    def need_services(self) -> bool:
        pass
