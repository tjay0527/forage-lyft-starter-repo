from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.spindlerBattery import SpindlerBattery
class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        
        if self.needs_service():
            return True
        else:
            return False
