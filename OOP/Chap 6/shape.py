from math import pi, sqrt
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area = self.width * self.height
        return self.area

    def perimeter(self):
        self.perimeter = 2 * (self.height + self.width)
        return self.perimeter

class Circle(Shape):
    def __init__(self, raidus):
        self.radius = raidus

    def area(self):
        self.area = pi * (self.radius ** 2)
        return self.area

    def perimeter(self):
        self.perimeter = 2 * pi * self.radius
        return self.perimeter

class Equilateraltriangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        self.area = sqrt(3) / 4 * (self.side ** 2)

    def perimeter(self):
        self.perimeter = self.area * 3
        return self.perimeter


class Paint:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("추가할 수 없습니다.")