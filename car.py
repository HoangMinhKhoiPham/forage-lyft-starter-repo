from abc import abstractmethod
from Serviceable import Serviceable
from Battery.Battery import Battery
from engine.engine import Engine
from tire.Tires import Tires


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tires):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    @abstractmethod
    def needs_service(self):
        return self._engine.need_service() or self._battery.need_service() or self._tire.need_servce(self.tire.tire_wear)

