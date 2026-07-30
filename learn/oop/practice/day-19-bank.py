class Account:
    def __init__(self, balance):
        self._balance = balance
        self._listeners = []   # aboneler

    def subscribe(self, listener):
        self._listeners.append(listener)

    def _notify(self, event):
        for listener in self._listeners:
            listener(event)    # her aboneye haber

    def withdraw(self, amount):
        self._balance -= amount
        self._notify(f"withdrew {amount}, left {self._balance}")

    def get_balance(self):
        return self._balance


def log_listener(event):
    print("LOG:", event)

def sms_listener(event):
    print("SMS:", event)


acc = Account(1000)
acc.subscribe(log_listener)
acc.subscribe(sms_listener)
acc.withdraw(100)
# Beklenen:
# LOG: withdrew 100, left 900
# SMS: withdrew 100, left 900

# characterization (before refactor):
# 1) holds balance
# 2) withdraw decreases balance
# 3) prints email on withdraw
# 4) appends to a history list
# after refactor these 4 behaviors must still work.


class GodBank:
    def __init__(self, balance, email):
        self.balance = balance
        self.email = email
        self.history = []

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(f"withdrew {amount}")
        print(f"EMAIL {self.email}: withdrew {amount}")

class TransactionLog:
    def __init__(self):
        self.entries = []
    def add(self, msg):
        self.entries.append(msg)

class Notifier:
    def send(self, email, msg):
        print(f"EMAIL {email}: {msg}")

class CleanAccount:
    def __init__(self, balance, email, log, notifier):
        self._balance = balance
        self._email = email
        self._log = log
        self._notifier = notifier

    def withdraw(self, amount):
        self._balance -= amount
        self._log.add(f"withdrew {amount}")
        self._notifier.send(self._email, f"withdrew {amount}")

    def get_balance(self):
        return self._balance

log = TransactionLog()
acc2 = CleanAccount(500, "a@x.com", log, Notifier())
acc2.withdraw(50)
print(acc2.get_balance())  # 450
print(log.entries)         # ['withdrew 50']

# Small steps (verify after each):
# Step1: keep GodBank, add characterization comments — run OK
# Step2: extract TransactionLog, GodBank uses it — run OK
# Step3: extract Notifier — run OK
# Step4: rename to CleanAccount — run OK
# Never rewrite everything in one blind jump.