import unittest
import random
import math
from tests.homework import (
    Rectangle
)


class RectanglePerimeterSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.width = random.randint(1, 100)
        self.height = random.randint(1, 100)

    def test_get_rectangle_perimeter(self):
        given_result = Rectangle(self.width, self.height).get_rectangle_perimeter()
        expected_result = (self.width + self.height) * 2
        self.assertEqual(given_result, expected_result)

    def test_get_rectangle_square(self):
        given_result = Rectangle(self.height, self.width).get_rectangle_square()
        expected_result = self.height * self.width
        self.assertEqual(given_result, expected_result)


class SumOfCorners(unittest.TestCase):

    def test_get_sum_of_corners(self):
        for no_of_corners in range(1, 5):
            given_result = Rectangle(10, 20).get_sum_of_corners(no_of_corners)
            expected_result = 90 * no_of_corners
            self.assertEqual(given_result, expected_result)

    def test_no_of_corners_more_than_4(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5).get_sum_of_corners(5)


class Diagonal(unittest.TestCase):

    def test_get_rectangle_diagonal(self):
        given_data = [(1, 3), (4, 6), (7, 9), (4, 10)]
        for (given_width, given_height) in given_data:
            given_result = Rectangle(given_width, given_height).get_rectangle_diagonal()
            expected_result = math.sqrt(math.pow(given_height, 2) + math.pow(given_width, 2))
            self.assertEqual(given_result, expected_result)


class RadiusOfCircumscribedCircle(unittest.TestCase):

    def test_get_radius_of_circumscribed_circle(self):
        rect = Rectangle(10, 5)
        given_result = rect.get_radius_of_circumscribed_circle()
        expected_result = rect.get_rectangle_diagonal()/2
        self.assertEqual(given_result, expected_result)


class RadiusOfInscribedCircle(unittest.TestCase):

    def test_get_radius_of_inscribed_circle(self):
        rect = Rectangle(10, 10)
        given_result = rect.get_radius_of_inscribed_circle()
        expected_result = rect.get_rectangle_diagonal()/(2 * math.sqrt(2))
        self.assertEqual(given_result, expected_result)

    def test_equal_sides(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 15)
            rect.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
