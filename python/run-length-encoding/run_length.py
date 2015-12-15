__author__ = 'afox'

import re

def encode(dataset):
    """
    This is working.. but it ain't pretty.

    :param dataset:
    :return:

    """
    counter = 1
    output = []

    for i, v in enumerate(dataset):
        if hasNext(i, dataset):
            nextChar = dataset[i + 1]
            if v == nextChar:
                counter += 1

            elif v != nextChar:
                if counter == 1:
                    output.append("{}{}".format('', v))
                else:
                    output.append("{}{}".format(counter, v))
                counter = 1

        else:
            if v == dataset[i - 1]:
                if counter == 1:
                    output.append("{}{}".format('', v))
                else:
                    output.append("{}{}".format(counter, v))

            else:
                if counter == 1:
                    output.append("{}{}".format('', v))
                else:
                    output.append("{}{}".format(counter, v))

    return ''.join(output)


def decode(dataset):
    pass


def hasNext(index, obj):
    return (len(obj) - index) > 1


if __name__ == '__main__':
    print(encode('AABBBCCCC'))
    # print(encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

