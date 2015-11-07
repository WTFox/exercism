# exercism io Kindegarten Garden

from pprint import pprint

class Garden(object):
    _students = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                 "Ileana", "Joseph", "Kincaid", "Larry"]


    def __init__(self, plants, students=_students):
        self.firstRow, self.secondRow = plants.split('\n')
        self._students = students
        self.myMap = {}

        index = 0
        for student in self.students:
            print(student)
            try:
                plantList = [self.firstRow[index],
                            self.firstRow[index+1],
                            self.secondRow[index],
                            self.secondRow[index+1]]
            except IndexError:
                continue
            self.myMap[student] = plantList
            index += 2

        print(self.myMap)
        return

    @property
    def students(self):
        return sorted(self._students)

    def plants(self, name):
        translation = {
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass',
            'V': 'Violets'
        }

        print([translation[x] for x in self.myMap[name]])
        return [translation[x] for x in self.myMap[name]]


if __name__ == '__main__':
    garden = Garden("VVCCGG\nVVCCGG")
    garden.plants("Bob")
