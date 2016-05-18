class Luhn:
    """
        Write a program that can take a number and determine whether or not it
        is valid per the Luhn formula.
    """

    def __init__(self, num):
        self.num = num

    def addends(self):
        return self._calc_addends(self.num, start=1)

    def checksum(self):
        return sum([int(x) for x in self.addends()])

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def _process_num(num):
        out = num * 2
        if out <= 9:
            return out
        return out - 9

    @classmethod
    def create(cls, num):
        addend = cls._calc_addends(num, start=0)
        mod = sum([int(x) for x in addend]) % 10
        check_digit = (10 - mod) % 10
        return int("{}{}".format(num, check_digit))

    @classmethod
    def _calc_addends(cls, num, start):
        output = []
        for i, n in enumerate(str(num)[::-1], start=start):
            n = int(n)
            if i % 2 == 0:
                output.append(cls._process_num(n))
            else:
                output.append(n)

        return [x for x in output[::-1]]