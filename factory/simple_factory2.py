# Factory (Fabrica) - classe ou metodo que cria objetos
## Factory Method / Abstract Mactory

##### Simple Factory - retornando a propria Factory#####
  
from abc import ABC, abstractmethod
from random import choice


class Vehicle(ABC): # Product (molde)
    @abstractmethod
    def get_client(self) -> None:
        ...


class LuxuryCar(Vehicle): # ConcretProduct1 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury car went to pick up the customer...')


class PopularCar(Vehicle): # ConcretProduct2 (feito do molde)
    def  get_client(self) -> None:
        print('Popular car went to pick up the customer...')


class PopularMotorbike(Vehicle): # ConcretProduct3 (feito do molde)
    def  get_client(self) -> None:
        print('Popular Motorbike went to pick up the customer...')


class LuxuryMotorbike(Vehicle): # ConcretProduct3 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury motorbike went to pick up the customer...')


# Simple Factory - retornando a propria Factory:
# a factory envolve o objeto
class VehicleFactory: 
    def __init__(self, type) -> None:
        self.vehicle = self.get_vehicle(type)

    @staticmethod
    def get_vehicle(type: str) -> Vehicle:
        if type == 'lux_car':
            return LuxuryCar()
        if type == 'popular_car':
            return PopularCar()
        if type == 'popular_motorbike':
            return PopularMotorbike()
        if type == 'lux_motorbike':
            return LuxuryMotorbike()
        assert 0, 'Vehicle doesnt exists'

    
    def get_client(self):
        self.vehicle.get_client()


if __name__ == ('__main__'): # Client code
    available_vehicles = [
        'lux_car', 'popular_car',
        'popular_motorbike', 'lux_motorbike'
        ]
    
    # retornando(instanciando) instancia da propria Factory  
    car = VehicleFactory(available_vehicles[0])
    car.get_client()

    for i in range(10):
        car = VehicleFactory(choice(available_vehicles))
        car.get_client()
  