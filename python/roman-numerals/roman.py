from collections import OrderedDict

__author__ = 'anthonyfox'


def numeral(arabic_num):
    output = []
    working_num = arabic_num
    while working_num:
        out, sub = get_num(working_num)
        working_num -= sub
        output.append(out)

    return ''.join(output)


def get_num(num):
    num_map = OrderedDict()
    num_map['M'] = range(1000, 4000)
    num_map['CM'] = range(900, 1000)
    num_map['D'] = range(500, 900)
    num_map['CD'] = range(400, 500)
    num_map['C'] = range(100, 400)
    num_map['XC'] = range(90, 100)
    num_map['L'] = range(50, 90)
    num_map['XL'] = range(40, 50)
    num_map['X'] = range(10, 40)
    num_map['IX'] = range(9, 10)
    num_map['V'] = range(5, 9)
    num_map['IV'] = range(4, 5)
    num_map['I'] = range(1,4)

    for k, v in num_map.items():
        if num in v:
            return k, v[0]
