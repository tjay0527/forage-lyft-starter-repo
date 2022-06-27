from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.nubbinBattery import NubbinBattery

class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        
        if self.needs_service():
            return True
        else:
            return False
