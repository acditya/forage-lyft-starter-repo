from datetime import datetime

from battery.Battery import Battery

class SpindlerBattery(Battery):
    def __init__(self):
        super().__init__(self, "Spindler")
        self.last_service_date = datetime.today()
        self.current_date = datetime.today()

    #Override superclass abstract needs_service method
    def needs_service(self):
        #Convert Date Difference to Num of Days
        days = self.current_date - self.last_service_date
        if((days.total_seconds()/86400) >= 730):
            return True
        else:
            return False
