class StatsGenerator:
    """
    All statistic related calculation should go here
    """

    _data = None
    _statistics = None

    def __init__(self, data):
        self._data = data
        self._statistics = {}

    def calculate_average_working_time(self):
        """
        Calculate average working time for all employees
        :return:
        """

        time_count = 0
        employee_count = 0

        for key, val in self._data.time_employee.items():
            count = len(val)
            employee_count += count
            time_count += count * key

        if employee_count == 0:
            raise ZeroDivisionError("employee_count is 0")

        # add calculation to statistics
        # this value is still in minutes so we can convert it to integer

        self._statistics['average_working_time'] = int(time_count/employee_count)

    @property
    def get_statistics(self):
        return self._statistics
