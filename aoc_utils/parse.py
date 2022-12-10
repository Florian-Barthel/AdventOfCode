
def parse_multi_element(filename: str, split_element: str = ' '):
    with open(filename) as f:
        for line in f.read().splitlines():
            yield list(map(convert_if_digit, line.split(split_element)))


def convert_if_digit(element: any):
    try:
        return int(element)
    except ValueError:
        pass
    try:
        return float(element)
    except ValueError:
        pass
    return element
