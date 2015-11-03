# series exercism io

def slices(string, n):
    ''' Write a program that will take a string of digits and give you all the
        possible consecutive number series of length `n` in that string.
    '''

    if n > len(string) or not n:
        raise ValueError

    output = [[x for x in map(int, string[i:i+n])] for i, v in enumerate(string)]
    return [x for x in output if len(x) == n]
