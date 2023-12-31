import re


NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str) -> bool:
    return len(string) == 0


def isValidNumber(string: str) -> bool:
    valid = None
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def formatFloat(number: float):
    len_number = len(str(number))
    if len_number > 10:
        return number
    elif number.is_integer():
        return int(number)
    else:
        return float(number)
