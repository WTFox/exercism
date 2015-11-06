# largest-series-product exercism.io
from functools import reduce
from operator import mul

def largest_product(string, n):
    '''
    Write a program that, when given a string of digits, can calculate the
    largest product for a series of consecutive digits of length n.

    For example, for the input `'0123456789'`, the largest product for a
    series of 3 digits is 504 (7 * 8 * 9), and the largest product for a
    series of 5 digits is 15120 (5 * 6 * 7 * 8 * 9).

    For the input `'73167176531330624919225119674426574742355349194934'`,
    the largest product for a series of 6 digits is 23520.
    '''

    if not len(string):
        return 1

    return max([reduce(mul, x) for x in slices(string, n)])


def slices(string, n):
    '''
    Write a program that will take a string of digits and give you all the
    possible consecutive number series of length `n` in that string.
    '''

    if n > len(string) or not n:
        raise ValueError

    output = [[x for x in map(int, string[i:i+n])] for i, v in enumerate(string)]
    return [x for x in output if len(x) == n]


if __name__ == '__main__':
    print(largest_product("", 0))
