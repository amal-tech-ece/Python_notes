class BankAccount:
    def __init__(self,account_name,account_number,blance):
        self.account_name=account_name
        self.account_number=account_number
        self.blance=blance
    def deposit(self,amount):
        self.blance+=amount
        print("blance : ",self.blance)
    def withdraw(self,amount):
        if amount>self.blance:
            print("insufficient blance")
        else:
            self.blance-=amount
            print("Blance :",self.blance)
    def blance(self):
        print("Blance : ",self.blance)
