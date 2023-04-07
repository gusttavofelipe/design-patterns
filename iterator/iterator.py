"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.
- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si
A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterable, Iterator
from typing import Any


class MyIterator(Iterator):
    def __init__(self, collection: list[Any]) -> None:
        self.collection = collection
        self._index = 0


    def __next__(self):
        try:
            item = self.collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration
        

class MyReverseIterator(Iterator):
    def __init__(self, collection: list[Any]) -> None:
        self.collection = collection
        self._index = -1


    def __next__(self):
        try:
            item = self.collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration
        

class MyIterable(Iterable):
    def __init__(self) -> None:
        self._items: list[Any] = []
        self._iterator = MyIterator(self._items) 

    
    def add(self, *values: Any) -> None:
        for value in values:
            self._items.append(value)
        

    def reverse(self) -> Iterator:
        return MyReverseIterator(self._items)


    def __iter__(self) -> Iterator:
        return self._iterator
    

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    myiterable = MyIterable()
    reverse_iterator = MyReverseIterator(myiterable)
    myiterator = MyIterator(myiterable)

    myiterable.add('Gustavo', 'Felipe', 27, 30)
    myiterable.add('item')

    print('VALUE:', next(iter(myiterable)))

    for value in myiterable:
        print(value)

    print()

    for value in myiterable.reverse():
        print(value)
    

