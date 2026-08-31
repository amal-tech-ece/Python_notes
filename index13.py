from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def area(self):
        return 4*4
class Rectangle(Shape):
    def area(self):
        return 4*2
# d=Rectangle()
# print(d.area())
s=Shape()
print(s.area())