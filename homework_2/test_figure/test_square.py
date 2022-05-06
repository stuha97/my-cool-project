from homework_2.src.Square import Square
from homework_2.src.Rectangle import Rectangle

import pytest


class TestSquare():

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


@pytest.mark.positive
def test_find_area():
    square = Square(15, 15)
    assert square.find_area == 225


@pytest.mark.positive
def test_find_perimeter():
    square = Square(15, 15)
    assert square.find_perimeter == 60


@pytest.mark.positive
def test_find_add_area():
    square = Square(15, 15)
    rectangle = Rectangle(10, 5)
    result = square.add_area(rectangle)
    assert result == 275


@pytest.mark.negative
def test_error_value_in_area():
    with pytest.raises(ValueError):
        square = Square(15, 15)
        triangle = TestSquare(7, 8, 9)
        result = square.add_area(triangle)
        assert (str(result.value)) == 'Invalid value'
