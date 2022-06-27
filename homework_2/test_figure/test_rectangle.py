from homework_2.src.Rectangle import Rectangle
from homework_2.src.Circle import Circle

import pytest


class TestRectangle():

    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.raduis = radius

@pytest.mark.positive
def test_find_area():
    rectangle = Rectangle(10, 5)
    assert rectangle.find_area == 50


@pytest.mark.positive
def test_find_perimeter():
    rectangle = Rectangle(10, 5)
    assert rectangle.find_perimeter == 30


@pytest.mark.positive
def test_find_add_area():
    rectangle = Rectangle(10, 5)
    circle = Circle(5)
    result = rectangle.add_area(circle)
    assert result == 128.53981633974485


@pytest.mark.negative
def test_error_value_in_area():
    rectangle = Rectangle(10, 5)
    square = TestRectangle(10, 5, 111)
    result = rectangle.add_area(square)
    assert (str(result.value)) == 'Invalid value'