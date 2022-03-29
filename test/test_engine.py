#!/usr/bin/env python
# -*- coding: utf-8 -*-
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class TestCapuletEngine:
    def test_engine_should_be_serviced(self):
        current_mileage = 40001
        last_service_mileage = 10000
        engine = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert engine.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 10001
        engine = CapuletEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert engine.needs_service() is False


class TestWilloughbyEngine:
    def test_engine_should_be_serviced(self):
        current_mileage = 70001
        last_service_mileage = 10000
        engine = WilloughbyEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert engine.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 10001
        engine = WilloughbyEngine(
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert engine.needs_service() is False


class TestSternmanEngine:
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        assert engine.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        assert engine.needs_service() is False
