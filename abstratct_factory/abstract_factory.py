
'''Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança para criar objetos, enquanto Abstract Factory
usa a composição.

Princípio: programe para interfaces, não para implementações'''

##### Abstract Method #####
  
from abc import ABC, abstractmethod
from random import choice


# Contrato/Familia p veiculos de luxo
# Abstract Factory - Interface
class LuxuryVehicle(ABC): # Product (molde)
    @abstractmethod
    def get_client(self) -> None:
        ...

# Contrato/Familia p veiculos populares
# Abstract Factory - Interface
class PopularVehicle(ABC): # Product (molde)
    @abstractmethod
    def get_client(self) -> None:
        ...


## North Zone Vehicles
class NzLuxuryCar(LuxuryVehicle): # ConcreteProduct1 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury car ZN went to pick up the customer...')


class NzPopularCar(PopularVehicle): # ConcreteProduct2 (feito do molde)
    def  get_client(self) -> None:
        print('Popular car ZN went to pick up the customer...')


class NzPopularMotorbike(PopularVehicle): # ConcreteProduct3 (feito do molde)
    def  get_client(self) -> None:
        print('Popular Motorbike ZN went to pick up the customer...')


class NzLuxuryMotorbike(LuxuryVehicle): # ConcreteProduct4 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury motorbike ZN went to pick up the customer...')


## South Zone Vehicles
class SzLuxuryCar(LuxuryVehicle): # ConcreteProduct1 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury car SZ went to pick up the customer...')


class SzPopularCar(PopularVehicle): # ConcreteProduct2 (feito do molde)
    def  get_client(self) -> None:
        print('Popular car SZ went to pick up the customer...')


class SzPopularMotorbike(PopularVehicle): # ConcreteProduct3 (feito do molde)
    def  get_client(self) -> None:
        print('Popular Motorbike SZ went to pick up the customer...')


class SzLuxuryMotorbike(LuxuryVehicle): # ConcreteProduct4 (feito do molde)
    def  get_client(self) -> None:
        print('Luxury motorbike SZ went to pick up the customer...')

# Creator
# Abstract Factory - Interface
class VehicleFactory(ABC): # -> empresa:

    @staticmethod
    @abstractmethod # >>Factory Method<<
    def get_popular_car() -> PopularVehicle: pass


    @staticmethod
    @abstractmethod # >>Factory Method<<
    def get_luxury_car() -> LuxuryVehicle: pass


    @staticmethod
    @abstractmethod # >>Factory Method<<
    def get_popular_motorbike() -> PopularVehicle: pass


    @staticmethod
    @abstractmethod # >>Factory Method<<
    def get_luxury_motorbike() -> LuxuryVehicle: pass
        

# Concrete Creator
class NZVehicleFactory(VehicleFactory): # -> filial

    @staticmethod
    def get_popular_car() -> PopularVehicle: 
        return NzPopularCar

    @staticmethod
    def get_luxury_car() -> LuxuryVehicle: 
        return NzLuxuryCar

    @staticmethod
    def get_popular_motorbike() -> PopularVehicle: 
        return NzPopularMotorbike
    

    @staticmethod
    def get_luxury_motorbike() -> LuxuryVehicle: 
        return NzLuxuryMotorbike


    def get_client(self):
        self.vehicle.get_client()

# Concrete Creator
class SZVehicleFactory(VehicleFactory): # -> filial

    @staticmethod
    def get_popular_car() -> PopularVehicle: 
        return SzPopularCar

    @staticmethod
    def get_luxury_car() -> LuxuryVehicle: 
        return SzLuxuryCar

    @staticmethod
    def get_popular_motorbike() -> PopularVehicle: 
        return SzPopularMotorbike
    

    @staticmethod
    def get_luxury_motorbike() -> LuxuryVehicle: 
        return SzLuxuryMotorbike
    
    def get_client(self):
        self.vehicle.get_client()


class Client:
    def get_clients(self) -> None:
        # Composição ( de outras factorys)
        for factory in [NZVehicleFactory(), SZVehicleFactory()]:
            popular_car = factory.get_popular_car() 
            popular_car.get_client(self)  

            lux_car = factory.get_luxury_car() 
            lux_car.get_client(self)  

            popular_motorbike = factory.get_popular_motorbike() 
            popular_motorbike.get_client(self)  

            lux_motorbike = factory.get_luxury_motorbike() 
            lux_motorbike.get_client(self)  

            
if __name__ == ('__main__'): # Client code:
    client = Client()
    client.get_clients()