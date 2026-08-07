def show():
    x=10
    print(x)
show()

x=20
def show():
    print(x)
show()
print(x)



x=30
def show():
    global x
    x=40
    print(x)
show()
print(x)


def outer():
    x="out"

    def inner():
        nonlocal x
        x="in"

    inner()
    print("x after in():",x)
outer()


x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner x:", x)
    inner()
    print("Outer x:", x)
outer()
print("Global x:", x)






a=1
a=2

print(a)



def countdown(n):
    if n>1:
        return n*countdown(n-1)
    else:
        return 1
    print(n)
countdown(5)



student_name="amal"
print(student_name)




student1name="amal"
print(student1name)



ten=10
print(ten)



def factriol(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factriol(n-1)
num=int(input("enter the numer"))
print("factriol of",num,"is",factriol(num))


