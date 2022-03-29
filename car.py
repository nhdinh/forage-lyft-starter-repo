from abstract import Engine, Battery, Serviceable, Tires


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        if not engine or not battery:
            raise ValueError("Engine and battery are required")

        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return (
            self.engine.needs_service()
            or self.battery.needs_service()
            or self.tires.need_services()
        )
