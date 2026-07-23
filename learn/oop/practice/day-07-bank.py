#BankAccount Invariants:
#_balance>=0
#_account_number cannot be empty
#_customer.get_name() cannot be empty

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
        if not account_number.strip():
            raise ValueError("Account number cannot be empty")

        self._balance = balance
        self._account_number = account_number
        self._customer = customer                  
        self.transaction_history = []
        self._log=TransactionLog()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self._log.add(f"Deposited {amount}")
        self._assert_invariants()
        return True
        

    def withdraw(self, amount):
        if amount <= 0:
           raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
           raise ValueError("Insufficient funds")
        self._balance -= amount
        self._log.add(f"Withdrew {amount}")
        self._assert_invariants()
        return True

    @staticmethod
    def open_empty(account_number, customer):
        return BankAccount(0, account_number, customer)
    
    def get_balance(self):
        return self._balance
    
    def transfer_to(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        self._log.add(f"Transferred {amount} to {other._account_number}")
        self._assert_invariants()
        return True
    
    def get_account_number(self):
        return self._account_number
    
    def get_customer_name(self):
        return self._customer.get_name()

    def get_log_entries(self):
        return list(self._log.entries)  # kopya — dışarıdan liste bozulmasın
    def _assert_invariants(self):
        if self._balance < 0:
            raise RuntimeError("Invariant broken: balance negative")
        if  not self._account_number.strip():
            raise RuntimeError("Invariant broken: account number empty")
        if not self._customer.get_name().strip():
            raise RuntimeError("Invariant broken: customer name empty")
        


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

try:
    acc1.withdraw(99999)
except ValueError as e:
    print("fail fast:",e)

try:
    acc1.deposit(-50)
except ValueError as e:
    print("fail fast:",e)

    # --- Görev 4: invariant edge case testleri ---

def test_invariants():
    c = Customer("Test", 1)

    # Edge 1: boş hesap no
    try:
        BankAccount(100, "", c)
        print("FAIL: empty account number allowed")
    except ValueError:
        print("OK: empty account number blocked")

    # Edge 2: sıfır deposit
    acc = BankAccount(100, "999", c)
    try:
        acc.deposit(0)
        print("FAIL: zero deposit allowed")
    except ValueError:
        print("OK: zero deposit blocked")

    # Edge 3: bakiye üstü withdraw
    try:
        acc.withdraw(500)
        print("FAIL: overdraft allowed")
    except ValueError:
        print("OK: overdraft blocked")

    # Edge 4: bakiye hâlâ sağlam mı?
    assert acc.get_balance() == 100
    print("OK: balance unchanged after failed withdraw")

test_invariants()