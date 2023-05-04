from tire.Tires import Tires

class OctoprimeTire(Tires):
    def __int__(self, tire_wear):
        super.__init__()
        self.tire_wear = tire_wear

    def needs_service(self, tire_wear: list[float]) -> bool:
        wear = sum(tire_wear)
        if wear >= 3:
            return True
        return False
