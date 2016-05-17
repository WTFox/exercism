__author_ = 'afox'


class Luhn:
    def __init__(self, num):
        self.num = num

    def addends(self):
        rlist = reversed(list(str(self.num)))
        output = []
        for i, n in enumerate(rlist, start=1):
            n = int(n)
            if i % 2 == 0:
                e = n * 2
                if e >= 10:
                    e -= 9
                output.append(e)
            else:
                output.append(n)

        return [x for x in reversed(output)]

    def checksum(self):
        output = self.addends()
        return sum([int(x) for x in output])

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def create(num):
        # The sum is 6+5+7 = 18. As 18 % 10 = 8
        # (10 - 8) % 10 = 2
        # 2 is the digit checksum control.

        rlist = reversed(list(str(num)))
        output = []
        for i, n in enumerate(rlist, start=0):
            n = int(n)
            if i % 2 == 0:
                e = n * 2
                if e >= 10:
                    e -= 9
                output.append(e)
            else:
                output.append(n)

        num2 = sum([int(x) for x in output])
        mod = num2 % 10
        check_digit = (10 - mod) % 10

        return int("{}{}".format(num, check_digit))


Luhn.create(123)