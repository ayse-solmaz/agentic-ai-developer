# Don't pattern-hunt:
# One simple Customer(name, id) needs NO Factory/Strategy.
# Pattern only when creation or algorithms get messy.
class Account:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, number, balance):
        super().__init__(number, balance)
        self.kind = "savings"

class CheckingAccount(Account):
    def __init__(self, number, balance):
        super().__init__(number, balance)
        self.kind = "checking"

def open_account(kind, number, balance):  # FACTORY
    if kind == "savings":
        return SavingsAccount(number, balance)
    if kind == "checking":
        return CheckingAccount(number, balance)
    raise ValueError("Unknown account kind")

# caller constructors bilmez:
a = open_account("savings", "S01", 1000)
b = open_account("checking", "C01", 500)
print(a.kind, b.kind)

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
# BAD
def fee_bad(kind, amount):
    if kind == "flat":
        return 2
    elif kind == "percent":
        return amount * 0.01
    elif kind == "none":
        return 0
    return 0

# GOOD — if yok; strategy ver
def withdraw(balance, amount, strategy):
    total = amount + strategy.fee(amount)
    return balance - total

print(withdraw(1000, 100, FlatFee()))     # 898
print(withdraw(1000, 100, PercentFee()))  # 899.0
print(withdraw(1000, 100, NoFee()))       # 900
