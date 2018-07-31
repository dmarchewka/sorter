from unittest import TestCase
from data import Data
from stats import StatsGenerator

class TestStatsGenerator(TestCase):

    @classmethod
    def setUpClass(cls):
        data = Data({'alex': 1120, 'andre': -130, 'bernhard': 3000,
                     'david': 5460, 'petra': 1120, 'olga': 1120},
                    {1120: ['alex', 'olga', 'petra'], 3000: ['bernhard'], 5460: ['david'], -130: ['andre']},
                     [5460, 3000, 1120, -130])
        cls.stats = StatsGenerator(data)

    def test_get_average_working_time(self):
        self.stats.get_average_working_time()
        self.assertDictEqual({'average_working_time': 1948}, self.stats.statistics)