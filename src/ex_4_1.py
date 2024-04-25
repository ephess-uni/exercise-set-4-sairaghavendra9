""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def num_shutdowns(logfile):
    shutdown_events = get_shutdown_events(logfile)
    num_shutdowns = len(shutdown_events) // 2

    return num_shutdowns



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    FILENAME = get_data_file_path('messages.log')
    num_of_shutdowns = num_shutdowns(FILENAME)
    print(f'Number of shutdowns: {num_of_shutdowns}')
