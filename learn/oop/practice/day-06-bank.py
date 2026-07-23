class Customer:
    def __init__(self,name,id):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self._name=name
        self.id=id
    def get_name(self):
        return self._name
    def rename(self,new_name):
        if not new_name.strip():
            raise ValueError("Name cannot be empty")
        self._name=new_name

class TransactionLog:
    def __init__(self):
        self.entries=[]

    def add(self,message):
        self.entries.append(message)


class BankAccount:
    def __init__(self, balance, account_number,customer):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        if not customer.get_name().strip():
            raise ValueError("Customer name cannot be empty")

        self._balance = balance
        self._account_number = account_number
        self._customer = customer                  
        self.transaction_history = []
        self._log=TransactionLog()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log.add(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._log.add(f"Withdrew {amount}")
            return True
        return False

    @staticmethod
    def open_empty(account_number, customer):
        return BankAccount(0, account_number, customer)
    
    def get_balance(self):
        return self._balance
    
    def transfer_to(self,other,amount):
        if self.withdraw(amount):
            other.deposit(amount)
            self._log.add(f"Transferred {amount} to {other._account_number}")
            return True
        return False
    
    def get_account_number(self):
        return self._account_number
    
    def get_customer_name(self):
        return self._customer.get_name()

    def get_log_entries(self):
        return list(self._log.entries)  # kopya — dışarıdan liste bozulmasın

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

# görev 2 : dışarıdan yazma dene
# eski public field artık yok

try: 
    acc1.balance=-500
    print("Uyarı: balance hala public")

except AttributeError:
    print("balance doğrudan yazılamıyor - iyi")

# doğru yol: method ile
acc1.withdraw(100)
print("method ile:",acc1.get_balance())

try:
    ayse.rename("")
except ValueError as e:
    print("Rename blocked:", e)

ayse.rename("Ayşe Yılmaz")
print(ayse.get_name())

print(acc1.get_account_number())
print(acc1.get_customer_name())
print(acc1.get_log_entries())