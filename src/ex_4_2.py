""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    date_format = '%Y-%m-%dT%H:%M:%S'

    # Parse the datestr using datetime.strptime() with the defined format
    datetime_obj = datetime.strptime(datestr, date_format)

    return datetime_obj


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    datetime_result = logstamp_to_datetime(test_date)
    print(f'{logstamp_to_datetime(test_date)=}')
    print(f'Datetime object: {datetime_result}')
