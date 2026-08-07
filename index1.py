def add(a,b):
    print(a+b)
result=add(10,20)
print(result)

def add(a,b):
    return a+b
result=add(10,20)
print(result)



def welcom():
    print("welcome")
welcom()
welcom()





def greet():
    print("hello")



print("a")
def greet():
    print("hai")
print("b")
greet()



def greet(name):
    print("hai",name)
greet("amal")



def test():
    print("a")
    return
    print("b")
test()


# Python can conveniently return multiple values.
def stats(a,b):
    return a+b,a*b
s,p=stats(2,3)
print("sum",s)
print("product",p)
stats(2,3)




def add(a,b):
    print(a+b)
add(5,5)


def add(a,b):
    print(a+b)
add(10,20)



def square(x):
    print(x*x)
square(2)



square=lambda x:x*x
print(square(2))


add=lambda a,b:a+b
print(add(2,3))


def greet(name,age):
    print("name=",name)
    print("age=",age)
greet("amal",22)




def greet(name,age):
    print("name=",name)
    print("age=",age)
greet(22,"amal")



def greet(name,age):
    print("name=",name)
    print("age=",age)
greet(age=22,name="amal")






def greet(name="guest"):
    print("hello",name)
greet()

def greet(name="guest"):
    print("hello",name)
greet("amal")


def greet(age,name="guest"):
    print("hello",name)
    print("age=",age)
greet(25)











