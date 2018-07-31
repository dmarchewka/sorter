class StatsGenerator():
    '''
    All statistic related calculation should go here
    '''

    _data = None
    statistics = {}

    def __init__(self, data):
        self._data = data

    def get_average_working_time(self):
        '''
        Calculate average working time for all employees
        :return:
        '''

        time_count = 0
        employee_cout = 0

        for key, val in self._data.time_employee.items():
            count = len(val)
            employee_cout += count
            time_count += count * key

        # add calculation to statistics
        # this value is still in minutes so we can convert it to integer
        self.statistics['average_working_time'] = int(time_count/employee_cout)

