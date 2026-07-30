# Violation hunt:
# LSP: BrokenReadOnlyAccount(Account) — withdraw surprises callers → use ReadOnlyView
# ISP: FatBankService forces PDF/SMS on every account → split Payable / Notifiable / Exportable
# DIP: pay() creating BankAccount inside → inject Payable instead
class Account:
    def __init__(self, balance):
        self._balance = balance
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
    def get_balance(self):
        return self._balance

# lsp violation: looks like account but withdraw always fails
class BrokenReadOnlyAccount(Account):
    def withdraw(self,amount):
        raise Exception("cannot withdraw") #caller account beklerken süpriz

#fix: don't pretend it's a withdrawable Account
class ReadOnlyView:
    def __init__(self,balance):
        self._balance = balance
    def get_balance(self):
        return self._balance
    # no withdraw -> honest API

class SavingsAccount(Account):
    def withdraw(self,amount):
        fee = 2
        super().withdraw(amount + fee) # still withdraws; same idea,stricter cost OK if documented


def take_100(acc: Account):
    acc.withdraw(100)
    print(acc.get_balance())

take_100(Account(500))          # 400
take_100(SavingsAccount(500))   # 398
# take_100(BrokenReadOnlyAccount(500))  # LSP break — bilerek deneme, comment'te bırak

from abc import ABC, abstractmethod

class FatBankService(ABC):
    @abstractmethod
    def withdraw(self, amount): pass
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def export_pdf(self): pass      # herkes buna ihtiyaç duymaz
    @abstractmethod
    def send_sms(self, msg): pass   # herkes buna ihtiyaç duymaz


class Payable(ABC):
    @abstractmethod
    def withdraw(self, amount): pass
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def get_balance(self): pass

class Notifiable(ABC):
    @abstractmethod
    def send_sms(self, msg): pass

class Exportable(ABC):
    @abstractmethod
    def export_pdf(self): pass

class SimpleAccount(Payable):
    def __init__(self, balance):
        self._balance = balance
    def withdraw(self, amount):
        self._balance -= amount
    def deposit(self, amount):
        self._balance += amount
    def get_balance(self):
        return self._balance
    # export_pdf / send_sms YOK — ISP

# High-level depends on Payable (abstraction), not BankAccount
def pay(source: Payable, amount):
    source.withdraw(amount)
    print("paid", amount, "left", source.get_balance())

# Inject concrete at the edge:
pay(SimpleAccount(300), 50)