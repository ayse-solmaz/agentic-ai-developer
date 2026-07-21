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

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    @staticmethod
    def open_empty(account_number, owner_name):
        return BankAccount(0, account_number, owner_name)


acc1 = BankAccount(1000, "001", "ayşe")
acc2 = BankAccount(500, "002", "ozan")

acc1.deposit(300)
acc2.withdraw(100)

print(f"{acc1.owner_name}: {acc1.balance}")  # 1300
print(f"{acc2.owner_name}: {acc2.balance}")  # 400

# Factory
acc3 = BankAccount.open_empty("003", "Ali")
print(acc3.balance)  # 0

# Validation
try:
    BankAccount(-50, "004", "Test")
except ValueError as e:
    print("Caught:", e)
