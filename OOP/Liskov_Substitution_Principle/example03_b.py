class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square:
    def __init__(self, side):
        self._side = side

    def area(self):
        return self._side * self._side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value if value > 0 else 1



# 행동규약을 지킬 수 있는지 확인하고 상속할 것
'''
    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1
'''

rectangle_1 = Rectangle(4, 6)
square_1 = Square(2)

rectangle_1.width = 3
rectangle_1.height = 7

print(rectangle_1.area())

square_1.side = 10


print(square_1.area())