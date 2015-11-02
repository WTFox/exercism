# exercism.io meetup challenge

from datetime import datetime, timedelta

class MeetupDayException(Exception):
	pass

def meetup_day(intYear, intMonth, strDay, strDesc):
	dayString = {
		1: 'Monday',
		2: 'Tuesday',
		3: 'Wednesday',
		4: 'Thursday',
		5: 'Friday',
		6: 'Saturday',
		7: 'Sunday'
	}

	dayRanges = {
		'teenth': range(13, 20),
		'1st': range(1, 8),
		'2nd': range(8, 16),
		'3rd': range(16, 24),
		'4th': range(24, 32),
		'5th': range(25, 32),
		'last':	range(22, 32),
	}

	for day in dayRanges[strDesc]:
		try:
			workingDate = datetime.date(datetime(intYear, intMonth, day))
		except:
			raise MeetupDayException

		if dayString[workingDate.isoweekday()] == strDay:
			if strDesc == 'last':
				newDate = workingDate + timedelta(days=7)
				if newDate.month == intMonth:
					return newDate
			return workingDate

	return

if __name__ == '__main__':
	meetup_day(2015, 2, 'Sunday', 'last')
