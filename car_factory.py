from datetime import date

from batteries import NubbinBattery, SpindlerBattery
from car import Car
from engine import WilloughbyEngine, SternmanEngine, CapuletEngine


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        calliope = Car(battery=battery, engine=engine)
        return calliope

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = WilloughbyEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        glissade = Car(battery=battery, engine=engine)
        return glissade

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date, warning_light_on: bool
    ) -> Car:
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        palindrome = Car(battery=battery, engine=engine)
        return palindrome

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = WilloughbyEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        rorschach = Car(battery=battery, engine=engine)
        return rorschach

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date
        )

        engine = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        thovex = Car(battery=battery, engine=engine)
        return thovex
