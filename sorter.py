from numpy import array
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r %2.2f sec' % \
              (method.__name__, te-ts)
        return result

    return timed


class Sorter:

    _raw_data = None
    time_employee = None
    time_sorted = None

    def __init__(self, raw_data):
        self._raw_data = raw_data
        self.time_sorted = []
        self.time_employee = {}

    def create_time_employee(self):
        """
        Creates dictionary where key represents time worked and value is a list of names of the employees
        :return:
        """
        for key, val in self._raw_data.items():
            if val in self.time_employee.keys():
                self.time_employee[val].append(key)
            else:
                self.time_employee[val] = [key,]

    @timeit
    def create_time_sorted(self):
        """
        Using numpy array.sort that uses quick sort algorithm
        :return:
        """
        arr = array(self.time_employee.keys())
        arr.sort()
        self.time_sorted = list(arr[::-1].flat[:])
