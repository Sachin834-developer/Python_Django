"""
Abstraction: abstraction is a process of hiding complex functionality 
behind the scenes to user only showing the necessary information.

An abstract method is defined in thr abstract class but the functionality
is not implemented in  abstract class . 
and abstract method is a  base class 
basically identifies the functionality should be implemented by all of its
subclasses.However the function body is differ from sub classes 
often the abstract method in base class is define with pass keyword.
Every subclass will override this method and implement the logic on its method.

Abstract classes are  derived from the module abc and class ABC 

Note: We must should define all the methods declared in Base abstract class in all subclasses
otherwise it will throw error.

TypeError: Can't instantiate abstract class Rectangle with abstract method perimeter

"""

from abc import ABC, abstractmethod, ABCMeta


class Shape(ABC):

    # __metaclass__=  ABCMeta  optinional
    temp = 90  # class var

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def area():
        print("HII")
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display(self):
        print("display")


# abstract_obj1=Shape('square')      #Can't instantiate abstract class Shape with abstract methods area, perimeter

# print(dir(Shape))


class Square(Shape):

    def __init__(self, type, side):
        self.side = side
        Shape.__init__(self, type)

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side

    def display(self):
        print("overiding")


square_1 = Square("square", 20)
print(square_1.type)
print(square_1.area())
print(square_1.perimeter())
print(square_1.display())


class Rectangle(Shape):
    def __init__(self, type, length, breadth):
        Shape.__init__(self, type)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)


rectangle1 = Rectangle("rectangle", 20, 10)
print(rectangle1.type)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1.display())
