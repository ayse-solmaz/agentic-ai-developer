class TransactionLog:
    def __init__(self):
        self.entries=[]

    def add(self,message):
        self.entries.append(message)

class BankAccount:
    def __init__(self, balance, account_number, owner_name):
        # Validation FIRST — before object is fully built
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        if not owner_name.strip():
            raise ValueError("Owner name cannot be empty")

        self.balance = balance
        self.account_number = account_number
        self.owner_name = owner_name
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
    def open_empty(account_number, owner_name):
        return BankAccount(0, account_number, owner_name)
    
    def get_balance(self):
        return self.balance
    
    def transfer_to(self,other,amount):
        if self.withdraw(amount):
            other.deposit(amount)
            self.log.add(f"Transferred {amount} to {other.account_number}")
            return True
        return False



acc1 = BankAccount(1000, "001", "ayşe")
acc2 = BankAccount.open_empty("002", "ozan")

acc1.transfer_to(acc2, 200)

print("acc1:", acc1.get_balance())   # 800
print("acc2:", acc2.get_balance())   # 200
print("log:", acc1.log.entries)      # işlem mesajları
