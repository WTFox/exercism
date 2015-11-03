# exercism io allergies

class Allergies(object):
	''' Write a program that, given a person's allergy score, can tell them
	whether or not they're allergic to a given item, and their full list of
	allergies.

	An allergy test produces a single numeric score which contains the
	information about all the allergies the person has (that they were
	tested for).

	Note: I think in order to pass the extra credit, I'd need to do this in
	binary. I'm submitting this since all tests pass and will work on the extra
	credit test in the 2nd iteration.
	'''

	@property
	def lst(self):
		return self.allergicTo

	def __init__(self, allergyScore=0):
		self.allergyScore = allergyScore
		self.allergicTo = []
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
		for allergy in reversed(sorted(self.allergyMap.keys())):
			if self.allergyScore >= allergy:
				self.allergicTo.append(self.allergyMap[allergy])
				self.allergyScore =  self.allergyScore - allergy
				self._calc_allergies()


	def is_allergic_to(self, allergy):
		return (allergy in self.allergicTo)


if __name__ == '__main__':
	allergies = Allergies(34)
	print(len(allergies.lst))
	print(allergies.lst)
