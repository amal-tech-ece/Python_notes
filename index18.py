try:
    a=10
    b=5
    
    if b==0:
        raise ZeroDivisionError("b cannot be 0")
    result=a/b
except ZeroDivisionError as e:
    print("Cannot divide by zero!",e)
except Exception as e:
    print("Unexpected error:",e)
else:
    print("Result is",result)
finally:
    print("Cleanup complete")
   