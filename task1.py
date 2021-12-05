import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    current_datetime = str(datetime.now())
    return original_write(f'[{current_datetime}]: {string_text}')


sys.stdout.write = my_write

string_for_write = 'Hello, my friend!'
# original_write(string_for_write)
sys.stdout.write(string_for_write)

