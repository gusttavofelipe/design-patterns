"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""
from abc import ABC, abstractmethod


class Handle(ABC):
    @abstractmethod
    def handle_request(self, letter: str) -> str:...


class HandleABC(Handle):
    def __init__(self, sucessor: Handle) -> None:
        self.letters = ['a', 'b', 'c']
        self.sucessor = sucessor


    def handle_request(self, letter: str) -> str:
        if letter.lower() in self.letters:
            return f'{self.__class__.__name__}: tratou {letter}'
        return self.sucessor.handle_request(letter)


class HandleDEF(Handle):
    def __init__(self, sucessor: Handle) -> None:
        self.letters = ['d', 'e', 'f']
        self.sucessor = sucessor


    def handle_request(self, letter: str) -> str:
        if letter.lower() in self.letters:
            return f'{self.__class__.__name__}: tratou {letter}'
        return self.sucessor.handle_request(letter)


class HandleUnsolved(Handle):
    def handle_request(self, letter: str) -> str:
        return f'não foi possivel tratar {letter}'

if __name__ == '__main__':
    han_unsolv = HandleUnsolved()  
    han_def = HandleDEF(han_unsolv)
    han_abc = HandleABC(han_def)

    print(han_abc.handle_request('A'))
    print(han_abc.handle_request('b'))
    print(han_abc.handle_request('c'))
    print(han_abc.handle_request('d'))
    print(han_abc.handle_request('E'))
    print(han_abc.handle_request('f'))
    print(han_abc.handle_request('G'))