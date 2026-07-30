# Reflection (20 days):
# Learned: encapsulation, contracts, SOLID, factory/strategy
# Hardest: LSP / when not to inherit
# SOLID that clicked: SRP + DIP
# Next practice: build a small real project with these rules
class Customer:
    def __init__(self,name,id):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self._name=name
        self.id=id
    def get_name(self):
        return self._name
    def rename(self,new_name):
        if not new_name.strip():
            raise ValueError("Name cannot be empty")
        self._name=new_name
class TransactionLog:
    def __init__(self):
        self._entries=[]
    def add(self,message):
        self._entries.append(message)
    def get_entries(self):
        return list(self._entries) # kopya
from abc import ABC, abstractmethod

class FeeStrategy(ABC):
    @abstractmethod
    def fee(self, amount):
        pass

class FlatFee(FeeStrategy):
    def fee(self, amount):
        return 2

class PercentFee(FeeStrategy):
    def fee(self, amount):
        return amount * 0.01

class NoFee(FeeStrategy):
    def fee(self, amount):
        return 0

class Payable(ABC):
    @abstractmethod
    def withdraw(self, amount): pass
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def get_balance(self): pass

class BankAccount(Payable):
    def __init__(self, balance, number, customer, notifier, fee_strategy):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance
        self._number = number
        self._customer = customer
        self._notifier = notifier
        self._fee = fee_strategy
        self._log = TransactionLog()
        self._email = "user@bank.com"  # basit tut

    def get_balance(self):
        return self._balance

    def get_log_entries(self):
        return self._log.get_entries()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._log.add(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        total = amount + self._fee.fee(amount)
        if total > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= total
        self._log.add(f"Withdrew {amount} (fee {self._fee.fee(amount)})")
        self._notifier.send(self._email, f"withdrew {amount}")

class Notifier:
    def send(self, email, msg):
        print(f"EMAIL {email}: {msg}")

def open_account(kind, number, balance, customer, notifier, fee_strategy):
    if kind == "savings":
        return BankAccount(balance, number, customer, notifier, fee_strategy)
    if kind == "checking":
        return BankAccount(balance, number, customer, notifier, NoFee())
    raise ValueError("Unknown account kind")

def pay(source, amount):
    """source = any Payable"""
    source.withdraw(amount)
    print(f"Paid {amount}, remaining: {source.get_balance()}")

c = Customer("ayşe", "C1")
acc = open_account("savings", "S01", 1000, c, Notifier(), FlatFee())
acc.deposit(100)
pay(acc, 50)
print(acc.get_balance())
print(acc.get_log_entries())  # getter ekle
