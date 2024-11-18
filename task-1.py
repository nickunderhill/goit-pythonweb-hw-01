from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model + " (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model + " (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model + " (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model + " (EU Spec)")


def main():
    car_us = USVehicleFactory().create_car("Toyota", "Corolla")
    car_us.start_engine()

    car_eu = EUVehicleFactory().create_car("Volkswagen", "Golf")
    car_eu.start_engine()

    bike_us = USVehicleFactory().create_motorcycle("Harley-Davidson", "Sportster")
    bike_us.start_engine()

    bike_eu = EUVehicleFactory().create_motorcycle("Yamaha", "FZ6")
    bike_eu.start_engine()


if __name__ == "__main__":
    main()
