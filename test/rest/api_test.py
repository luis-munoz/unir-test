import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # Test para la ruta raíz
    def test_api_root(self):
        # Remover la barra final para evitar el redirect 308
        base = BASE_URL.rstrip('/')
        url = f"{base}/"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertIn("Hello", content)

    # Tests para ADD
    def test_api_add(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual("4", content)

    def test_api_add_negative_numbers(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/add/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertEqual("0", content)

    def test_api_add_floats(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/add/2.5/2.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(5.0, float(content), delta=0.0001)

    def test_api_add_invalid_parameters(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/add/abc/2"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # Tests para SUBSTRACT
    def test_api_substract(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertEqual("2", content)

    def test_api_substract_negative_result(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/substract/2/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertEqual("-3", content)

    def test_api_substract_floats(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/substract/5.5/2.5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(3.0, float(content), delta=0.0001)

    def test_api_substract_invalid_parameters(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/substract/xyz/2"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # Tests para MULTIPLY
    def test_api_multiply(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertEqual("12", content)

    def test_api_multiply_by_zero(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/multiply/5/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertEqual("0", content)

    def test_api_multiply_negative(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/multiply/-2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertEqual("-6", content)

    def test_api_multiply_floats(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/multiply/2.5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(5.0, float(content), delta=0.0001)

    def test_api_multiply_invalid_parameters(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/multiply/abc/2"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # Tests para DIVIDE
    def test_api_divide(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(5.0, float(content), delta=0.0001)

    def test_api_divide_with_decimals(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/divide/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(2.5, float(content), delta=0.0001)

    def test_api_divide_negative(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/divide/-10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(-5.0, float(content), delta=0.0001)

    def test_api_divide_by_zero(self):
        """Test que verifica que la división por cero retorna BAD_REQUEST"""
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/divide/5/0"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    def test_api_divide_invalid_parameters(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/divide/abc/2"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # Tests para POWER
    def test_api_power(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(8.0, float(content), delta=0.0001)

    def test_api_power_to_zero(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/power/5/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(1.0, float(content), delta=0.0001)

    def test_api_power_negative_exponent(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/power/2/-1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(0.5, float(content), delta=0.0001)

    def test_api_power_floats(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/power/2.5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(6.25, float(content), delta=0.0001)

    def test_api_power_invalid_parameters(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/power/abc/2"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # Tests para SQUARE_ROOT
    def test_api_square_root(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/square_root/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(2.0, float(content), delta=0.0001)

    def test_api_square_root_of_nine(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/square_root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(3.0, float(content), delta=0.0001)

    def test_api_square_root_of_zero(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/square_root/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(0.0, float(content), delta=0.0001)

    def test_api_square_root_negative_number(self):
        """Test que verifica que sqrt de número negativo retorna BAD_REQUEST"""
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/square_root/-4"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    def test_api_square_root_invalid_parameter(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/square_root/abc"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # Tests para LOG10
    def test_api_log10(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(1.0, float(content), delta=0.0001)

    def test_api_log10_of_100(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(2.0, float(content), delta=0.0001)

    def test_api_log10_of_1(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/log10/1"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
        content = response.read().decode('utf-8')
        self.assertAlmostEqual(0.0, float(content), delta=0.0001)

    def test_api_log10_of_zero(self):
        """Test que verifica que log10(0) retorna BAD_REQUEST"""
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/log10/0"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    def test_api_log10_of_negative(self):
        """Test que verifica que log10 de número negativo retorna BAD_REQUEST"""
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/log10/-10"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    def test_api_log10_invalid_parameter(self):
        base = BASE_URL.rstrip('/')
        url = f"{base}/calc/log10/abc"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()