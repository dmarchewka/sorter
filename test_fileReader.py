from unittest import TestCase
from fIleReader import FileReader
from os import path, getcwd


class TestFileReader(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_reader = FileReader(path.join(getcwd(), 'test_data', 'test_data.txt'))

    def test_buffer(self):
        self.assertEqual(20000000, self.file_reader.BUFFER_SIZE)

    def test_split(self):
        text = 'a,b;c.d'
        separators = (',', ';', '.')
        self.assertListEqual(['a', 'b', 'c', 'd'], self.file_reader.split(text, separators))

    def test_parse(self):
        self.file_reader.parse()
        self.assertDictEqual({'alex': 1120, 'andre': -130, 'bernhard': 3000,
                              'david': 5460, 'petra': 1120, 'olga': 1120},
                             self.file_reader.result)
