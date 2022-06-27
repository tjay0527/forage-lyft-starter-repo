from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from engine.spindlerBattery import SpindlerBattery

class Glissade(WilloughbyEngine,SpindlerBattery):
    def needs_service(self):
        
        if self.needs_service():
            return True
        else:
            return False
