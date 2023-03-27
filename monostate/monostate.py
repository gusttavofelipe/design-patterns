'''
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
'''

class StringReprMixim:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
            )
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixim):
    _state = {
        # 'x': 10, 'y': 11
    }
    def __init__(self, name=None, last_name=None) -> None:
        self.__dict__ = self._state
        # alteracoes são visiveis apenas depois do state
        # self.x = 100000
        if name is not None:
            self.name = name
        if last_name is not None:    
            self.last_name = last_name


if __name__ == '__main__':
    m1 = MonoStateSimple('Gustavo')
    m2 = MonoStateSimple(last_name='Silva ')
    # o valor é mudado para todas as instancias como nos singletons
    # m2.x = 'another value'
    print(m1)
    print(m2)
    