from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):

    def pay(self):
        print("UPI payment done")

class Card(Payment):

    def new(self):#show error becouse that class  not use absctract method from abstact class
        print("Card payment done")


obj=Card()