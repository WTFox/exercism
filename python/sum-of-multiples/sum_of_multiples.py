# exercism sum_of_multiples

def sum_of_multiples(num, factors=[3, 5]):
    '''
    Write a program that, given a number, can find the sum of all the multiples
    of particular numbers up to but not including that number.

    If we list all the natural numbers up to but not including 15 that are
    multiples of either 3 or 5, we get 3, 5, 6 and 9, 10, and 12. The sum of
    these multiples is 45.

    Write a program that can find the sum of the multiples of a given set of
    numbers.
    '''

    output = []
    for x in range(num):
        for f in factors:
            if f == 0:
                output.append(0)
                pass
            elif x % f == 0:
                output.append(x)

    return sum(set(output))
