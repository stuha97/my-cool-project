from homework_2.src.Triangle import Triangle
from homework_2.src.Square import Square

import pytest


class TestTriangle():

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


@pytest.mark.positive
def test_find_area():
    triangle = Triangle(7, 8, 9)
    assert triangle.find_area == 26.832815729997478


@pytest.mark.positive
def test_find_perimeter():
    triangle = Triangle(7, 8, 9)
    assert triangle.find_perimeter == 24


@pytest.mark.positive
def test_find_add_area():
    triangle = Triangle(7, 8, 9)
    square = Square(15, 15)
    result = triangle.add_area(square)
    assert result == 251.8328157299975


@pytest.mark.negative
def test_error_value_in_area():
    with pytest.raises(ValueError):
        triangle = Triangle(7, 8, 9)
        rectangle = TestTriangle(10, 5, 21)
        result = triangle.add_area(rectangle)
        assert (str(result.value)) == 'Invalid value'
