#test file for flightGroupClassmk2

import unittest
import flightGroupClassMk2


class TestflightGroupClass(unittest.TestCase):
    def test_init(self):
        result = flightGroupClassMk2.flightGroup('dest', '2022-12-2','2022-12-12', 10, [('MSP', 3)])
        self.assertIsInstance(result.destination, str)
        self.assertIsInstance(result.departDate, str)
        self.assertIsInstance(result.returnDate, str)
        self.assertIsInstance(result.stayRange, int)
     
        self.assertIsInstance(result, flightGroupClassMk2.flightGroup)
        # This test only checks that an instance of the class is instantiated with valid types
        # However, it will not raise an issue if the groupOrgins attribute is None
    
    def test_from_file(self):
        result = flightGroupClassMk2.flightGroup.from_file()
        self.assertIsInstance(result.destination, str)
        self.assertIsInstance(result.departDate, str)
        self.assertIsInstance(result.returnDate, str)
        self.assertIsInstance(result.stayRange, int)
     
        self.assertIsInstance(result, flightGroupClassMk2.flightGroup)

        # Currently this will only work if the pkl file is not empty
        # I should later add a check to make certain that the file isnt empty before checking


if __name__ == '__main__':
    unittest.main()