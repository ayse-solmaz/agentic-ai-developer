class Customer:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class TransactionLog:
    def __init__(self):
        self.entries=[]

    def add(self,message):
        self.entries.append(message)


class BankAccount:
    def __init__(self, balance, account_number,customer):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        if not customer.name.strip():
            raise ValueError("Customer name cannot be empty")

        self.balance = balance
        self.account_number = account_number
        self.customer = customer                  
        self.transaction_history = []
        self.log=TransactionLog()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log.add(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.log.add(f"Withdrew {amount}")
            return True
        return False

    @staticmethod
    def open_empty(account_number, customer):
        return BankAccount(0, account_number, customer)
    
    def get_balance(self):
        return self.balance
    
    def transfer_to(self,other,amount):
        if self.withdraw(amount):
            other.deposit(amount)
            self.log.add(f"Transferred {amount} to {other.account_number}")
            return True
        return False

ayse=Customer("ayşe",1234567890)
ozan=Customer("ozan",1234567891)


acc1 = BankAccount(1000, "001", ayse)
acc2 = BankAccount.open_empty("002", ozan)

acc1.deposit(300)
acc1.transfer_to(acc2, 200)
print(acc1.get_balance())
print(acc2.get_balance())
try:
    BankAccount(-100,"003",Customer("",1234567892))
except ValueError as e:
    print("Caught:", e) 
