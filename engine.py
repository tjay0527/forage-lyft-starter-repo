from abc import ABC, abstractmethod
from car import Car

class Engine(Car, ABC):
    def __init__(self, eng):
        super().__init__(eng)

    @abstractmethod
    def needs_service(self):
        pass