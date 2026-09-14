# def greet():
#     print("Hello")

# x=greet
# x()

# x=greet()



# def square(x):
#     return x*x

# def calculate(func,value):
#     return func(value)

# result=calculate(square,5)
# print(result)



def outer():
    def inner():
        print("Hello")
    return inner
x=outer()
x()