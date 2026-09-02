def agechecker(age):
    if age<0:
        raise ValueError("age cannot be negative")
    return age
try:
    print(agechecker(-22))
except ValueError as e:
    print("Age cannot be negative",e)
except Exception as e:
    print("Unexpected error:",e)

