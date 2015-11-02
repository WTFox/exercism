
class Allergies(object):

	@property
	def lst(self):
		return self.allergies

	def __init__(self, allergyScore=0):
		self.allergyScore = allergyScore
		
		self.allergies = []
		self.allergyMap = {
			1: 'eggs',
			2: 'peanuts',
			4: 'shellfish',
			8: 'strawberries',
			16: 'tomatoes',
			32: 'chocolate',
			64: 'pollen',
			128: 'cats'
		}

		workingNum = self.allergyScore
		for food in self.allergyMap.keys():
			if workingNum > food:
				self.allergies.append(self.allergyMap[food])
				# workingNum = workingNum - food
			
		
	def is_allergic_to(self, food):
		return (food in self.allergies)
	
		