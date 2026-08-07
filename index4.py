
def index4():
    num=[5,4,3,2,1]
    reverse_list=num[::-1]
    print(num)
    print(reverse_list)

    fruits=["apple","banana","mango"]#iterating over lists
    for fruit in fruits:
        print(fruit)

    fruits=["apple","banana","mango"]#iterating using for
    for i in range(len(fruits)):
        print(fruits[i])

    nums=[1,2,3]#membership operators(in & not in)
    print(2 in nums)
    print(5 not in nums)
    print(5 in nums)

    a=[1,2]
    b=[3,4]
    print(a+b)#co
    print(a*2)#repetition

    matrix=[[1,2],[3,4]]#nested list
    print(matrix)
    print(matrix[0])
    print(matrix[1])
    print(matrix[0][1])
    print(matrix[1][0])
def tuple122():
    #tuples
    num=(1,2,3,4,5)
    print(type(num))

    empty=()
    print(type(empty))

    n=(5)
    print(type(n))

    n=(5,)
    print(type(n))

    a=10,20
    print(type(a))
    x,y=a#tuple unpacking
    print(x)
    print(y)

    a=10,20
    x,y,z=a#value error
    print(x)
    print(y)
    print(z)

    a=10,20,30,40,50
    print(a[-1])
    print(a[4])

    num=(10,20,30,40,50)
    print(num[0:4])#tuple slicing
    print(num[::-1])#reverse
    num[0]=1#cannot modify a tuple
    print(num)

    num=(10,20,20,20,50)
    print(num.count(20))#counting how many
    print(num.index(10))#which index

    colours=("red","green","blue")
    for colour in colours:
        print(colour)

    student=("amal",22)
    name=student[0]
    age=student[1]
    print("name:",name,"age:",age)

    student=("amal",22)
    name,age=student
    print("name:",name,"age:",age)

    student=("amal",22)
    age,name=student
    print("name:",name,"age:",age)

    num=(1,2,3,4,5)
    a,b,*c=num
    print("a:",a)
    print("b:",b)
    print("c:",c)

num_list=[1,2,3]
print(num_list)
num_tuple=tuple(num_list)
print(num_tuple)
num_list1=list(num_tuple)
print(num_list1)

data=((1,2),(3,4))
print(data[0][0])
print(data[0][1])
print(data[1][0])
print(data[1][1])