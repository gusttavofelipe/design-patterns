"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from abc import ABC, abstractmethod


class Collegue(ABC): ## Collegue
    def __init__(self) -> None:
        self.name: str


    @abstractmethod
    def broadcast(self, msg: str) -> None:...

    @abstractmethod
    def direct(self, msg: str) -> None:...


class Mediator(ABC): ## Mediator
    @abstractmethod
    def broadcast(self, collegue: Collegue, msg: str) -> None:...

    @abstractmethod
    def direct(self, sender: Collegue, reciever: str, msg: str) -> None:...


class Person(Collegue): ## ConcreteCollegue
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator
    

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)
    

    def send_direct(self, reciever: Collegue, msg: str):
        self.mediator.direct(self, reciever,  msg)


    def direct(self, msg: str) -> None:
        print(msg)


class ChatRoom(Mediator): ## ConcreteMediator
    def __init__(self) -> None:
        self.collegues: list[Collegue] = []

    
    def is_collegue(self, collegue: Collegue) -> bool:
        return collegue in self.collegues


    def acept(self, collegue: Collegue) -> None:
        if not self.is_collegue(collegue):
            self.collegues.append(collegue)
        

    def remove(self, collegue: Collegue) -> None:
        if self.is_collegue:
            self.collegues.remove(collegue)
    

    def broadcast(self, collegue: Collegue, msg: str) -> None:
        if not self.is_collegue(collegue):
            return
        print(f'{collegue.name} disse: "{msg}"')

    
    def direct(self, sender: Collegue, reciever: str, msg: str) -> None:
        if not self.is_collegue(sender):
            return
        
        reciever_obj: list[Collegue] = [
            collegue for collegue in self.collegues
            if collegue.name == reciever
            ]

        if not reciever:
            return
        reciever_obj[0].direct(
            f'{sender.name} para {reciever_obj[0].name}: "{msg}"'
        )


if __name__ == '__main__':
    chat = ChatRoom()

    rivaldo = Person('Rivaldo', chat)
    yan = Person('Yan', chat)
    rodrigo = Person('Rodrigo', chat)
    gustavo = Person('Gustavo', chat)

    chat.acept(rivaldo)
    chat.acept(yan)
    chat.acept(rodrigo)
    chat.acept(gustavo)

    gustavo.broadcast('Hi')
    rodrigo.broadcast('Hello')
    yan.broadcast('Hi guys')

    print()

    rivaldo.send_direct(rodrigo.name, 'Hello  friend')
    rodrigo.send_direct(rivaldo.name, 'Hi bro')