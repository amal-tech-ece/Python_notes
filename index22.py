# def square(x):
#     return x*x
# numbers=[1,2,3,4]
# result=map(square,numbers)
# print(list(result))
# def is_even(x):
#     return x%2==0
# numbers=[1,2,3,4,5,6]
# result=filter(is_even,numbers)
# print(list(result))

# from functools import reduce
# def multiply(a,b):
#     return a*b
# numbers=[1,2,3,4]
# result=reduce(multiply,numbers)
# print(result)


# numbers=[5,8,2,1,12]
# print(sorted(numbers))

# numbers=[1,2,3,4]
# result=map(lambda x:x*2,numbers)
# print(list(result))

numbers=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x:x%2==0,numbers)
print(list(result))