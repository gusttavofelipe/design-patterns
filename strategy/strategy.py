'''
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
'''

from __future__ import annotations
from abc import ABC, abstractmethod


class Order(): # contexto
    def __init__(self, total:float, discount:DiscountStrategy) -> None:
        self._total = total
        self._discount = discount


    @property
    def total(self):
        return self._total
    

    @property
    def total_discount(self):
        return self._discount.calculate(self._total)


# Abstract Strategy -> molde
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: ...


'''Famila dia algoritimos'''

# StrategyA
class TwentyPercent(DiscountStrategy): 
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)
    

# StrategyB
class FiftyPercent(DiscountStrategy): 
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


# StrategyC
class NoDiscount(DiscountStrategy): 
    def calculate(self, value: float) -> float:
        return value
    

# StrategyD
class CustomDiscount(DiscountStrategy): 
    def __init__(self, discount) -> None:
        self.discount = discount / 100
        

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)
    

if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    custom_discount = CustomDiscount(5)

    order = Order(1000, twenty_percent)
    print(order.total, order.total_discount)    

    order = Order(1000, fifty_percent)
    print(order.total, order.total_discount)

    order = Order(1000, no_discount)
    print(order.total, order.total_discount)

    order = Order(1000, custom_discount)
    print(order.total, order.total_discount)