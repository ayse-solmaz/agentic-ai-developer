# Hierarchy (Day 11): shallow only
# Account
#  ├── SavingsAccount
#  └── CheckingAccount
# One level is enough. Deeper trees → fragile base class risk.
class Account:
    def __init__(self,account_number,balance):
        if balance < 0:
            raise ValueError("balance cannot be negative")
        if not account_number.strip():
            raise ValueError("account number cannot be empty")
        self._account_number=account_number
        self._balance=balance
    def get_balance(self):
        return self._balance
    def get_account_number(self):
        return self._account_number
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount
    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("withdraw must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
acc=Account("001",1000)
acc.deposit(100)
print(acc.get_balance()) #1100

class SavingsAccount(Account):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)  # parent's kur
        self._intereset_rate=interest_rate
    def apply_interest(self):
        interest= self._balance * self._intereset_rate
        self.deposit(interest) # miras alınan method
        return interest
class CheckingAccount(Account):
    def __init__(self,account_number,balance,overdraft_limit):
        super().__init__(account_number,balance)
        self._overdraft_limit=overdraft_limit
    def withdraw(self,amount): # özel kural - görev 3'te reuse de bakarız
        if amount <=0:
            raise ValueError("withdraw must be positive")
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Overdraft exceeded")
        self._balance -= amount
sav = SavingsAccount("S01", 1000, 0.05)
chk = CheckingAccount("C01", 500, 200)
print(sav.get_balance(), chk.get_balance())
sav = SavingsAccount("S01", 1000, 0.05)
chk = CheckingAccount("C01", 500, 200)

# Inherited from Account
sav.deposit(200)
print("savings:", sav.get_balance(), sav.get_account_number())

chk.deposit(50)
print("checking:", chk.get_balance())

# Specialized
interest = sav.apply_interest()   # veya apply_intrest — senin metod adın
print("interest:", interest, "balance:", sav.get_balance())

# Checking overdraft: balance 550, limit 200 → max 750
chk.withdraw(700)
print("after overdraft withdraw:", chk.get_balance())