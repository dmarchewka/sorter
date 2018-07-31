from unittest import TestCase
from sorter import Sorter

class TestSorter(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sorter = Sorter({'alex': 1120, 'andre': -130, 'bernhard': 3000,
                             'david': 5460, 'petra': 1120, 'olga': 1120})

    def test_create_time_employee(self):
        self.sorter.create_time_employee()
        self.assertDictEqual({1120: ['alex', 'olga', 'petra'], 3000: ['bernhard'], 5460: ['david'], -130: ['andre']},
                             self.sorter.time_employee)

    def test_quick_sort_time(self):
        self.sorter.create_time_employee()
        self.sorter.create_time_sorted()
        self.assertListEqual([5460, 3000, 1120, -130], self.sorter.time_sorted)