'''
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
 operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final)
'''


from __future__ import annotations
from abc import ABC, abstractmethod


class Light: ### Reciver
    def __init__(self, name, locale) -> None:
        self.name = name
        self.locale = locale
        self.color = 'Default color'
        self.alight = False
    
    
    def on(self) -> None:
        print(f'The {self.name} is now ON ')


    def off(self) -> None:
        print(f'The {self.name} is now OFF ')

    
    def change_color(self, color: str):
        self.color = color
        print(f'The {self.name} is now {self.color}')



class ICommand(ABC): ### Command Interface

    @abstractmethod # execute command
    def execute(self) -> None: ...


    @abstractmethod # execute inverse command
    def undo(self) -> None: ...


class LightOnCommand(ICommand): ### ConcreteCommand
    def __init__(self, light: Light) -> None:
        self.light = light


    def execute(self) -> None:
        self.light.on()


    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand): ### ConcreteCommand
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._previous_color = self.light.color


    def execute(self) -> None:
        self._previous_color = self.light.color
        self.light.change_color(self.color)


    def undo(self) -> None:
        self.light.color = self._previous_color
        self.light.change_color(self._previous_color)


class RemoteController: ### Invoker
    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}
        self._undos: list[tuple[str, str]] = []


    def button_add_command(self, id: str, command: ICommand) -> None:
        self._buttons[id] = command


    def button_pressed(self, id: str) -> None:
        if id in self._buttons:
            self._buttons[id].execute()
            self._undos.append((id, 'execute'))

    
    def undo_button(self, id: str) -> None:
        if id in self._buttons:
            self._buttons[id].undo()
            self._undos.append((id, 'undo'))

    def global_undo(self):
        if not self._undos:
            print('Nothing to undo')
            return None
        
        button_id, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_id].undo()
        else:
            self._buttons[button_id].execute()

        self._undos.pop()


if __name__ == '__main__':
    bedroom_light = Light('bedroom light' ,'bedroom')
    bathroom_light = Light('bathroom light', 'bathroom')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_red = LightChangeColor(bedroom_light, 'red')
    bedroom_light_gray = LightChangeColor(bedroom_light, 'gray')

    remote = RemoteController()
    remote.button_add_command('button 1', bedroom_light_on)
    remote.button_add_command('button 2', bathroom_light_on)
    remote.button_add_command('button 3', bedroom_light_red)
    remote.button_add_command('button 4', bedroom_light_gray)

    remote.button_pressed('button 1')
    remote.button_pressed('button 2')
    remote.button_pressed('button 3')
    remote.button_pressed('button 4')

    # remote.undo_button('button 1')
    # remote.undo_button('button 2')
    # remote.undo_button('button 4')
    # remote.undo_button('button 3')

    print()

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo() 
    remote.global_undo() 