class FileReader:

    _file = None
    BUFFER_SIZE = 20000000 # 20MB
    result = {}

    def __init__(self, file):
        self._file = file

    def split(self, text, separators):
        '''
        Custom split method
        :param text: text to split
        :param separators: tuple of separators
        :return:
        '''
        default = separators[0]

        for separator in separators[1:]:
            text = str(text).replace(separator, default)

        return text.split(default)

    def parse(self):
        '''
        Buffering and parsing file
        :return:
        '''
        with open(self._file, buffering=self.BUFFER_SIZE) as f:
            for line in f:
                list = self.split(line, (',', ';'))
                for item in list:
                    key, val = [x.strip().lower() for x in item.split(':')]
                    val = int(val)
                    if self.result.has_key(key):
                        self.result[key] += val
                    else:
                        self.result[key] = val