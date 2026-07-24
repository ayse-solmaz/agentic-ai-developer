# Day 9 — Mutable vs Immutable
# Mutable = aynı nesne değişir (id aynı kalır)

# when to choose :
# mutable -> bankaccount gibi kimliği alan entity( aynı hesap,bakiue değişir)
# immutable -> money/ tarih gibi value object (deger degisince yeni kopya)
# trade-off: mutable kolay; immutable paylasımda daha guvenli,sonucu atamayı unutma

class MutableMoney:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._amount = amount

    def get_amount(self):
        return self._amount

    def add(self, value):
        if value < 0:
            raise ValueError("Cannot add negative")
        self._amount += value

    def subtract(self, value):
        if value < 0:
            raise ValueError("Cannot subtract negative")
        if value > self._amount:
            raise ValueError("Insufficient funds")
        self._amount -= value


# --- Görev 1 demo ---
m = MutableMoney(100)
print("before:", id(m), m.get_amount())
m.add(50)
print("after: ", id(m), m.get_amount())  # aynı id, 150

class ImmutableMoney:
    def __init__(self,amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._amount =amount
    def get_amount(self):
        return self._amount
    def add(self,value):
        if value <0:
            raise ValueError("cannot add negative")
        return ImmutableMoney(self._amount + value) # yeni nesne

# görev 2

class ImmutableWallet:
    def __init__(self,amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self._amount = amount
    def get_amount(self):
        return self._amount
    def add(self,value):
        if value < 0:
            raise ValueError("cannot add negative")
        return ImmutableMoney(self._amount + value) # yeni nesne
    def subtract(self,value):
        if value <0:
            raise ValueError("cannot subtract negative")
        if value > self._amount:
            raise ValueError("Insufficient funds")
        return ImmutableMoney(self._amount - value) # yeni nesne

im=ImmutableMoney(100)
print("before", id(im),im.get_amount())
im2=im.add(50)
print("old:   ",id(im),im.get_amount()) # hala 100
print("new:   ",id(im2),im2.get_amount()) # yeni id, 150

# trade-ofs:
# mutable: kolay kullan (m.add(50)), ama paylasılan nesne yan etki riski
# immutable: im2=im.add(50) unutulursa eski kalir ; debug/paylasım daha guvenli
# debug: immutable'da eski hali kaybolmaz
# sharing: aynı mutablemoney'yi iki yerde tutmak tehlikeli