"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.

Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python
Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.

Do livro "Python Fluente", por Luciano Ramalho (pág. 223)
"""
from dataclasses import dataclass
from copy import deepcopy


# INGREDIENTS:
# "Component" for the decorator
@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.0


@dataclass
class Bacon(Ingredient):
    price: float = 7.50


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class PotatoSticks(Ingredient):
    price: float = 3.45


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class Cheese(Ingredient):
    price: float = 5.0


# HOTDOGS:
# "ConcreteComponent" for the decorator
class Hotdog:
    _name: str
    _ingredients: list[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self.ingredients}'


class SimpleHotDog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotDog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class EspecialHotDog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'EspecialHotDog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            PotatoSticks(),
            MashedPotatoes(),
            Cheese()
        ]


# DECORATORS
class HotDogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self.hotdog.ingredients


class BaconDecorator(HotDogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients


if __name__ == '__main__':
    simplehotdog = SimpleHotDog()
    print(simplehotdog)

    decorated_simphotdog = HotDogDecorator(simplehotdog)
    print(decorated_simphotdog)

    bacon_simphotdog = BaconDecorator(simplehotdog)
    print(bacon_simphotdog)

    # é possivel redecorar quantas vezes quiser
    bacon_simphotdog = BaconDecorator(bacon_simphotdog)
    print(bacon_simphotdog)
