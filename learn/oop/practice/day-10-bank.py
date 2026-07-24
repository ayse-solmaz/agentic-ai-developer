# Before → After (what is now impossible):
# 1. acc.balance = -999  → no public balance field
# 2. Negative opening balance → ValueError in __init__
# 3. withdraw more than balance → ValueError
# 4. deposit(0) / deposit(-5) → ValueError
# 5. Empty customer rename → ValueError

class Customer:
    def __init__(self,name,customer_id):
        self._name=name
        self._id=customer_id
    def get_name(self):
        return self._name
    def get_id(self):
        return self._id
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
class BankAccount:
    def __init__(self, balance, account_number, customer):
        if balance < 0:
          raise ValueError("Balance cannot be negative")
        if not account_number.strip():
           raise ValueError("Account number cannot be empty")
        if not customer.get_name().strip():
            raise ValueError("Customer name cannot be empty")
        self._balance = balance
        self._account_number = account_number
        self._customer = customer
        self._log = TransactionLog()

    def get_balance(self):
        return self._balance

    def get_customer_name(self):
        return self._customer.get_name()
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
    def receive_salary(self,amount):
        self.deposit(amount)
        self._log.add(f"salary received: {amount}")
    def pay_bill(self,amount,bill_name):
        self.withdraw(amount)
        self._log.add(f"paid bill: {bill_name}")
    def get_log_entries(self):
        return self._log.get_entries()
    
    
ayse = Customer("ayşe", "C001")
acc = BankAccount(1000, "001", ayse)
acc.deposit(200)
print(acc.get_balance())
print(acc.get_customer_name())  # getter ile

try:
    acc.withdraw(99999)
except ValueError as e:
    print("Blocked:", e)
acc.receive_salary(500)
acc.pay_bill(100, "electricity")
print(acc.get_balance())
print(acc._log.get_log_entries())  # veya get_log_entries getter ekle