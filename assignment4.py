# def create_account(name,acc_number,acc_type="saving"):
#     print("Name: ",name)
#     print("Account Number: ",acc_number)
#     print("Account Type: ",acc_type)
# name=input("Enter your number:")
# acc_number=input("Enter your account number:")
# create_account(name,acc_number)

def deposit_amount(dep_amount,blance=100):
    blance=blance+dep_amount
    print("Deposit amount:Rs ",dep_amount)
    print("Blance:Rs ",blance)

dep_amount=int(input("Enter the amount:"))
deposit_amount(dep_amount)