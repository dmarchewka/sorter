class Data():
    '''
    Place holder of all data
    '''

    raw_data = {}
    time_employee = {}
    time_sorted = []

    def __init__(self, raw_data, time_employee={}, time_sorted=[]):
        self.raw_data = raw_data
        self.time_employee = time_employee
        self.time_sorted = time_sorted