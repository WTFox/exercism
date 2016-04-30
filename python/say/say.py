def say(num):
    """
    DISCLAIMER: this is probably the worst and most unreadable code I've ever produced.
    Even though all 17 tests passed.

    That being said, This function takes an Int and outputs the phonetic representation as a string.
    :return: string representation of the num
    """
    num = int(num)
    if 0 > num or num >= 1000000000000:
        raise AttributeError

    rev_num_string = str(num)[::-1]
    chunk_strings = [say_chunk(int(x[::-1])) for x in chunks(rev_num_string, 3)]

    mappings = ['', 'thousand', 'million', 'billion']
    result = ["{} {}".format(v, mappings[i]).strip() for i, v in enumerate(chunk_strings)]

    # Terrible code ahead.
    bad_words = ['zero thousand', 'zero million']
    for x in bad_words:
        if x in result:
            result.remove(x)
            if result[1] != 'and':
                result.insert(1, 'and')

    output_string = " ".join(result[::-1]).replace(' and zero', '')
    if output_string.endswith('zero') and len(output_string) > 4:
        output_string = output_string.replace('zero', '').strip()

    return output_string


def chunks(l, n):
    """
    Generator to return sets of n (int) from a l (list)
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]


def say_chunk(num):
    """
    Given a number from 0 to 999 it returns the phonetic representation
    """
    output_string_list = []
    num_string = str(num)

    units = ['zero', 'one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # singles
    if num < 10:
        output_string_list.append(units[num])

    # teens
    elif 10 <= num <= 19:
        output_string_list.append(teens[int(num) % 10])

    # tens
    elif 20 <= num <= 99:
        num_str = str(num)
        modifier = int(num_str[0])
        if int(num_str[1]):
            output_string_list.append("{}-{}".format(tens[modifier - 2], units[int(num) % 10]))
        else:
            output_string_list.append(tens[modifier - 2])

    # hundreds
    elif 100 <= num <= 999:
        output_string_list.append(units[int(num_string[0])])
        output_string_list.append('hundred')

        num = int(num_string[1:])
        if num:
            output_string_list.append('and')
            num_string = str(num)
            modifier = int(num_string[0])

            if int(num_string[1]):
                output_string_list.append("{}-{}".format(tens[modifier - 2], units[int(num_string[1:]) % 10]))
            else:
                output_string_list.append(tens[modifier - 2])

    return ' '.join(output_string_list)

if __name__ == '__main__':
    resp = say(1234876126)
    print(resp)