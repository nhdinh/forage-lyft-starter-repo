#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from batteries import SpindlerBattery, NubbinBattery


class TestSpindlerBattery:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        spindler = SpindlerBattery(
            last_service_date=last_service_date, current_date=today
        )
        assert spindler.needs_service() is True

    def test_battery_should_not_be_servicd(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        spindler = SpindlerBattery(
            last_service_date=last_service_date, current_date=today
        )
        assert spindler.needs_service() is False


class TestNubbinBattery:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - 5, month=today.month - 2
        )

        spindler = NubbinBattery(
            last_service_date=last_service_date, current_date=today
        )
        assert spindler.needs_service() is True

    def test_battery_should_not_be_servicd(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        spindler = NubbinBattery(
            last_service_date=last_service_date, current_date=today
        )
        assert spindler.needs_service() is False
