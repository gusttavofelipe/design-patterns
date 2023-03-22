# Factory (Fabrica) - classe ou metodo que cria objetos
## Factory Method / Abstract Mactory

'''
Vantagens:

Permitem criar um sistema com baixo acoplamento entre classes porque
ocultam as classes que criam os objetos do código cliente.

Facilitam a adição de novas classes ao código, porque o cliente não
conhece e nem utiliza a implementação da classe (utiliza a factory).

Podem facilitar o processo de "cache" ou criação de "singletons" porque a
fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
novos objetos sempre que o cliente precisar.

Desvantagens:

Podem introduzir muitas classes no código

Simple Factory <- pode não ser considerado um padrão de projeto por si só 
Simple Factory <- pode quebrar princípios do SOLID
'''

### Simple Factory ###
  
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


class VehicleFactory: # Simple Factory 
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


if __name__ == ('__main__'): # Client code:
    available_vehicles = [
        'lux_car', 'popular_car',
        'popular_motorbike', 'lux_motorbike'
        ]

    car = VehicleFactory.get_vehicle(available_vehicles[0])
    car.get_client()

    for i in range(10):
        car = VehicleFactory.get_vehicle(choice(available_vehicles))
        car.get_client()
  