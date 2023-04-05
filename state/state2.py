from __future__ import annotations
from abc import ABC, abstractmethod


class Sound: ## Context
    def __init__(self) -> None:
        self.mode: PlayerMode = RadioMode(self)
        self.playing = 0

    
    def change_mode(self, mode: PlayerMode) -> None:
        print(f'Mudando para {mode.__class__.__name__}')
        self.playing = 0
        self.mode = mode
    

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)
    

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    
    def __str__(self) -> str:
        return str(self.playing)


class PlayerMode(ABC): ## State
    def __init__(self, sound: Sound) -> None:
        self.sound = sound


    @abstractmethod
    def press_next(self) -> None:...


    @abstractmethod
    def press_prev(self) -> None:...


class RadioMode(PlayerMode): ## ConcreteState
    def press_next(self) -> None:
        self.sound.playing += 20


    def press_prev(self) -> None:
        self.sound.playing -= 20 if self.sound.playing > 0 else 0 


class MusicMode(PlayerMode): ## ConcreteState
    def press_next(self) -> None:
        self.sound.playing += 1


    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0 


if __name__ == '__main__':

    sound = Sound()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()


    print()    

    sound.change_mode(MusicMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()

    print()    

    sound.change_mode(RadioMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()