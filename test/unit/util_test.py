import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    
    # Tests para convert_to_number
    def test_convert_to_number_with_integers(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertEqual(100, util.convert_to_number("100"))
        self.assertEqual(-999, util.convert_to_number("-999"))

    def test_convert_to_number_with_floats(self):
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)
        self.assertAlmostEqual(3.14159, util.convert_to_number("3.14159"), delta=0.0000001)
        self.assertAlmostEqual(-2.5, util.convert_to_number("-2.5"), delta=0.0000001)

    def test_convert_to_number_with_whitespace(self):
        # Python's int() y float() aceptan strings con espacios
        self.assertEqual(4, util.convert_to_number("  4  "))
        self.assertEqual(-5, util.convert_to_number(" -5 "))
        self.assertAlmostEqual(3.14, util.convert_to_number("  3.14  "), delta=0.0000001)

    def test_convert_to_number_invalid_strings(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, " ")
        self.assertRaises(TypeError, util.convert_to_number, "abc")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, "12.34.56")
        
    def test_convert_to_number_scientific_notation(self):
        # Notación científica sin "." -> int("1e5") falla
        self.assertRaises(TypeError, util.convert_to_number, "1e5")
        self.assertRaises(TypeError, util.convert_to_number, "2e10")
        
    def test_convert_to_number_special_floats(self):
        # inf, NaN no tienen "." -> int("inf") falla
        self.assertRaises(TypeError, util.convert_to_number, "inf")
        self.assertRaises(TypeError, util.convert_to_number, "-inf")
        self.assertRaises(TypeError, util.convert_to_number, "NaN")
        
    def test_convert_to_number_with_none_and_objects(self):
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()