from unittest import TestCase
from data import Data
from fileWriter import FileWriter
from collections import OrderedDict
from os import path, getcwd
import json


class TestFileWriter(TestCase):

    @classmethod
    def setUpClass(cls):
        data = Data({'alex': 1120, 'andre': -130, 'bernhard': 3000,
                     'david': 5460, 'petra': 1120, 'olga': 1120},
                    {1120: ['alex', 'olga', 'petra'], 3000: ['bernhard'], 5460: ['david'], -130: ['andre']},
                    [5460, 3000, 1120, -130])
        cls.fileWriter = FileWriter(data, {'average_working_time': 1948})

    @staticmethod
    def get_file_content(file_name):
        with open(file_name, 'rb') as f:
            content = f.read()
        return content.strip()

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

    def test_write(self):
        self.fileWriter.create_stats_output()
        self.fileWriter.create_data_output()

        self.fileWriter.write2json()
        self.fileWriter.write2cvs()

        file_json = path.join(getcwd(), self.fileWriter._file_name + '.json')
        file_csv = path.join(getcwd(), self.fileWriter._file_name + '.csv')

        self.assertTrue(path.exists(file_json))
        self.assertTrue(path.exists(file_csv))

        json_content = json.loads('''  {"statistics": [{"average_working_time": "32.5"}], "employees": [{"name": "david", "time": "91.0"}, {"name": "bernhard", "time": "50.0"}, {"name": "alex", "time": "18.7"}, 
                            {"name": "olga", "time": "18.7"}, {"name": "petra", "time": "18.7"}, {"name": "andre", "time": "-2.2"}]}''')

        self.assertDictEqual(json_content, json.loads(self.get_file_content(file_json)))

        cvs_content = '''statistics\r\naverage_working_time,32.5;\nemployees\r\ndavid,91.0;\nbernhard,50.0;\nalex,18.7;\nolga,18.7;\npetra,18.7;\nandre,-2.2;'''

        self.assertEqual(cvs_content, self.get_file_content(file_csv))

    def test_emtpy_stats(self):
        empty_data = FileWriter({})
        self.assertDictEqual({}, empty_data._stats)