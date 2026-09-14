# class Studeent:
#     def __init__(self):
#         self.mark=98
# r=Studeent()
# class Student:
#     def __init__(self):
#         self.mark=92
# s=Student()
# print(s.mark)

# class Student:
#     def __init__(self):
#         self.__mark=98
#     def Display(self):
#         print("Mark : ",self.__mark)


# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#             print("C")
# class D(B, C):
#     pass
# d = D()
# d.show()



# class A:
#     def show(self):
#         print("A")
# class B(A):
#     pass
# class C(A):
#     def show(self):
#             print("C")
# class D(B, C):
#     pass
# d = D()
# d.show()


# class Z:
#     pass
# class A(Z):
#     pass

# class B(A):
#     pass

# class E:
#     def show(self):
#         print("E")

# class C(E):
#     pass

# class D(B, C):
#     pass

# d = D()
# d.show()
# print(D.mro())


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show()


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# print(D.mro())


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass

# class C(B):
#     pass

# c = C()
# c.show()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())