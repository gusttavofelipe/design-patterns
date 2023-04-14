"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.
Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:
- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.
Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;
Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""

# sem Abastract Flyweight (interface)
from __future__ import annotations


class Client:
    '''Context'''

    def __init__(self, name: str) -> None:
        self._name = name
        self._addresses: list = []

        # extrinsic addresses data
        self.address_number: str
        self.address_detail: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(
                self.address_number, self.address_detail
                )


class Address:
    '''Flyweight Object'''

    def __init__(self, street: str, neighbourhood: str, zipcode: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zipcode = zipcode

    def show_address(self, address_number: str, address_detail: str) -> None:
        print(
            self._street, address_number, self._neighbourhood,
            address_detail, self._zipcode
            )


class AddressFactory:
    '''Flyweight Factory'''

    _address: dict = {}  # Flyweight Poll

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._address[key]
            print('USANDO OBJETO JA CRIADO')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._address[key] = address_flyweight
            print('CRIANDO NOVO OBJETO')

        return address_flyweight


if __name__ == '__main__':
    factory = AddressFactory()

    address1 = factory.get_address(
        street='street A',
        neighbourhood='Angelim',
        zipcode='000000-000'
    )

    address2 = factory.get_address(
        street='street A',
        neighbourhood='Angelim',
        zipcode='000000-000'
    )

    gustavo = Client('Gustavo')
    gustavo.address_number = '50'
    gustavo.address_detail = 'Casa'
    gustavo.add_address(address1)
    gustavo.list_addresses()

    marco = Client('Gustavo')
    marco.address_number = '250B'
    marco.address_detail = 'AP 310'
    marco.add_address(address2)
    marco.list_addresses()

    print(address1 == address2)
