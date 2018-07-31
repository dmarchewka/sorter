from unittest import TestCase
from data import Data
from fileWriter import FileWriter
from collections import OrderedDict
from os import path, getcwd

class TestFileWrtier(TestCase):

    @classmethod
    def setUpClass(cls):
        data = Data({'alex': 1120, 'andre': -130, 'bernhard': 3000,
                     'david': 5460, 'petra': 1120, 'olga': 1120},
                    {1120: ['alex', 'olga', 'petra'], 3000: ['bernhard'], 5460: ['david'], -130: ['andre']},
                    [5460, 3000, 1120, -130])
        cls.fileWriter = FileWriter(data, {'average_working_time': 1948})

    def setUp(self):
        self.fileWriter._output = OrderedDict()

    def test_convert2hours(self):
        self.assertEqual('1.0', self.fileWriter.convert2hours(60))
        self.assertEqual('1.3', self.fileWriter.convert2hours(75))
        self.assertEqual('-1.3', self.fileWriter.convert2hours(-75))
        self.assertEqual('0.0', self.fileWriter.convert2hours(0))

    def test_create_stats_output(self):
        self.fileWriter.create_stats_output()
        self.assertDictEqual({'statistics': [{'average_working_time': '32.5'}]}, self.fileWriter._output)

    def test_create_data_output(self):
        self.fileWriter.create_data_output()
        self.assertDictEqual({'employees': [{'name': 'david', 'time': '91.0'},
                                            {'name': 'bernhard', 'time': '50.0'},
                                            {'name': 'alex', 'time': '18.7'},
                                            {'name': 'olga', 'time': '18.7'},
                                            {'name': 'petra', 'time': '18.7'},
                                            {'name': 'andre', 'time': '-2.2'}]}, self.fileWriter._output)

    def get_file_content(self, file):
        with open(file, 'rb') as f:
            content = f.read()
        return content.strip()

    def test_write(self):
        self.fileWriter.create_stats_output()
        self.fileWriter.create_data_output()

        self.fileWriter.write2json()
        self.fileWriter.write2cvs()

        file_json = path.join(getcwd(), self.fileWriter._file_name + '.json')
        file_csv = path.join(getcwd(), self.fileWriter._file_name + '.csv')

        self.assertTrue(path.exists(file_json))
        self.assertTrue(path.exists(file_csv))

        json_content = '''{"statistics": [{"average_working_time": "32.5"}], "employees": [{"name": "david", "time": "91.0"}, {"name": "bernhard", "time": "50.0"}, {"name": "alex", "time": "18.7"}, {"name": "olga", "time": "18.7"}, {"name": "petra", "time": "18.7"}, {"name": "andre", "time": "-2.2"}]}'''

        self.assertEqual(json_content, self.get_file_content(file_json))

        cvs_content = '''statistics
average_working_time,32.5;
employees
david,91.0;
bernhard,50.0;
alex,18.7;
olga,18.7;
petra,18.7;
andre,-2.2;'''

        self.assertEqual(cvs_content, self.get_file_content(file_csv))

