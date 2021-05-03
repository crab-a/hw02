def mean(values):
    """
    calculate the mean of all values in the iterable 'values'
    :param values: iterable containing numbers(int/float/double)
    :return: the meanRR
    """
    total = sum(values)
    length = len(values)
    return total / length


def median(values):
    """
    calculate the median of all values in the iterable 'values'
    :param values: iterable containing numbers(int/float/double)
    :return: the medianR
    """
    length = len(values)
    sorted_values = sorted(values)
    med = 0
    if length % 2:
        return sorted_values[int(length / 2)]
    return (sorted_values[int(length / 2)] + sorted_values[int((length / 2)) - 1]) / 2
