from abc import ABC, abstractmethod
from datetime import date


class Battery(ABC):
    def __init__(self, current_date: date, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass
