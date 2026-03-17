import math

class Shape:
    count = 0
    def __init__(self):
        self.__area = 0.0
        self.__perimeter = 0.0
        Shape.count += 1

    @property
    def area(self):
        return round(self.__area, 2)

    @property
    def perimeter(self):
        return round(self.__perimeter, 2)

    def _set_area(self, area):
        self.__area = area

    def _set_perimeter(self, perimeter):
        self.__perimeter = perimeter


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = radius
        self._calc_area()
        self._calc_perimeter()

    def _calc_area(self):
        self._set_area(math.pi * self._radius**2)

    def _calc_perimeter(self):
        self._set_perimeter(2 * math.pi * self._radius)

    @property
    def radius(self):
        return round(self._radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        if (not isinstance(width, (int, float)) or width < 0 or
            not isinstance(height, (int, float)) or height < 0 ):
            raise ValueError("Width and height must be a positive number")
        self._width = width
        self._height = height
        self._calc_area()
        self._calc_perimeter()

    def _calc_area(self):
        area = self._width * self._height
        self._set_area(area)

    def _calc_perimeter(self):
        perimeter = 2 * (self._width + self._height)
        self._set_perimeter(perimeter)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._side = side

    @property
    def side(self):
        return self._side


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        if (not all(isinstance(i, (int, float)) for i in [a, b, c])
            or a < 0 or b < 0 or c < 0):
            raise ValueError("Sides must be positive numbers")
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid sides for a triangle")

        self._a = a
        self._b = b
        self._c = c
        self._calc_area()
        self._calc_perimeter()

    def _calc_area(self):
        s = (self._a + self._b + self._c) / 2
        area = math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))
        self._set_area(area)

    def _calc_perimeter(self):
        perimeter = self._a + self._b + self._c
        self._set_perimeter(perimeter)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c




circle = Circle(5)
print('圆的面积为：', circle.area)
print('圆的周长为：', circle.perimeter)
print('圆的半径为：', circle.radius, end='\n\n')

rectangle = Rectangle(2, 5)
print('矩形的面积为：', rectangle.area)
print('矩形的周长为：', rectangle.perimeter)
print('矩形的宽为：', rectangle.width)
print('矩形的高为：', rectangle.height, end='\n\n')

square = Square(5)
print('正方形的面积为：', square.area)
print('正方形的周长为：', square.perimeter)
print('正方形的边长为：', square.side, end='\n\n')

triangle = Triangle(3, 4, 5)
print('三角形的面积为：', triangle.area)
print('三角形的周长为：', triangle.perimeter)
print('三角形的边长为: ', triangle.a)
print('三角形的边长为: ', triangle.b)
print('三角形的边长为: ', triangle.c)


