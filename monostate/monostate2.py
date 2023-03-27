
class StringReprMixim:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
            )
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__


class MonoState(StringReprMixim):
    _state = {
        # 'x': 10, 'y': 11
    }


    def __new__(cls, *args, **kwargs) :
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj


    def __init__(self, name=None, last_name=None) -> None:
        # alteracoes são visiveis apenas depois do state
        # self.x = 100000
        if name is not None:
            self.name = name
        if last_name is not None:    
            self.last_name = last_name


class A(MonoState):
    ...


if __name__ == '__main__':
    m1 = MonoState('Gustavo')
    m2 = MonoState(last_name='Silva ')
    m3 = A()
    # o valor é mudado para todas as instancias como nos singletons
    # m2.x = 'another value'
    print(m3)
    print(m1)
    print(m2)
    