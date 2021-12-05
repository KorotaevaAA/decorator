from typing import Callable
import sys


def redirect_output(filepath: str) -> Callable:
    def outer_wrapper(function: Callable) -> Callable:
        def inner_wrapper():
            file = open(filepath, 'w')
            sys.stdout = file
            function()
            file.close()

        return inner_wrapper

    return outer_wrapper


@redirect_output('function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


calculate()
