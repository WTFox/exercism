__author__ = 'afox'


def encode(dataset):
    print([x for x in dataset])
    output = []
    temp1 = list(dataset)
    temp = []
    for i, v in enumerate(dataset):
        if v == dataset[i-1]:
            temp.append(temp1.pop(0))
        else:
            continue

    print(temp)

def decode(dataset):
    pass


if __name__ == '__main__':
    encode('AABBBCCCC')
