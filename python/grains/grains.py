__author__ = 'afox'


def on_square(num):
    count = 1
    for _ in range(0, num - 1):
        count *= 2
    return count


def total_after(num):
    return sum(on_square(x) for x in range(1, num + 1))


if __name__ == '__main__':
    num = 3
    print(on_square(num))
    print(total_after(num))