import unittest
import task
import random
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testCircleArea(self):
        expected = 0
        self.assertEqual(expected, task.circleArea(0))
        i = 0
        while i < 10000:
            r = random.uniform(-10.0, 10.0)
            if r < 0:
                expected = None
            else:
                expected = math.pi*r**2
            self.assertAlmostEqual(expected, task.circleArea(r), places=8)
            i = i + 1

    if __name__ == '__main__':
        unittest.main()

