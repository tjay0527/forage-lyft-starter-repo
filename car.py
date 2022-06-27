from abc import ABC, abstractmethod
from battery import Batter
from serviceable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self, bat, eng) -> None:
        super().__init__(self, bat, eng)
        self.battery = bat
        self.engine = eng

