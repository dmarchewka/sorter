class Data:
    """
    Place holder of all data
    """

    raw_data = None
    time_employee = None
    time_sorted = None

    def __init__(self, raw_data, time_employee=None, time_sorted=None):
        self.raw_data = raw_data
        if time_employee is None:
            time_employee = {}
        if time_sorted is None:
            time_sorted = []
        self.time_employee = time_employee
        self.time_sorted = time_sorted
