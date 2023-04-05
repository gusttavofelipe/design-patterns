"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from abc import ABC, abstractmethod


class Order: ## Context
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)


    def pending(self) -> None:
        print('Executando pending()')
        print('Estado: atual', self.state)
        self.state.pending()
        print()


    def aprove(self) -> None:
        print('Executando aprove()')
        print('Estado: atual', self.state)
        self.state.aprove()
        print()


    def reject(self) -> None:
        print('Executando reject()')
        print('Estado: atual', self.state)
        self.state.reject()
        print()


class OrderState(ABC): ## State
    def __init__(self, order: Order) -> None:
        self.order = order


    @abstractmethod
    def pending(self) -> None: ...


    @abstractmethod
    def aprove(self) -> None: ...


    @abstractmethod
    def reject(self) -> None: ...


    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState): ## ConcreteState

    def pending(self) -> None:
        print('Pagamento já pendente')


    def aprove(self) -> None:
        self.order.state = PaymentAproved(self.order)
        print('Pagamento aprovado')


    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento recusado')


class PaymentAproved(OrderState): ## ConcreteState

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')


    def aprove(self) -> None:
        print('Pagamento já aprovado')


    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento recusado')


class PaymentReject(OrderState): ## ConcreteState

    def pending(self) -> None:
        print('Pagamento recusado')


    def aprove(self) -> None:
        print('Pagamento recusado')


    def reject(self) -> None: 
        print('Pagamento recusado')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.aprove()
    order.aprove()
    order.pending()
    order.pending()
    order.reject()
    order.pending()
    order.aprove()
    order.reject()  

