""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    shutdown_events = get_shutdown_events(logfile)

    if not shutdown_events:
        return None  # Return None if no shutdown events found

    # Convert the timestamps of the first and last shutdown events to datetime objects
    first_shutdown_time = logstamp_to_datetime(shutdown_events[0].split()[1])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1].split()[1])

    # Compute the time difference between the first and last shutdown events
    time_difference = last_shutdown_time - first_shutdown_time

    return time_difference



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    FILENAME = get_data_file_path("messages.log")
    time_diff = time_between_shutdowns(FILENAME)

    if time_diff:
        print(f"Time between first and last shutdowns: {time_diff}")
    else:
        print("No shutdown events found in the logfile.")
