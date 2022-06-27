from homework_2.src.Circle import Circle
from homework_2.src.Triangle import Triangle

import pytest

class TestCircle():

    def __init__(self, radius):
        self.radius = radius


@pytest.mark.positive
def test_find_area():
    circle = Circle(5)
    assert circle.find_area == 78.53981633974483


@pytest.mark.positive
def test_find_perimeter():
    circle = Circle(5)
    assert circle.find_perimeter == 31.41592653589793


@pytest.mark.positive
def test_find_add_area():
    circle = Circle(5)
    triangle = Triangle(7, 8, 9)
    result = circle.add_area(triangle)
    assert result == 105.37263206974231


@pytest.mark.negative
def test_error_value_in_area():
    circle = Circle(5)
    square = TestCircle(10)
    result = circle.add_area(square)
    assert (str(result.value)) == 'Invalid value'


