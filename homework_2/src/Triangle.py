from homework_2.src.Figure import Figure
from homework_2.src.Square import square

import math


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.name = "Triangle"
        self.find_area
        self.find_perimeter

    @property
    def find_perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def half_of_perimeter(self):
        return self.find_perimeter / 2

    @property
    def find_area(self):
        return math.sqrt(self.half_of_perimeter * (self.half_of_perimeter - self.side1) *
                         (self.half_of_perimeter - self.side2) * (self.half_of_perimeter - self.side3))


triangle = Triangle(7, 8, 9)
print(triangle.add_area(square))
