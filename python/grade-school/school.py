class School(object):
    """
    Write a small archiving program that stores students' names along with the grade that they are in.
    """

    def __init__(self, schoolName):
        self.schoolName = schoolName
        self._db = {}

    def add(self, student, grade):
        try:
            self._db[grade].add(student)
        except KeyError:
            self._db[grade] = {student}

    def sort(self):
        return [(x, tuple(sorted(self._db[x]))) for x in self._db]

    def grade(self, grade):
        try:
            return self._db[grade]
        except KeyError:
            return set()

    @property
    def db(self):
        return self._db


if __name__ == '__main__':
    pass