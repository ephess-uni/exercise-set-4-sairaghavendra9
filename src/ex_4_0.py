""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


import re
def get_shutdown_events(logfile):
    shutdown_events = []

    # Open the logfile
    with open(logfile, 'r') as file:
        # Read each line in the file
        for line in file:
            # Use regular expression to find shutdown events
            if re.search(r'Shutdown initiated', line, re.IGNORECASE):
                # Append the line to the shutdown_events list
                shutdown_events.append(line.strip())

    return shutdown_events

# The code below will call your function and print the results
if __name__ == "__main__":
    from util import get_data_file_path
    
    FILENAME = get_data_file_path('messages.log')
    shutdown_events = get_shutdown_events(FILENAME)
    
    if shutdown_events:
        print("Shutdown events found:")
        for event in shutdown_events:
            print(event)
    else:
        print("No shutdown events found.")
