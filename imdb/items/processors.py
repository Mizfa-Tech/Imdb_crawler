import re


# ------------------------------------- processors --------------------------------------------------------------------
def run_time(value: list[str]):
    return ''.join(value)


def validate_data(value):
    if value:
        return value
    return 'NULL'


def get_imdb_id(value):
    result = ''.join(re.findall("(tt\d+)", value))
    return result
