from datetime import date
from typing import List

from batteries import NubbinBattery, SpindlerBattery
from car import Car
from engine import WilloughbyEngine, SternmanEngine, CapuletEngine
from tires import OctoprimeTires, CarriganTires


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_sensor_data: List[float],
    ) -> Car:
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )

        tires = OctoprimeTires(tires_sensor_data=tires_sensor_data)

        calliope = Car(battery=battery, engine=engine, tires=tires)
        return calliope

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_sensor_data: List[float],
    ) -> Car:
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = WilloughbyEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )

        tires = OctoprimeTires(tires_sensor_data=tires_sensor_data)
        glissade = Car(battery=battery, engine=engine, tires=tires)
        return glissade

    @staticmethod
    def create_palindrome(
        current_date: date,
        last_service_date: date,
        warning_light_on: bool,
        tires_sensor_data: List[float],
    ) -> Car:
        battery = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        tires = CarriganTires(tires_sensor_data=tires_sensor_data)
        palindrome = Car(battery=battery, engine=engine, tires=tires)
        return palindrome

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_sensor_data: List[float],
    ) -> Car:
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date
        )
        engine = WilloughbyEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        tires = CarriganTires(tires_sensor_data=tires_sensor_data)
        rorschach = Car(battery=battery, engine=engine, tires=tires)
        return rorschach

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_sensor_data: List[float],
    ) -> Car:
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date
        )

        engine = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        tires = CarriganTires(tires_sensor_data=tires_sensor_data)
        thovex = Car(battery=battery, engine=engine, tires=tires)
        return thovex
