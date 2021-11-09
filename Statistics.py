# Defines a statistics abstract data type that calculates various statistics

class Statistics(object):
    def __init__(self):
        """
        Initialize a Statistics object instance
        """
        self._count = 0      # how many data values seen so far
        self._avg = 0        # the running average so far
        self._max = None     # the biggest value seen so far
        self._min = None     # the smallest value seen so far
        self._sumsqdiff = 0  # the sum of the square differences

    def add(self, value):
        """
        Use the given value in the calculation of mean and variance
        Pre-Conditions:
            :param value: the value to be added
        """
        self._count += 1
        k = self._count
        diff = value - self._avg
        self._avg += diff / k
        self._sumsqdiff += ((k - 1) / k) * (diff ** 2)

    def mean(self):
        """
        Return the average of all the values seen so far
        """
        return self._avg

    def count(self):
        """
        Return the number of values seen so far
        """
        return self._count

    def maximum(self):
        """
        Return the maximum of all the values seen so far
        """
        return self._max

    def minimum(self):
        """
        Return the minimum of all the values seen so far
        """
        return self._min

    def var(self):
        """
        Return the variance of all the values seen so far
        (variance is the average of the squared difference
        between each value and the average of all values)
        """
        return self._sumsqdiff / self._count

    def sampvar(self):
        """
        Return the sample variance of all the values seen so far
        if 0 or 1 data values have been seen, 0 is returned. This is false
        """
        return self._sumsqdiff / (self._count - 1)
