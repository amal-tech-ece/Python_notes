# def divide(a,b):
#     try:
#         result=a/b
#         return result
#     except ZeroDivisionError as e:
#         print("Error occurred inside divide()")
#         raise
# try:
#     result=divide(10,0)
#     print("Result: ",result)
# except ZeroDivisionError:
#     print("caller handled the error")


# try:
#     x=10/0
# except Exception:
#     print("General error")
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# try:
#     x=10/0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception:
#     print("General error")


# try:
#     val=int(None)
# except (ValueError,TypeError) as e:
#     print("Ivalid input:",e)
#Ivalid input: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'


# try:
#     f=open("data.txt","r")
#     try:
#         data=f.read()
#         number=int(data)
#     except ValueError:
#         print("File does not contain a valid integer")
#     finally:
#         f.close()
# except FileNotFoundError:
#     print("File not found")


# class InsufficientFundError(Exception):
#     pass
# class BankAccount:
#     def __init__(self,blance=0):
#         self.blance=blance
#     def withdraw(self,amount):
#         if amount>self.blance:
#             raise InsufficientFundError(
#                 f"Attempted to withdraw {amount},but only {self.blance} availale"
#             )
#         self.blance-=amount
#         print(self.blance)
# b=BankAccount()
# try:
#     b.withdraw(5)
# except InsufficientFundError as e:
#     print("error")