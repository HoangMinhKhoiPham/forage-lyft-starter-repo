import unittest
from tire.Tires import Tires
from tire.OctoprimeTire import OctoprimeTire
from tire.CarriganTire import CarriganTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 1, 1, 1]
        tire = OctoprimeTire()
        self.assertTrue(tire.needs_service(tire_wear))

    def test_needs_service_false(self):
        tire_wear = [0, 0.5, 0.98, 1]
        tire = OctoprimeTire()
        self.assertFalse(tire.needs_service(tire_wear))


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.98, 0.99, 1]
        tire = CarriganTire()
        self.assertTrue(tire.needs_service(tire_wear))

    def test_needs_service_false(self):
        tire_wear = [0, 0.5, 0.9, 1]
        tire = CarriganTire()
        self.assertFalse(tire.needs_service(tire_wear))
