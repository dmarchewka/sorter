class Sorter():

    _raw_data = {}
    time_employee = {}
    time_sorted = []

    def __init__(self, raw_data):
        self._raw_data = raw_data

    def create_time_employee(self):
        '''
        Creates dictionary where key represents time worked and value is a list of names of the employees
        :return:
        '''
        for key, val in self._raw_data.items():
            if self.time_employee.has_key(val):
                self.time_employee[val].append(key)
            else:
                self.time_employee[val] = [key,]

    def quick_sort_time(self):
        '''
        Python implementation of quick sort algorithm for better performance
        :return:
        '''
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr

            pivot = arr[0]

            return quick_sort([x for x in arr if x > pivot]) + [pivot,] + quick_sort([x for x in arr if x < pivot])

        self.time_sorted = quick_sort(self.time_employee.keys())