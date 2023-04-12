"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IObservable(ABC):  # Observable

    @property
    @abstractmethod
    def state(self): ...

    @abstractmethod
    def add_observer(self, observer: IObservable): ...

    @abstractmethod
    def remove_observer(self, observer: IObservable): ...

    @abstractmethod
    def notify_observers(self, observer: IObservable): ...


class WeatherStation(IObservable):  # ConcreteObservable
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


class IObserver(ABC):  # Observer
    @abstractmethod
    def update(self): ...


class SmartPhone(IObserver):  # ConcreteObserver
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}, o objeto {observable_name}\n'
              f'foi atualizado -> {self.observable.state}')


class Notebook(IObserver):  # ConcreteObserver
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}, o objeto {observable_name}\n'
              f'foi atualizado -> {self.observable.state}')


class WeatherStationFacade:
    '''Facade Object'''
    def __init__(self) -> None:
        self.weather_station = WeatherStation()

        self.smartphone = SmartPhone('Nokia', self.weather_station)
        self.notebook = Notebook('Acer', self.weather_station)

        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, obeserver: IObserver) -> None:
        self.weather_station.remove_observer(obeserver)

    def change_state(self, state: dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        self.weather_station.remove_observer(self.smartphone)

    def reset_state(self) -> None:
        self.weather_station.reset()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()
    weather_station.change_state({'temperature': '30°'})
    weather_station.change_state({'temperature': '27°'})

    weather_station.remove_smartphone()

    weather_station.change_state({'humidity': '80%'})
    weather_station.change_state({'humidity': '98&'})
