import unittest
import pytest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Tests para ADD
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(-3, self.calc.add(-1, -2))
        self.assertAlmostEqual(4.5, self.calc.add(2.2, 2.3), delta=0.0000001)

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # Tests para SUBSTRACT
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))
        self.assertEqual(-1, self.calc.substract(0, 1))
        self.assertAlmostEqual(0.5, self.calc.substract(2.5, 2.0), delta=0.0000001)

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)

    # Tests para MULTIPLY
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(6, self.calc.multiply(2, 3))
        self.assertAlmostEqual(6.25, self.calc.multiply(2.5, 2.5), delta=0.0000001)

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)

    # Tests para DIVIDE
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(-1, self.calc.divide(2, -2))
        self.assertEqual(-2, self.calc.divide(-4, 2))
        self.assertAlmostEqual(2.5, self.calc.divide(5, 2), delta=0.0000001)

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, -5, 0)

    # Tests para POWER
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0, self.calc.power(0, 5))
        self.assertAlmostEqual(0.5, self.calc.power(2, -1), delta=0.0000001)
        self.assertAlmostEqual(9, self.calc.power(3, 2), delta=0.0000001)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)

    # Tests para SQUARE_ROOT
    def test_square_root_method_returns_correct_result(self):
        self.assertAlmostEqual(2, self.calc.square_root(4), delta=0.0000001)
        self.assertAlmostEqual(3, self.calc.square_root(9), delta=0.0000001)
        self.assertAlmostEqual(5, self.calc.square_root(25), delta=0.0000001)
        self.assertAlmostEqual(0, self.calc.square_root(0), delta=0.0000001)
        self.assertAlmostEqual(1, self.calc.square_root(1), delta=0.0000001)
        self.assertAlmostEqual(1.414213, self.calc.square_root(2), delta=0.0001)

    def test_square_root_method_fails_with_negative_number(self):
        self.assertRaises(ValueError, self.calc.square_root, -1)
        self.assertRaises(ValueError, self.calc.square_root, -4)
        self.assertRaises(ValueError, self.calc.square_root, -100)

    def test_square_root_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, "4")
        self.assertRaises(TypeError, self.calc.square_root, None)
        self.assertRaises(TypeError, self.calc.square_root, object())

    # Tests para LOG10
    def test_log10_method_returns_correct_result(self):
        self.assertAlmostEqual(0, self.calc.log10(1), delta=0.0000001)
        self.assertAlmostEqual(1, self.calc.log10(10), delta=0.0000001)
        self.assertAlmostEqual(2, self.calc.log10(100), delta=0.0000001)
        self.assertAlmostEqual(3, self.calc.log10(1000), delta=0.0000001)
        self.assertAlmostEqual(0.30103, self.calc.log10(2), delta=0.0001)

    def test_log10_method_fails_with_non_positive_number(self):
        self.assertRaises(ValueError, self.calc.log10, 0)
        self.assertRaises(ValueError, self.calc.log10, -1)
        self.assertRaises(ValueError, self.calc.log10, -10)

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "10")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()