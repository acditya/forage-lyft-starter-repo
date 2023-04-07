
class Car:
    def __init__(self, battery, engine, carType):
        self.battery = battery
        self.engine = engine
        self.carType = carType

    def needs_service(self):
        if(self.engine.needs_service() | self.battery.needs_service()):
            return True
        else:
            return False
