'''O Singleton tem a intenção de garantir que uma classe tenha somente
uma instancia e fornece um ponto global de acesso para ela'''

class AppSettings:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    

    def __init__(self) -> None:
        self.theme = 'default'
        self.font = 'arial'
    

if __name__ == '__main__':
    as1 = AppSettings()
    as1.theme = 'black'
    print(as1.theme)

    as2 = AppSettings()
    print(as2.theme)
    # init chamado sempre que ha uma instancia nova
    # a nova instancia sobreppoe o valor anterior

    # print(as1)
    # print(as2)
    # print(as1 == as2)  
    # print(id(as1) == id(as2))

