# Design critique (Day 15):
# - Used Payable ABC + BankAccount/Wallet instead of deep inheritance tree
# - Shared logging via composition (has-a TransactionLog), not Logger(Account)
# - process_payments depends on Payable only — shallow, swappable

from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def label(self):
        """short name for demo prints"""
        pass


class TransactionLog:
    def __init__(self):
        self._entries = []

    def add(self, message):
        self._entries.append(message)

    def get_entries(self):
        return list(self._entries)


class BankAccount(Payable):
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._log = TransactionLog()  # composition (Görev 3 için hazır)

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._log.add(f"Withdrew {amount}")

    def label(self):
        return f"Bank:{self._name}"
    def get_log_entries(self):
        return self._log.get_entries()


class Wallet(Payable):
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def label(self):
        return f"Wallet:{self._name}"

a = BankAccount("ayşe", 1000)
w = Wallet("cash", 200)
print(a.label(), a.get_balance())
print(w.label(), w.get_balance())

def process_payments(payables, amount):
    for p in payables:
        p.withdraw(amount)
        print(p.label(), "→", p.get_balance())


sources = [
    BankAccount("ayşe", 1000),
    Wallet("cash", 200),
    BankAccount("ozan", 500),
]

process_payments(sources, 50)
bank = sources[0]  # BankAccount ayşe
print("log via composition:", bank.get_log_entries())