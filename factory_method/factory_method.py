
'''Factory method é um padrão de criação que permite definir uma interface/
clsse abstrata para criar objetos, mas deixa as subclasses decidirem
quais objetos criar. O Factory method permite adiar a instanciação para as
subclasses, garantindo o baixo acoplamento entre classes.'''

##### Factory method #####
  
from abc import ABC, abstractmethod
from random import choice


class Vehicle(ABC): # Product (molde)
    @abstractmethod
    def get_client(self) -> None:
        ...


class LuxuryCar(Vehicle): # ConcreteProduct1 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury car went to pick up the customer...')


class PopularCar(Vehicle): # ConcreteProduct2 (feito do molde)
    def  get_client(self) -> None:
        print('Popular car went to pick up the customer...')


class PopularMotorbike(Vehicle): # ConcreteProduct3 (feito do molde)
    def  get_client(self) -> None:
        print('Popular Motorbike went to pick up the customer...')


class LuxuryMotorbike(Vehicle): # ConcreteProduct4 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury motorbike went to pick up the customer...')


# Creator
class VehicleFactory(ABC): # -> empresa:
    def __init__(self, type) -> None:
        self.vehicle = self.get_vehicle(type)

    @staticmethod
    @abstractmethod # >>Factory Method<<
    def get_vehicle(type: str) -> Vehicle: 
        ...
    
    def get_client(self):
        self.vehicle.get_client()


# Concrete Creator
class NorthZoneVehicleFactory(VehicleFactory): # -> filial

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

# Concrete Creator
class SouthZoneVehicleFactory(VehicleFactory): # -> filial

    @staticmethod
    def get_vehicle(type: str) -> Vehicle:
        if type == 'popular_car':
            return PopularCar()
        assert 0, 'Vehicle doesnt exists'
    
    def get_client(self):
        self.vehicle.get_client()


if __name__ == ('__main__'): # Client code:
    availab_vehicles_nz = [
        'lux_car', 'popular_car',
        'popular_motorbike','lux_motorbike'
        ]
    availab_vehicles_sz = ['popular_car']
    

    print('NORTH ZONE')
    for i in range(10):
        car = NorthZoneVehicleFactory(choice(availab_vehicles_nz))
        car.get_client()

    print()
  
    print('SOUTH ZONE')
    for i in range(10):
        sz_car = NorthZoneVehicleFactory(choice(availab_vehicles_sz))
        sz_car.get_client()