import unittest
import task
import random
import math
import datetime


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

    def testFirstLast(self):
        list1 = []
        expected = []
        self.assertEqual(expected, task.firstAndLast(list1))
        list1 = [123]
        expected = [123, 123]
        self.assertEqual(expected, task.firstAndLast(list1))
        list1 = [111, 222]
        expected = [111, 222]
        self.assertEqual(expected, task.firstAndLast(list1))
        list1 = [111, 222, 333, 99]
        expected = [111, 99]
        self.assertEqual(expected, task.firstAndLast(list1))

    def testDaysBetween(self):
        date1 = datetime.date(2020, 3, 1)
        date2 = datetime.date(2020, 3, 1)
        self.assertEqual(0, task.daysBetween(date1, date2))
        date1 = datetime.date(2020, 3, 1)
        date2 = datetime.date(2020, 3, 2)
        self.assertEqual(1, task.daysBetween(date1, date2))
        date1 = datetime.date(2019, 3, 1)
        date2 = datetime.date(2020, 3, 1)
        self.assertEqual(366, task.daysBetween(date1, date2))
        date1 = datetime.date(2019, 3, 1)
        date2 = datetime.date(2018, 3, 1)
        self.assertEqual(365, task.daysBetween(date1, date2))
        date1 = datetime.date(2019, 12, 31)
        date2 = datetime.date(2020, 3, 1)
        self.assertEqual(31+29+1, task.daysBetween(date1, date2))

    if __name__ == '__main__':
        unittest.main()
