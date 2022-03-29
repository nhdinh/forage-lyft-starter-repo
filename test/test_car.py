import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False


class TestGlissade:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False


class TestPalindrome:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
        )
        assert car.needs_service() is False


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False


class TestThovex:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
        )
        assert car.needs_service() is False
