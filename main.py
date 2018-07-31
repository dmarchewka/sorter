from data import Data
from fIleReader import FileReader
from fileWriter import FileWriter
from sorter import Sorter
from stats import StatsGenerator
from os import path, getcwd

class Main():

    file_path = path.join(getcwd(), 'test_data', 'test_data.txt')

    def run(self):
        # Read file
        file_reader = FileReader(self.file_path)
        file_reader.parse()

        # Store output in data object
        data = Data(raw_data=file_reader.result)

        # Sort data
        sorter = Sorter(raw_data=file_reader.result)
        sorter.create_time_employee()
        sorter.create_time_sorted()

        # Store sorted data in data object
        data.time_employee = sorter.time_employee
        data.time_sorted = sorter.time_sorted

        # Create statistics
        stats = StatsGenerator(data)
        stats.get_average_working_time()

        # Write data to files
        file_writer = FileWriter(data, stats.statistics)
        file_writer.create_stats_output()
        file_writer.create_data_output()
        file_writer.write2json()
        file_writer.write2cvs()

if __name__ == '__main__':
    obj = Main()
    obj.run()