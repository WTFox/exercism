# exercism hamming

def distance(dna1, dna2):
	'''	Write a program that can calculate the Hamming difference between two
		DNA strands.

		It is found by comparing two DNA strands and counting how many of the
		nucleotides are different from their equivalent in the other string.

	    GAGCCTACTAACGGGAT
	    CATCGTAATGACGGCCT
	    ^ ^ ^  ^ ^    ^^
	'''

	hDistance = 0
	for index, value in enumerate(dna1):
		if not value == dna2[index]:
			hDistance += 1

	return hDistance


if __name__ == "__main__":
    print(distance('AG', 'CT'))
