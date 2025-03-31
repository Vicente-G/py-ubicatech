def ignore_wildcard(element):
    return element != "*"


def remove_nulls(element):
    return element[1] is not None
