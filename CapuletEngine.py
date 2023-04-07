from abc import ABC

from Car import Car
from engine.Engine import Engine
from datetime import datetime


class CapuletEngine(Engine):
    def __init__(self):
        super().__init__(self, "Capulet")

        #Define Class Attributes
        self.last_service_mileage = 0
        self.current_mileage = 0

    #Override needs_service superclass abstract method
    def needs_service(self):
        if(self.current_mileage - self.last_service_mileage >= 30000):
            return True
        else:
            return False

