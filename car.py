from abstract import Engine, Battery, Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        if not engine or not battery:
            raise ValueError("Engine and battery are required")

        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
