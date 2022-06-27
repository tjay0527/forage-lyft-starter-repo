from abc import ABC
from car import Car
from datetime import datetime
class SpindlerBattery(Car, ABC):
    def __init__(self, bat, eng,last_service_date, current_date) -> None:
        super().__init__(bat, eng)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False