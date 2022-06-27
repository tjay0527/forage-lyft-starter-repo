from datetime import datetime

from engine.sternman_engine import SternmanEngine
from engine.spindlerBattery import SpindlerBattery

class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        
        if self.needs_service:
            return True
        else:
            return False
