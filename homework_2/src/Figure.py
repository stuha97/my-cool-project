class Figure:

    def __init__(self):
        self.find_area = None

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.find_area + figure.find_area
        else:
            raise ValueError("Invalid value")
