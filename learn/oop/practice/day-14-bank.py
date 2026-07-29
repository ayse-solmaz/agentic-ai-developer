# Bad hierarchy (forced inheritance):
# class Logger(Account):   # ??? Logger is NOT an Account
#     def write(self, msg): ...
#
# Why awkward?
# 1. Logger is not an Account (no is-a)
# 2. Inherits deposit/withdraw it does not need
# 3. Changing Account can break Logger for no reason
# Rule of thumb:
# Inheritance → true is-a (SavingsAccount IS an Account)
# Composition → has-a / reuse helper (Account HAS a TransactionLog / InterestCalculator)
# Prefer composition when you only want shared behavior, not a subtype

from traceback import print_tb


class TransactionLog:
    def __init__(self):
        self._entries = []

    def add(self,message):
        self._entries.append(message)

    def get_entries(self):
        return list(self._entries)

class Account:
    def __init__(self, account_number, balance, interest=None):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._account_number = account_number
        self._balance = balance
        self._log = TransactionLog()
        self._interest = interest

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._log.add(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._log.add(f"Withdrew {amount}")

    def get_balance(self):
        return self._balance

    def get_log_entries(self):
        return self._log.get_entries()

    def apply_interest(self):
        if self._interest is None:
            raise ValueError("No interest calculator")
        amount = self._interest.calculate(self._balance)
        self.deposit(amount)
        return amount

acc = Account("001",1000)
acc.deposit(200)
acc.withdraw(50)
print(acc.get_balance()) #1150
print(acc.get_log_entries())

class InterestCalculator:
    def __init__(self, rate):
        if rate < 0:
            raise ValueError("Rate cannot be negative")
        self._rate = rate

    def calculate(self, balance):
        return balance * self._rate


calc = InterestCalculator(0.05)
acc = Account("002", 1000, interest=calc)
print(acc.apply_interest())   # 50.0
print(acc.get_balance())      # 1050.0