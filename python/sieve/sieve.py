# exercism io sieve.py

def sieve(num):
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

    rangeList = [x for x in range(2, num+1)]
    outputList = [x for x in range(2, num+1)]

    for index in rangeList: # first iteration
        for subindex in rangeList:
            try:
                outputList.remove(index+index)
            except:
                pass


        # for f in l:
        #     try:
        #         l.remove(x+x)
        #     except:
        #         pass

    print(outputList)
    return


if __name__ == '__main__':
    sieve(10)
