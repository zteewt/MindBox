import unittest
from Figure_square import Figure_square

class SquareTest(unittest.TestCase):
    def setUp(self):
        self.Figure_square = Figure_square()
    def test_circle_square(self):
        self.assertEqual(self.Figure_square.circle_square(5), 78.54)
    def test_triangle_square(self):
        self.assertEqual(self.Figure_square.triangle_square(14, 13, 15), 84)
    def test_is_rectangular(self):
        self.assertEqual(self.Figure_square.is_rectangular(3, 4, 5), "Треугольник прямоугольный")

if __name__ == "__main__":
  unittest.main()