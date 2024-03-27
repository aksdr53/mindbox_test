import unittest

from .shape_calc import ShapeCalculator

class TestShapeCalculator(unittest.TestCase):
    def test_calculate_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.calculate_circle_area(3), math.pi * 3**2, places=5)

    def test_calculate_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.calculate_triangle_area(3, 4, 5), 6.0, places=5)

    def test_is_right_triangle(self):
        self.assertTrue(ShapeCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(ShapeCalculator.is_right_triangle(2, 3, 4))

if __name__ == "__main__":
    unittest.main()