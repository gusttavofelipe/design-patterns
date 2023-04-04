'''
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You.'
11 (IOC Inversão de controle)
'''
from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self): ## template method
        global class_name
        class_name = self.__class__.__name__

        self.add_ingredients() # Abstract
        self.cook() # Abstract
        self.cut() # Final
        self.hook_before_serve() # Hook
        self.serve() # Final
        self.hook_after_serve() # Hook


    def hook_before_serve(self):...


    def hook_after_serve(self):...


    @abstractmethod
    def add_ingredients(self): ...    


    @abstractmethod
    def cook(self): ...    


    def cut(self): 
        print(class_name, '- Cortando Pizza')


    def serve(self):
        print(class_name, '- Servindo Pizza')


class French(Pizza): 
    def add_ingredients(self):
        print(class_name, '- Adicionando ingredientes...')

    
    def cook(self):
        print(class_name, '- No forno por 30 minutos')


class Portuguese(Pizza):
    def add_ingredients(self):
        print(class_name, '- Adicionando ingredientes...')

    
    def cook(self):
        print(class_name, '- No forno por 45 minutos')


if __name__ == '__main__':
    french = French()
    french.prepare()

    print()

    portuguese = Portuguese()
    portuguese.prepare()

