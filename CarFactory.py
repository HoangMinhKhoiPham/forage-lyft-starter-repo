from abc import ABC
from car import Car
from engine.capulet_engine import CapuletEngine
from Battery.SplindlerBattery import SplindlerBattery
from engine.willoughby_engine import WilloughbyEngine
from Battery.NubbinBattery import NubbinBattery
from engine.sternman_engine import SternmanEngine
from tire.Tires import Tires
from tire.OctoprimeTire import OctoprimeTire
from tire.CarriganTire import CarriganTire

class CarFactory(Car, ABC):
    def __int__(self) -> None:
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage, )
        battery = SplindlerBattery(current_date=current_date, last_service_date=last_service_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SplindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, tire_wear) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        battery = SplindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

