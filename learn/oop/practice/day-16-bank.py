# Before/After count:
# BAD fee switch: add Premium → edit calc_fee_bad (1 place that grows forever)
#   + every caller that must know new type strings
# GOOD FeePolicy: add PremiumFee class only (1 new file/class)
#   withdraw_with_fee unchanged, SavingsFee/CheckingFee unchanged
# Places changed for new fee type:
#   bad approach ≈ 1+ (switch + any string callers)
#   good approach ≈ 1 (new class only)

# before (srp violation) : money + notifications in one class
class BankAccount:
    def __init__(self,balance,email):
        self.balance = balance
        self.email = email
    def withdraw(self,amount):
        self.balance -= amount
        print(f"email to {self.email}: withdraw {amount}")

# after (srp):

class Notifier:
    def notify(self,email,message):
        print(f"email to {email}: {message}")
class Account:
    def __init__(self,balance,email,notifier):
        self._balance = balance
        self._notifier = notifier
        self._email = email
    def withdraw(self,amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._notifier.notify(self._email, f"Withdrew {amount}")
    def get_balance(self):
        return self._balance

Account(1000, "a@x.com", Notifier()).withdraw(100)

def calc_fee_bad(account_type, amount):
    if account_type == "savings":
        return 2
    elif account_type == "checking":
        return 1
    # yeni tip gelince BURAYI tekrar edit et → OCP ihlali
    return 0

from abc import ABC, abstractmethod

class FeePolicy(ABC):
    @abstractmethod
    def fee(self,amount):
        pass

class SavingsFee(FeePolicy):
    def fee(self,amount):
        return 2

class CheckingFee(FeePolicy):
    def fee(self, amount):
        return 1
class PremiumFee(FeePolicy):   # YENİ davranış = YENİ class (switch'e dokunma)
    def fee(self, amount):
        return 0

def withdraw_with_fee(balance, amount, policy):
    total = amount + policy.fee(amount)
    if total > balance:
        raise ValueError("Insufficient funds")
    return balance - total

print(withdraw_with_fee(1000, 100, SavingsFee()))   # 898
print(withdraw_with_fee(1000, 100, PremiumFee()))  # 900

# Smell: ReportExporter that both
# 1) calculates account interest AND
# 2) writes PDF / uploads to S3
# Two reasons to change → split Calculator vs Exporter