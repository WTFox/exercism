# exercism io allergies

class Allergies(object):

	@property
	def lst(self):
		return self.allergies

	def __init__(self, allergyScore=0):
		self.allergyScore = allergyScore
		self.allergies = []

		self.allergyMap = {
			128: 'cats',
			64: 'pollen',
			32: 'chocolate',
			16: 'tomatoes',
			8: 'strawberries',
			4: 'shellfish',
			2: 'peanuts',
			1: 'eggs'
		}

		self._calc_allergies()

	def _calc_allergies(self):
		for food in reversed(sorted(self.allergyMap.keys())):
			if self.allergyScore >= food:
				self.allergies.append(self.allergyMap[food])
				self.allergyScore =  self.allergyScore - food
				self._calc_allergies()


	def is_allergic_to(self, food):
		return (food in self.allergies)


if __name__ == '__main__':
	allergies = Allergies(255)
	print(len(allergies.lst))
	print(allergies.lst)
