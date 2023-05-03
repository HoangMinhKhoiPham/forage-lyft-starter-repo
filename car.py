from abc import abstractmethod
from Serviceable import Serviceable
from Battery.Battery import Battery
from engine.engine import Engine


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self._engine.need_service() or self._battery.need_service()
