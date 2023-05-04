from abc import ABC
from typing import List
from tire.Tires import Tires

class CarriganTire():
    def __int__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self, tire_wear: list[float]):
        for wear in tire_wear:
            if wear >= 0.9:
                return True
            return False
