from abc import ABC, abstractmethod
from car import Car


class Batter(Car, ABC):
    def __init__(self, bat):
        super().__init__(bat)
        
    @abstractmethod
    def needs_service(self):
        pass