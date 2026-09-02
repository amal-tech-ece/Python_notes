try:
    result=10/2 
except ZeroDivisionError as e:
    print("Cannot divide by zero!",e)
except Exception as e:
    print("Unexpected error:",e)
else:
    print("Result is",result)
finally:
    print("Cleanup complete")