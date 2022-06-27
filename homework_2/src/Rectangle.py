from homework_2.src.Figure import Figure
from homework_2.src.Circle import circle


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.name = "Rectangle"
        self.find_area
        self.find_perimeter

    @property
    def find_area(self):
        return self.length * self.width

    @property
    def find_perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)
print(rectangle.add_area(circle))
