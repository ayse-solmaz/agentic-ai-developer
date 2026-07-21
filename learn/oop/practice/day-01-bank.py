# OOP Day 1 — Procedural vs OOP (Bank: withdraw)

# --- Procedural ---
balance = 1000

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        return True
    return False

withdraw(200)
print("Procedural balance:", balance)

# --- OOP ---
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

account = BankAccount(1000)
account.withdraw(200)
print("OOP balance:", account.balance)
