#Script unittest dari ChatGPT

import unittest

class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5)  # Pass: 3 + 2 = 5

    def test_assertNotEqual(self):
        self.assertNotEqual(3 + 2, 6)  # Pass: 3 + 2 != 6

    def test_assertTrue(self):
        self.assertTrue(5 > 3)  # Pass: 5 > 3 is True

    def test_assertFalse(self):
        self.assertFalse(3 > 5)  # Pass: 3 > 5 is False

    def test_assertIs(self):
        a = b = [1, 2, 3]
        self.assertIs(a, b)  # Pass: a and b refer to the same object

    def test_assertIsNot(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertIsNot(a, b)  # Pass: a and b are not the same object

    def test_assertIsNone(self):
        value = None
        self.assertIsNone(value)  # Pass: value is None

    def test_assertIsNotNone(self):
        value = 42
        self.assertIsNotNone(value)  # Pass: value is not None

    def test_assertIn(self):
        self.assertIn(3, [1, 2, 3, 4])  # Pass: 3 is in the list

    def test_assertNotIn(self):
        self.assertNotIn(5, [1, 2, 3, 4])  # Pass: 5 is not in the list

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(3.14159, 3.1416, places=4)  # Pass: Rounded to 4 places

    def test_assertNotAlmostEqual(self):
        self.assertNotAlmostEqual(3.14159, 3.15, places=2)  # Pass: Not equal at 2 places

    def test_assertRaises(self):
        with self.assertRaises(ZeroDivisionError):  # Pass: Division by zero raises ZeroDivisionError
            _ = 1 / 0

    def test_assertRaisesWithFunction(self):
        def divide(a, b):
            return a / b
        self.assertRaises(ZeroDivisionError, divide, 1, 0)  # Pass: divide(1, 0) raises ZeroDivisionError

# Jalankan jika file ini dijalankan langsung
if __name__ == '__main__':
    unittest.main()
