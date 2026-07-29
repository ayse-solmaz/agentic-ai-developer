from abc import ABC,abstractmethod



class Payable(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass

try:
    Payable()
except TypeError as e:
    print("ok blocked: ",e)

class BankAccount(Payable):
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


class Wallet(Payable):
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


acc = BankAccount(1000)
wal = Wallet(200)
acc.deposit(50)
wal.withdraw(50)
print(acc.get_balance(), wal.get_balance())  # 1050 150

def pay(source, amount):
    """source = any Payable"""
    source.withdraw(amount)
    print(f"Paid {amount}, remaining: {source.get_balance()}")

pay(BankAccount(500), 100)
pay(BankAccount(500), 100)  # remaining 400
pay(Wallet(300), 50)        # remaining 250