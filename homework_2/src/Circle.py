import math

from homework_2.src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"
        self.find_area
        self.find_perimeter

    @property
    def find_perimeter(self):
        return 2 * self.radius * math.pi

    @property
    def find_area(self):
        return self.radius * self.radius * math.pi


circle = Circle(5)
