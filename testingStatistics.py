# Testing of the statistics abstract data type

import Statistics as S

a = 0.1 + 0.1 + 0.1
b = 0.3
tolerance = 0.001


def close_enough(check_a, check_b, check_tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to be considered equal
    Pre-Conditions:
        :param check_a: a floating point value
        :param check_b: a floating point value
        :param check_tolerance: a small positive floating point value
    Return:
        :return True if the difference between a and b is small
    """
    return abs(check_a - check_b) < check_tolerance


if not close_enough(a, b, tolerance):
    print("The difference between a and b is too large")
else:
    pass


def test():
    # test Statistics.create()
    test_item = 'Statistics.create()'
    expected = 0
    reason = "Initial count value"

    # call the operation
    stats = S.Statistics()
    result = stats.count()

    if result != expected:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    expected = 0
    reason = "Initial average value"

    # call the operation
    stats = S.Statistics()
    result = stats.mean()

    if result != expected:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    #####################################################################
    # Testing the add value
    expected = None
    reason = "Initial add value"

    # call the operation
    stats = S.Statistics()
    result = stats.add(0)

    if result != expected:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    #####################################################################
    # test Statistics.add()

    test_item = 'add() + count()'
    data_in = 0
    expected = 1
    reason = "Check count after one value added"

    # call the operation
    stats = S.Statistics()
    stats.add(data_in)
    result = stats.count()

    if result != expected:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    test_item = 'add() + mean()'
    data_in = [0, 0, 0, 0, 0]
    expected = 0.0
    reason = "Check count after 5 values added"

    # call the operation
    stats = S.Statistics()
    for v in data_in:
        stats.add(v)
    result = stats.mean()

    if result != expected:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    test_item = 'count() + mean()'
    data_in = [0, 0, 0, 0, 0]
    expected = 0
    reason = "Check count after 5 values added"

    # call the operation
    stats = S.Statistics()
    for v in data_in:
        stats.mean()
    result = stats.count()

    if result != expected:
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    #####################################################################
    # test Statistics.mean()

    test_item = 'add() + mean()'
    data_in = 0
    expected = 0
    reason = "Check average after one value added"

    # call the operation
    stats = S.Statistics()
    stats.add(data_in)
    result = stats.mean()

    # We shouldn't test the floating point values for equality, because of round off error
    # So use the close_enough() function.

    if not close_enough(expected, result, 0.0001):
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    #####################################################################
    # test Statistics.mean()

    test_item = 'Statistics.add()'
    data_in = [0, 0, 0, 0, 0]
    expected = 0.0
    reason = "Check average after 5 values added"

    # call the operation
    stats = S.Statistics()
    for v in data_in:
        stats.add(v)
    result = stats.mean()

    if not close_enough(expected, result, 0.0001):
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    #####################################################################
    # test Statistics.count()

    test_item = 'add() + count()'
    data_in = 0
    expected = 1
    reason = "Check average after one value added"

    # call the operation
    stats = S.Statistics()
    stats.add(data_in)
    result = stats.count()

    # We shouldn't test the floating point values for equality, because of round off error
    # So use the close_enough() function.

    if not close_enough(expected, result, 0.0001):
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    #####################################################################
    # test Statistics.count()

    test_item = 'Statistics.count()'
    data_in = [0, 0, 0, 0, 0]
    expected = 5
    reason = "Check average after 5 values added"

    # call the operation
    stats = S.Statistics()
    for v in data_in:
        stats.add(v)
    result = stats.count()

    if not close_enough(expected, result, 0.0001):
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    print('* Test script completed *')
