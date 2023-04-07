from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine

from battery import NubinBattery
from battery import SpindlerBattery

import Car

class CarFactory:
    def create_calliope(self):
        batt = SpindlerBattery()
        eng = CapuletEngine()

        return Car(batt, eng, "Calliope")

    def create_glissade(self):
        batt = SpindlerBattery()
        eng = WilloughbyEngine()

        return Car(batt, eng, "Glissade")

    def create_palindrome(self):
        batt = SpindlerBattery()
        eng = SternmanEngine()

        return Car(batt, eng, "Palindrome")

    def create_rorscach(self):
        batt = NubinBattery()
        eng = WilloughbyEngine()

        return Car(batt, eng, "Rorscach")

    def create_thovex(self):
        batt = NubinBattery()
        eng = CapuletEngine()

        return Car(batt, eng, "Thovex")
