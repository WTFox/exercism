# exercism io sieve.py

def sieve(limit):
    ''' Write a program that uses the Sieve of Eratosthenes to find all the
    primes from 2 up to a given number.

    The Sieve of Eratosthenes is a simple, ancient algorithm for finding all
    prime numbers up to any given limit. It does so by iteratively marking as
    composite (i.e. not prime) the multiples of each prime,
    starting with the multiples of 2.

    Create your range, starting at two and continuing up to and including the
    given limit. (i.e. [2, limit])

    The algorithm consists of repeating the following over and over:

    - take the next available unmarked number in your list (it is prime)
    - mark all the multiples of that number (they are not prime)

    Repeat until you have processed each number in your range.

    When the algorithm terminates, all the numbers in the list that have not
    been marked are prime.

    '''

    unwantedList = []
    nums = [x for x in range(2, limit+1)]

    for index, num in enumerate(nums):
        for x in nums[index::num][1:]:
            unwantedList.append(x)

    return [x for x in nums if not x in unwantedList]

if __name__ == '__main__':
    sieve(10)
