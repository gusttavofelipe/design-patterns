"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.
Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from copy import deepcopy
from typing import Any


class Memento: ## Memento
    def __init__(self, state: dict) -> None:
        self._state: dict
        super().__setattr__('_state', state)

    def get_state(self) -> dict:
        return self._state
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError('This class is immutable')
    

class ImageEditor: ## Originator
    def __init__(self, name: str, width: int, height: int) -> None:
        # state
        self.name = name
        self.width = width
        self.height = height
    

    def save_state(self) -> None:
        return Memento(deepcopy(self.__dict__))
    

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()
    

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    

## Command sem interface
class Caretaker:  ## Caretaker
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: list[Memento] = []

    
    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())


    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    img1 = ImageEditor('picture1.jpg', 1, 1)
    caretaker = Caretaker(img1)
    caretaker.backup()

    img1.name = 'picture2.jpg'
    img1.width = 2
    img1.height = 2
    caretaker.backup()

    img1.name = 'picture3.jpg'
    img1.width = 3
    img1.height = 3
    caretaker.backup()

    img1.name = 'picture4.jpg'
    img1.width = 4
    img1.height = 4
    caretaker.backup()
    
    img1.name = 'picture5.jpg'
    img1.width = 5
    img1.height = 5
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()

    print(img1)
