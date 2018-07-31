import json
import csv
from os import path, getcwd, linesep
from collections import OrderedDict

class FileWriter():

    _data = None
    _stats = None
    _output = OrderedDict()
    _file_name = 'output'

    def __init__(self, data, stats={}):
        self._data = data
        self._stats = stats

    def convert2hours(self, minutes):
        '''
        Convert minutes to hours
        :param minutes:
        :return:
        '''
        return "{0:.1f}".format(round(float(minutes)/60, 1))

    def create_stats_output(self):
        '''
        Create list of all statistics
        :return:
        '''
        tmp = []
        for key, val in self._stats.items():
            tmp.append({ key: self.convert2hours(val)})
        self._output['statistics'] = tmp

    def create_data_output(self):
        '''
        Create list of dictionaries with all employees
        :return:
        '''
        tmp = []
        for key in self._data.time_sorted:
            for employee in self._data.time_employee[key]:
                tmp.append({'name': employee, 'time': self.convert2hours(key)})
        self._output['employees'] = tmp

    def write2json(self):
        '''
        Handle writing to json file
        :return:
        '''
        output_path = path.join(getcwd(), self._file_name + '.json')
        with open(output_path, 'wb') as f:
            json.dump(self._output, f)

    def write2cvs(self):
        '''
        Handle writing to csv file with custom line separators
        :return:
        '''
        output_path = path.join(getcwd(), self._file_name + '.csv')
        line_separator = ';'+linesep
        with open(output_path, 'wb') as f:
            writer_header = csv.writer(f)
            writer_rows = csv.writer(f, lineterminator=';'+linesep)
            dict_writer = csv.DictWriter(f, ('name', 'time'), lineterminator=line_separator)
            for key, val in self._output.items():
                writer_header.writerow((key, ))
                for item in val:
                    if item.has_key('name'):
                        dict_writer.writerow(item)
                    else:
                        writer_rows.writerow(item.items()[0])
