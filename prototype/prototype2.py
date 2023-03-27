'''
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
'''

### usando metodo de clonagem ###

from copy import deepcopy

class StringReprMixim:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
            )
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixim):
    def __init__(self,first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = []


    def add_address(self, address) -> None:
        self.addresses.append(address)

    # metodo de clonagem
    def clone(self):
        return deepcopy(self)


class Address(StringReprMixim):
    def __init__(self, street: str, number:str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':

    gus = Person('Gustavo', 'Felipe')
    gus_address = Address('Rua nova', '14')
    gus.add_address(gus_address)

    gus_brother = gus.clone() # metodo de clonagem
    gus_brother.first_name = 'Felipe'

    print(gus)
    print(gus_brother)