class BankAccount:
    def __init__(self,balance,account_number,owner_name):
        self.balance=balance
        self.account_number=account_number
        self.owner_name=owner_name

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return True
        return False

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return True
        return False

acc1=BankAccount(1000,"001","ayşe")
acc2=BankAccount(500,"002","ozan")

acc1.deposit(300)
acc2.withdraw(100)

print(f"{acc1.owner_name}: {acc1.balance}")  # 1300
print(f"{acc2.owner_name}: {acc2.balance}")  # 400

