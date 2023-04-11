
'''
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos (method chaining).
'''

from abc import ABC, abstractmethod


class StringReprMixim:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
            )
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__


class User(StringReprMixim): # Product
    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC): # Builder
    @property
    @abstractmethod
    def result(self):...


    @abstractmethod
    def add_firstname(self, first_name):...


    @abstractmethod
    def add_last_name(self, last_name):...


    @abstractmethod
    def add_age(self, age):...


    @abstractmethod
    def add_phone(self, phone):...


    @abstractmethod
    def add_addresses(self, addresses):...


class UserBuilder(IUserBuilder): # ConcreteBuilder
    def __init__(self) -> None:
        self.reset()


    def reset(self):
        self._result = User()


    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    '''RETORNAR self PARA ACEITAR method chaining'''
    def add_firstname(self, first_name):
        self._result.first_name = first_name
        return self


    def add_last_name(self, last_name):
        self._result.last_name = last_name
        return self


    def add_age(self, age):
        self._result.age = age
        return self


    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)
        return self


    def add_addresses(self, address):
        self._result.addresses.append(address)
        return self


# ultiliza um Builder
class UserDirector: # Director
    def __init__(self, builder):
        self._builder: UserBuilder = builder


    def with_age(self, first_name, last_name, age):
        # encadeamento de metodos (method chaining)
        self._builder.add_firstname(first_name)\
        .add_last_name(last_name).add_age(age)
        return self._builder.result
    

    def with_address(self, first_name, last_name, address):
        # encadeamento de metodos (method chaining)
        self._builder.add_firstname(first_name)\
        .add_last_name(last_name).add_addresses(address)
        return self._builder.result
    

if __name__ == '__main__':
        user_builder = UserBuilder()
        user_director = UserDirector(user_builder)
        user1 = user_director.with_age('Gustavo', 'Silva', 18)
        print(user1)

        user2 = user_director.with_address('Felipe', 'Costa', 'Santa Ines')
        print(user2)