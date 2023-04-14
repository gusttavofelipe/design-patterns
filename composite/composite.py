"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).
No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.

Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class BoxStructure(ABC):
    '''Component'''

    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    '''Composite'''

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: list[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
            ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    '''Leaf'''

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':

    # Leaf
    shirt1 = Product('black shirt', 10.0)
    shirt2 = Product('white shirt', 10.0)
    shirt3 = Product('blue shirt', 10.0)
    # shirt3.print_content()
    # shirt3.get_price()

    # omposite
    shirtbox = Box('Shirt box')
    shirtbox.add(shirt1)
    shirtbox.add(shirt2)
    shirtbox.add(shirt3)

    # shirtbox.print_content()

    # Leaf
    smartphone1 = Product('Nokia', 1000.0)
    smartphone2 = Product('Blackberry', 1000.0)
    smartphone3 = Product('motorola', 1000.0)

    smartphonebox = Box('Smartphone box')
    smartphonebox.add(smartphone1)
    smartphonebox.add(smartphone2)
    smartphonebox.add(smartphone3)

    # smartphonebox.print_content()

    bigbox = Box('Big box')
    bigbox.add(smartphonebox)
    bigbox.add(shirtbox)

    bigbox.print_content()
    print('Total price:', bigbox.get_price())
