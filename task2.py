from typing import Callable
from datetime import datetime
import sys


def timed_output(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        current_datetime = str(datetime.now())
        sys.stdout.write(f'[{current_datetime}]: ')
        function(*args, **kwargs)
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


print_greeting('Anna')