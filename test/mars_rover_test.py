import unittest

from parameterized import parameterized

from mars_rover import Rover

class MarsRoverTest(unittest.TestCase):
    def test_works(self):
        rover = Rover()
        result = rover.execute("M")
        self.assertEqual("0:0:N", result)

if __name__ == '__main__':
    unittest.main()