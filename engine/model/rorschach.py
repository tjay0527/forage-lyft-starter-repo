from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from engine.nubbinBattery import NubbinBattery

class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        
        if self.needs_service():
            return True
        else:
            return False
