from abc import ABC, abstractclassmethod


class Template(ABC):
    @abstractclassmethod
    def method(self):...

    @abstractclassmethod
    def method2(self): ...

    def hook(self): ...
        
    def template_method(self):
        self.hook()
        self.method()
        self.method2()


class ConcreteClass(Template):
    def hook(self):
        print('utilizando o hook')


    def method(self):
        print('operation 1 succsesfuly')


    def method2(self):
        print('operation 2 succsesfuly')
 

class ConcreteClass2(Template):
    def method(self):
        print('operation 1 succsesfuly diferentemente')

    def method2(self):
        print('operation 2 succsesfuly diferentemente')


if __name__ == '__main__':
    temp1 = ConcreteClass()
    temp1.template_method()

    temp2 = ConcreteClass2()
    temp2.template_method()