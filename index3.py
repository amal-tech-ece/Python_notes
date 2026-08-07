def hai():
    text="hello"
    print(text[:5])

    text="hello"
    print(text[2:])

    text="hello"
    print(text[::-1])

    text="hello"
    print(text[::2])

    text="hello"
    print(text[:3])

    first="hello"
    second=" world"
    print(first+second)

    msg="good"
    msg+=" morning"
    print(msg)


    word=["python","is","good"]
    ",".join(word)
    print(",".join(word))

    name="venna"
    age=30
    print(f"{name} is {age} yeras old")


    age=25
    print("age:"+age)#error

    age=25
    print(f"age:{age}")

    age=25
    print("age:"+str(age))

    mixed=[10,"python",3.5,True]
    print(mixed)

    num=[10,20,30,40,50]
    print(num[0])

    num=[10,20,30,40,50]
    print(num[-5])

    num=[10,20,30,40,50]
    print(num[1:4])

    num=[10,20,30,40,50]
    print(num[:4])

    num=[10,20,30,40,50]
    print(num[:5:2])

    num=[10,20,30,40,50]
    print(num[::-1])

    num=[10,20,30,40,50]
    num[0]=1
    num[2]=3
    num[4]=5
    print(num)

    num=[10,20,30,40,50]
    num.append(3)
    print(num)

    num=[10,20,30,40,50]
    num.append(3,4)
    print(num)

    num=[10,20,30,40,50]
    num.insert(3,4)
    print(num)

    num=[10,20,30,40,50]
    num.extend([6,7])
    print(num)

    num=[10,20,30,40,50]
    num.append([3,4])
    print(num)

    num=[10,20,30,40,50]
    num.remove(10)
    print(num)

    num=[10,20,30,40,50]
    num.remove(1)
    print(num)

    num=[10,20,30,40,50]
    num.pop(0)
    print(num)

    num=[10,20,30,40,50]
    num.pop()
    print(num)

    num=[10,20,30,40,50]
    num.pop()
    print(num)
    x=num.pop()
    print(x)

    num=[10,20,30,40,50]
    num.clear()
    print(num)

    num=[10,20,30,40,50]
    num.index(10)
    print(num)

num=[1,2,2,2,3,3]
num.count(2)
print(num.count(3))

num=[10,20,30,40,50]
num.index(10)
print(num.index(10))

num=[20,10,50,40,30]
num.sort()
print(num)

num=[20,10,50,40,30]
num.sort(reverse=True)
print(num)

num=[20,10,50,40,30]
num.reverse()
print(num)

num=[20,10,50,40,30]
num.sort()
num.reverse()
print(num)



















