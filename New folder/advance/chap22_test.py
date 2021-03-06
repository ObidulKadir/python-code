
import unittest
from UnitTesting import msmath
from UnitTesting import msstring


class MsPackMsMathTestCase(unittest.TestCase):
    def test_sum(self):
        sum = msmath.sum(8, 12)
        self.assertEqual(sum, 20)

    def test_subtract(self):
        result = msmath.subtract(109, 9)
        self.assertTrue(result == 100)

    def test_multiplication(self):
        result = msmath.multiplication(9, 3)
        self.assertEqual(result, 27)

        result = msmath.multiplication(100, 3)
        self.assertEqual(result, 300)

    def test_division(self):
        result = msmath.division(50, 25)
        self.assertEqual(result, 2)


class MsPackMsStringTestCase(unittest.TestCase):
    def test_full_name(self):
        name = msstring.MsName("Life", "Good").full_name()
        self.assertEqual("Life Good", name)


class MsPackMsString1TestCase(unittest.TestCase):
    def setUp(self):  # setUp U is in uppercase
        self.str_obj = msstring.MsName("Life", "Good")

    def test_full_name(self):
        name = self.str_obj.full_name()
        self.assertEqual("Life Good", name)

    def test_full_name_length(self):
        length = len(self.str_obj.full_name())
        self.assertTrue(length == 9)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
