from os import path, getcwd
import random
import string

file_path = path.join(getcwd(), 'test_data', 'test_data.txt')


def random_employee():
    name = ''.join((random.choice(string.ascii_uppercase) for _ in range(4)))
    hours = random.randint(-9999,9999)
    return "%s:%s" % (name, hours)

with open(file_path, 'wb') as f:
    while(path.getsize(file_path) >> 20) < 20:
        f.write(','.join(random_employee() for _ in range(100)))
        f.write('\n')