# class Student:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name)
# s=Student("Amal")
# s.show()


class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
    def withdraw(self,amount):
        if amount>self._balance:
            raise ValueError("Insufficient balance")
        self._balance-=amount
b=BankAccount(1000)
print(b._balance)
b.deposit(500)
print(b._balance)
b.withdraw(501)
print(b._balance)
# b.withdraw(1000)
# print(b._balance)