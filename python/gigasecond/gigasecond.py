# exercism gigasecond
from datetime import datetime, timedelta

def add_gigasecond(birthday):
	''' Write a program that will calculate the date that someone turned or will
		celebrate their 1 Gs anniversary.

		A gigasecond is one billion (10**9) seconds.
	'''

	return birthday + timedelta(seconds=10**9)


if __name__ == "__main__":
	print(add_gigasecond(datetime(1988, 10, 05)))
