# exercism io Kindegarten Garden

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
            if len(self.firstRow) - index > 1:
                plantList = [
                    self.firstRow[index],
                    self.firstRow[index+1],
                    self.secondRow[index],
                    self.secondRow[index+1]
                ]
                self.myMap[student] = plantList
                index += 2
        return

    @property
    def students(self):
        return sorted(self._students)

    def plants(self, student):
        translation = {
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass',
            'V': 'Violets'
        }
        return [translation[x] for x in self.myMap[student]]

if __name__ == '__main__':
    garden = Garden("VVCCGG\nVVCCGG")
