import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------------------------
    # Tests for addition
    # ---------------------------
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # ---------------------------
    # Tests for subtraction
    # ---------------------------
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)

    # ---------------------------
    # Tests for multiplication
    # ---------------------------
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    # ---------------------------
    # Tests for division
    # ---------------------------
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # ---------------------------
    # Optional: Edge / Precision Cases
    # ---------------------------
    def test_division_precision(self):
        """Test floating point precision behavior."""
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 0.3333, places=4)


if __name__ == "__main__":
    unittest.main()
