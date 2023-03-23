'''
resolvendo problema de sobreposição
de valores susando um decorador
'''

def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class

@singleton
class AppSettings:
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
