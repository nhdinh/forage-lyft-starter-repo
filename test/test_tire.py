from tires import CarriganTires, OctoprimeTires


class TestCarriganTires:
    def test_tire_should_be_serviced(self):
        carrigan_tires = CarriganTires(tires_sensor_data=[0.1, 0.2, 0.9, 0.8])
        assert carrigan_tires.need_services() is True

        carrigan_tires = CarriganTires(tires_sensor_data=[0.91, 0.2, 0.3, 0.8])
        assert carrigan_tires.need_services() is True

        carrigan_tires = CarriganTires(
            tires_sensor_data=[0.31, 0.92, 0.3, 0.8]
        )
        assert carrigan_tires.need_services() is True

        carrigan_tires = CarriganTires(
            tires_sensor_data=[0.31, 0.42, 0.3, 0.98]
        )
        assert carrigan_tires.need_services() is True

    def test_tire_should_not_be_serviced(self):
        carrigan_tires = CarriganTires(tires_sensor_data=[0.1, 0.2, 0.3, 0.4])
        assert carrigan_tires.need_services() is False


class TestOctoprimeTires:
    def test_tire_should_be_serviced(self):
        octoprime_tires = OctoprimeTires(
            tires_sensor_data=[0.9, 0.9, 0.9, 0.8]
        )
        assert octoprime_tires.need_services() is True

    def test_tire_should_not_be_serviced(self):
        octoprime_tires = OctoprimeTires(
            tires_sensor_data=[0.1, 0.2, 0.3, 0.4]
        )
        assert octoprime_tires.need_services() is False
