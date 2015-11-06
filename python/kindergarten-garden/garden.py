# exercism io Kindegarten Garden

from pprint import pprint

class Garden(object):
    _students = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                 "Ileana", "Joseph", "Kincaid", "Larry"]

    def __init__(self, plants, students=_students):
        self.plants1, self.plants2 = plants.split('\n')
        self.students = students
        self.myMap = {}


        tmp = []
        for i, p1 in enumerate(self.plants1):
            tmp.append([p1, self.plants2[i]])


        # Failing when parsing plants. Needs major reworking.
        for student in self.students:
            try:
                self.myMap[student] = []
                self.myMap[student].append(tmp[0].pop(0))
                self.myMap[student].append(tmp[1].pop(0))
                self.myMap[student].append(tmp[0].pop(0))
                self.myMap[student].append(tmp[1].pop(0))
            except:
                pass

        print(self.myMap)
        return

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
