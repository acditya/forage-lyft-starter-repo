from abc import ABC

from Car import Car

from engine.Engine import Engine
from datetime import datetime


class SternmanEngine(Engine):
    def __init__(self):
        super().__init__(self, "Sternman")

        #Define Class Attributes
        self.warning_light_on = False

    #Override needs_service superclass abstract method
    def needs_service(self):
        if(self.warning_light_on):
            return True
        else:
            return False
