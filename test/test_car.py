import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is False

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        bad_octoprime_data = [0.9, 0.26, 0.95, 0.9]

        car = CarFactory.create_calliope(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=bad_octoprime_data,
        )
        assert car.needs_service() is True


class TestGlissade:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        good_octoprime_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_octoprime_data,
        )
        assert car.needs_service() is False

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        bad_octoprime_data = [0.9, 0.26, 0.95, 0.9]

        car = CarFactory.create_glissade(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=bad_octoprime_data,
        )
        assert car.needs_service() is True


class TestPalindrome:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is False

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        bad_carrigan_data = [0.9, 0.2, 0.3, 0.4]

        car = CarFactory.create_palindrome(
            current_date=today,
            last_service_date=last_service_date,
            warning_light_on=warning_light_is_on,
            tires_sensor_data=bad_carrigan_data,
        )
        assert car.needs_service() is True


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is False

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        bad_carrigan_data = [0.1, 0.96, 0.3, 0.4]

        car = CarFactory.create_rorschach(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=bad_carrigan_data,
        )
        assert car.needs_service() is True


class TestThovex:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is True

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is False

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is True

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        good_carrigan_data = [0.1, 0.2, 0.3, 0.4]

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=good_carrigan_data,
        )
        assert car.needs_service() is False

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        bad_carrigan_data = [0.9, 0.2, 0.3, 0.4]

        car = CarFactory.create_thovex(
            current_date=today,
            last_service_date=last_service_date,
            current_mileage=current_mileage,
            last_service_mileage=last_service_mileage,
            tires_sensor_data=bad_carrigan_data,
        )
        assert car.needs_service() is True
