#test file for flightGroupClassmk2

from traceback import StackSummary
import unittest
import flightGroupClassMk2
import exampleGroupGenerator


class TestflightGroupClass(unittest.TestCase):
    def test_init(self):
        result = flightGroupClassMk2.flightGroup("MAS", "2022-12-3", "2022-12-30", (5,7), "owenoh@email.com", [("YYZ", 3),("ZPO", 7)])
        self.assertIsInstance(result.destination, str)
        self.assertIsInstance(result.dateLowerBound, str)
        self.assertIsInstance(result.dateUpperBound, str)
        self.assertIsInstance(result.stayRange[0], int)
        self.assertIsInstance(result.stayRange[1], int)
        self.assertIsInstance(result, flightGroupClassMk2.flightGroup)
        self.assertTrue(result.stayRange[0] <= result.stayRange[1])
        # This test only checks that an instance of the class is instantiated with valid types
        # However, it will not raise an issue if the groupOrgins attribute is None


if __name__ == '__main__':
    unittest.main()