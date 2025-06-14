import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 2), 7) 


    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(9, 3), 6)
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-6, 5), -11)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 4), 16)
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(-5, 6), -30)

    def test_division(self):
        self.assertEqual(self.calc.divide(25, 5), 5)
        self.assertEqual(self.calc.divide(6, 0), None)
        self.assertEqual(self.calc.divide(2, 2), 1)

if __name__ == "__main__":
    unittest.main()