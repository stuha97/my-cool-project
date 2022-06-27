from homework_2.src.Figure import Figure
from homework_2.src.Rectangle import rectangle


class Square(Figure):
    def __init__(self, side1, side2):
        self.name = 'Square'
        self.side1 = side1
        self.side2 = side2
        self.find_area
        self.find_perimeter

    @property
    def find_area(self):
        return self.side1 * self.side2

    @property
    def find_perimeter(self):
        return self.side1 * 4


square = Square(15, 15)
print(square.add_area(rectangle))
