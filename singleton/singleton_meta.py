'''
Singleton usando metaclass
'''

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        print(cls._instances)
        return cls._instances[cls]
    

class AppSettings(metaclass=Singleton):
    print('Inicializado')
    def __init__(self) -> None:
        self.theme = 'default'
        self.font = 'arial'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.theme = 'black'
    print(as1.theme)

    as2 = AppSettings()
    print(as2.theme)

    # print(as1)
    # print(as2)
    # print(as1 == as2)  
    # print(id(as1) == id(as2))