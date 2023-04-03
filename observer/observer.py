'''
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações
'''

from __future__ import annotations
from abc import ABC, abstractmethod


class IObservable(ABC): # Observable

    @property
    @abstractmethod
    def state(self):...

    @abstractmethod
    def add_observer(self, observer: IObservable): ...

    @abstractmethod
    def remove_observer(self, observer: IObservable): ...

    @abstractmethod
    def notify_observers(self, observer: IObservable): ...


class WeatherStation(IObservable): # ConcreteObservable
    def __init__(self) -> None:
        self._observers: list[IObserver] = []
        self._state: dict = {}


    def add_observer(self, observer: IObservable):
        self._observers.append(observer)


    def remove_observer(self, observer: IObservable):
        if observer in self._observers:
            self._observers.remove(observer)
        return


    def notify_observers(self, observer: IObservable): 
        for observer in self._observers:
            observer.update()


    def reset(self): 
        self._state = {}
        self.notify_observers(observer=WeatherStation)


    @property
    def state(self):
        return self._state
    

    @state.setter
    def state(self, state_upd: dict):
        new_state = {**self._state, **state_upd}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers(observer=WeatherStation)


class IObserver(ABC): # Observer
    @abstractmethod
    def update(self): ...


class SmartPhone(IObserver): # ConcreteObserver
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    
    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name}\n'
              f'foi atualizado -> {self.observable.state}')
        

if __name__ == '__main__':
    weather_station = WeatherStation()

    smartphone = SmartPhone('Nokia', weather_station)
    smartphone2 = SmartPhone('Oppo', weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(smartphone2)


    weather_station.state = {'temperature': '35°'}
    weather_station.state = {'temperature': '35°', 'humidity': '90%'}
    weather_station.state = {'temperature': '35°'}
    weather_station.state = {'temperature': '35°'}
    weather_station.state = {'temperature': '35°'}

    weather_station.remove_observer(smartphone2)
    weather_station.reset()   